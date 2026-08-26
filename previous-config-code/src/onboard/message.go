package utils

import (
	"bytes"
	"encoding/binary"
	"fmt"
)

//                     1                   2                   3
// 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2
// +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
// |      SRC      |       DST     |   PORT        |      OPT      |
// +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
// |                              TIME                             |
// +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
// |                              TIME                             |
// +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
// |            PARAM0             |            PARAM1             |
// +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
// |                     APPLYTIME (SCHENAL only)                  |
// +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
// |                     APPLYTIME (SCHENAL only)                  |
// +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
// |                    CYCLEPERIOD (SCHENAL only)                 |
// +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
// |                    CYCLEPERIOD (SCHENAL only)                 |
// +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
// |   ENTRYNUM (SCHENAL only)     |   GATE_TIME (SCHENAL only)    ...
// +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
// |                      GATE_STATUS (SCHENAL only)               ...
// +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+


const (
	PORTNUM     = 6
	QUEUENUM    = 8
	GUARULARITY = 10
	MAXINTEVAL  = 1e8
)

const (
	SCHENAL   = 0x7F
	LINKSPEED = 0x01
	VLAN = 0x02
)

type Header struct {
	Src    uint8
	Dst    uint8
	Port   uint8
	Opt    uint8
	Time   uint64
	Param0 uint16
	Param1 uint16
}

type GCL struct {
	ApplyTime   uint64
	CyclePeriod uint64
	EntryNum    uint16

	//only values from 640 to 655350 are allowed.
	GateTime   []uint64
	GateStatus []byte
}

type Msg struct {
	Header
	GCL
}

func FromBuf(buf []byte) Msg {
	var msg Msg
	msg.Src = uint8(buf[0])
	msg.Dst = uint8(buf[1])
	msg.Port = uint8(buf[2])
	msg.Opt = uint8(buf[3])
	msg.Time = uint64(binary.LittleEndian.Uint64(buf[4:12]))
	msg.Param0 = uint16(binary.LittleEndian.Uint16(buf[12:14]))
	msg.Param1 = uint16(binary.LittleEndian.Uint16(buf[14:16]))

	if msg.Opt == SCHENAL {
		var gcl GCL
		gcl.ApplyTime = uint64(binary.LittleEndian.Uint64(buf[16:24]))
		gcl.CyclePeriod = uint64(binary.LittleEndian.Uint64(buf[24:32]))
		gcl.EntryNum = uint16(binary.LittleEndian.Uint16(buf[32:34]))
		gcl.GateTime = Buf2Uint64(buf[34 : 34+8*gcl.EntryNum])
		gcl.GateStatus = buf[34+8*gcl.EntryNum : 34+8*gcl.EntryNum+gcl.EntryNum]
		msg.GCL = gcl
	}
	return msg
}

func (pkt *Msg) ToBuf() []byte {
	buf := make([]byte, 0)
	buf = append(buf, byte(pkt.Src))
	buf = append(buf, byte(pkt.Dst))
	buf = append(buf, byte(pkt.Port))
	buf = append(buf, byte(pkt.Opt))

	temp := make([]byte, 8)
	binary.LittleEndian.PutUint64(temp, uint64(pkt.Time))
	buf = append(buf, temp...)

	temp = make([]byte, 2)
	binary.LittleEndian.PutUint16(temp, uint16(pkt.Param0))
	buf = append(buf, temp...)

	temp = make([]byte, 2)
	binary.LittleEndian.PutUint16(temp, uint16(pkt.Param1))
	buf = append(buf, temp...)

	if pkt.Opt == SCHENAL {
		temp = make([]byte, 8)
		binary.LittleEndian.PutUint64(temp, uint64(pkt.ApplyTime))
		buf = append(buf, temp...)

		temp = make([]byte, 8)
		binary.LittleEndian.PutUint64(temp, uint64(pkt.CyclePeriod))
		buf = append(buf, temp...)

		temp = make([]byte, 2)
		binary.LittleEndian.PutUint16(temp, uint16(pkt.EntryNum))
		buf = append(buf, temp...)

		buf = append(buf, Uint642Buf(pkt.GateTime)...)
		buf = append(buf, pkt.GateStatus...)
	}

	return buf
}

func Buf2Uint64(buf []byte) []uint64 {
	var data64 []uint64
	for i, _ := range buf {
		if i%8 == 0 {
			targetBuf := buf[i : i+8]
			data64 = append(data64, binary.LittleEndian.Uint64(targetBuf))
		}
	}
	return data64
}

func Uint642Buf(arr []uint64) []byte {
	var payload bytes.Buffer
	for _, v := range arr {
		err := binary.Write(&payload, binary.LittleEndian, v)
		if err != nil {
			fmt.Println(err)
		}
	}
	return payload.Bytes()
}
