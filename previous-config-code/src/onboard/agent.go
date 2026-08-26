package agent

import (
	"TSN/src/utils"
	"encoding/binary"
	"fmt"
	"net"
	"os"
	"os/exec"
	"strconv"
	"strings"
	"time"
)

type Agent struct {
	ID        int
	IP        string
	LocalPort int
	HostClock uint64

	LinkIn  [utils.PORTNUM]int
	LinkOut [utils.PORTNUM]int

	PortName        [utils.PORTNUM]string
	PortClock       [utils.PORTNUM]uint64
	CurrentSchedule [utils.PORTNUM]*utils.GCL
	QueuePriority   [utils.PORTNUM][utils.QUEUENUM]uint8

	MsgChan chan *utils.Msg
}

func (agent *Agent) Init(id int, ip string, localPort int) {
	agent.ID = id
	agent.IP = ip
	agent.LocalPort = localPort
	agent.HostClock = uint64(time.Now().UnixNano())
	agent.PortName = [utils.PORTNUM]string{"sw0ep", "sw0p1", "sw0p2", "sw0p3", "sw0p4", "sw0p5"}
	for i := 2; i != utils.PORTNUM; i++ {
		initSchedule := utils.GCL{}
		initSchedule.ApplyTime = 0
		initSchedule.CyclePeriod = utils.MAXINTEVAL
		initSchedule.EntryNum = 1
		initSchedule.GateTime = append(initSchedule.GateTime, 650)
		initSchedule.GateStatus = append(initSchedule.GateStatus, 0xff)

		agent.CurrentSchedule[i] = &initSchedule

		agent.configure(uint8(i), utils.LINKSPEED, 0, 100, 0)
		agent.schedule(uint8(i), &initSchedule)
	}

	agent.MsgChan = make(chan *utils.Msg, 1024)

	go agent.listen(uint16(agent.LocalPort))

	for {
		msg := <-agent.MsgChan
		if msg.Opt != utils.SCHENAL {
			go agent.configure(msg.Port, msg.Opt, msg.Time, msg.Param0, msg.Param1)
		} else {
			go agent.schedule(msg.Port, &msg.GCL)
		}
	}
}

func (agent *Agent) listen(port uint16) {
	ServerAddr, err := net.ResolveUDPAddr("udp", ":"+strconv.Itoa(int(port)))
	if err != nil {
		fmt.Println(err)
	}
	ServerConn, err := net.ListenUDP("udp", ServerAddr)
	if err != nil {
		fmt.Println(err)
	}
	defer ServerConn.Close()
	for {
		buf := make([]byte, 1500)
		_, _, err := ServerConn.ReadFromUDP(buf)
		if err != nil {
			fmt.Println(err)
		}
		msg := utils.FromBuf(buf)
		agent.MsgChan <- &msg
	}
}

func (agent *Agent) send() {
	c, err := net.Dial("udp4", "192.168.0.21:19981")
	if err != nil {
		fmt.Println("[!] UDP Error", err)
	}
	bs := make([]byte, 2)
	binary.BigEndian.PutUint16(bs, utils.SCHENAL)
	_, err = c.Write(bs)
	if err != nil {
		fmt.Println("[!] UDP send failed")
	}
}

func (agent *Agent) configure(port uint8, opt uint8, time uint64, param0 uint16, param1 uint16) {
	switch opt {
	case utils.LINKSPEED:
		// ethtool -s sw0p2 speed 100 duplex full autoneg on
		portname := agent.PortName[port]
		speed := strconv.Itoa(int(param0))
		output, err := exec.Command(
			"ethtool",
			"-s",
			portname,
			"speed",
			speed,
			"duplex",
			"full",
			"autoneg",
			"on").Output()
		fmt.Println(
			"ethtool",
			"-s",
			portname,
			"speed",
			speed,
			"duplex",
			"full",
			"autoneg",
			"on",
		)
		if err != nil {
			fmt.Println("[!] Link speed,", err)
		} else {
			fmt.Println("[-] Link speed,", output)
		}

	case utils.VLAN:
		// bridge vlan add dev sw0p3 vid 7
		var oper string
		var portname string
		var vid string

		portname = agent.PortName[port]
		vid = strconv.Itoa(int(param1))
		if param0 == 0 {
			oper = "add"
		} else if param0 == 1 {
			oper = "del"
		}
		output, err := exec.Command(
			"bridge",
			"vlan",
			oper,
			"dev",
			portname,
			"vid",
			vid).Output()
		fmt.Println(
			"bridge",
			"vlan",
			oper,
			"dev",
			portname,
			"vid",
			vid,
		)
		if err != nil {
			fmt.Println("[!] Vlan setting,", err)
		} else {
			fmt.Println("[-] Vlan setting,", output)
		}

	default:
		fmt.Println("[!] Option not existing: ", opt)
	}

}

