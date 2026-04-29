package main

// import (
// 	"TSN/src/utils"
// 	"fmt"
// 	"net"
// 	"time"
// )

// const FREQUENCY = 1000
// const ADDRESS = "192.168.0.3:54321"

// func main() {
// 	msg := utils.Msg{}
// 	msg.Src = 1
// 	msg.Dst = 0
// 	msg.Port = 2
// 	msg.Opt = utils.SCHENAL
// 	msg.Time = 0
// 	msg.Param0 = 0
// 	msg.Param1 = 0

// 	msg.ApplyTime = 0
// 	msg.CyclePeriod = utils.MAXINTEVAL / 2
// 	msg.EntryNum = 2
// 	msg.GateTime = []uint64{650, 650}
// 	msg.GateStatus = []byte{0x01, 0xff}

// 	conn, err := net.Dial("udp", ADDRESS)
// 	if err != nil {
// 		fmt.Println(err)
// 	}

// 	defer conn.Close()

// 	for {
// 		conn.Write(msg.ToBuf())
// 		time.Sleep(1 / FREQUENCY)
// 	}

// }