func (agent *Agent) schedule(port uint8, gcl *utils.GCL) {
	// Prepare GCL table file
	gclPath := "./gcl/" + strconv.Itoa(int(port)) + "_" + strconv.Itoa(int(gcl.ApplyTime)) + ".cfg"
	f, err := os.Create(gclPath)
	if err != nil {
		fmt.Println(err)
	}
	for i := 0; i != int(gcl.EntryNum); i++ {
		if gcl.GateTime[i] < 650 || gcl.GateTime[i] > 655350 {
			fmt.Println("[!] GCL interval out of range [650,655350)")
		}
		_, err := f.WriteString(
			fmt.Sprintf("sgs %s 0x%02X\n", strconv.FormatUint(gcl.GateTime[i], 10), gcl.GateStatus[i]),
		)
		if err != nil {
			fmt.Println("[!] Writing GCL table,", err)
		}

	}
	f.Close()

	// Write GCL table
	// tsntool st wrcl <sw0p3> </home/root/qbv.cfg>
	portArg := agent.PortName[int(port)]
	output, err := exec.Command(
		"tsntool",
		"st",
		"wrcl",
		portArg,
		gclPath).Output()
	fmt.Println(
		"tsntool",
		"st",
		"wrcl",
		portArg,
		gclPath,
	)
	if err != nil {
		fmt.Println("[!] Wrcl,", err)
	} else {
		fmt.Println("[-] Configure,", output)
	}

	// Apply schedule
	// tsntool st configure <basetime> <cycletime> <cycletime-extension> <interface>
	var (
		secondBase  uint64
		NanoBase    uint64
		basetimeArg string
	)

	if gcl.ApplyTime != 0 {
		secondBase = gcl.ApplyTime / 1e9
		NanoBase = gcl.ApplyTime % 1e9
		basetimeArg = fmt.Sprintf("%s.%s", strconv.FormatUint(secondBase, 10), strconv.FormatUint(NanoBase, 10))
	} else {
		basetimeArg = "+0.0"
	}

	cycletimeArg := "1/" + strconv.FormatUint(1e9/gcl.CyclePeriod, 10)
	cycletimeExt := "0"
	interfaceArg := agent.PortName[port]
	output, err = exec.Command(
		"tsntool",
		"st",
		"configure",
		basetimeArg,
		cycletimeArg,
		cycletimeExt,
		interfaceArg).Output()
	fmt.Println("tsntool",
		"st",
		"configure",
		basetimeArg,
		cycletimeArg,
		cycletimeExt,
		interfaceArg)
	if err != nil {
		fmt.Println("[!] Configure,", err)
	} else {
		fmt.Println("[-] Configure,", output)
	}

	if port == 3 {
		agent.send()
	}
}

func (agent *Agent) getTime(port uint8) uint64 {
	path := fmt.Sprintf("/sys/class/net/%s/ieee8021ST/CurrentTime", agent.PortName[port])
	timeCur, err := os.ReadFile(path)
	if err != nil {
		fmt.Println("[!] No current time " + agent.PortName[port])
		curr := uint64(time.Now().UnixNano())
		return curr
	}
	timeStr := strings.Split(string(timeCur), ".")

	secondTime, _ := strconv.ParseUint(timeStr[0][:10], 10, 64)
	nanoTime, _ := strconv.ParseUint(timeStr[1][:9], 10, 64)
	return secondTime*1e9 + nanoTime
}
