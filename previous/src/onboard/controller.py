from ctypes import Structure, c_uint8, c_uint16, c_uint64
import socket
from numpy import uint64


class Header(Structure):
    _pack_ = 1
    _fields_ = [
        ("src", c_uint8),
        ("dst", c_uint8),
        ("port", c_uint8),
        ("opt", c_uint8),
        ("time", c_uint64),
        ("param0", c_uint16),
        ("param1", c_uint16),
        ("apply_time", c_uint64),
        ("cycle_period", c_uint64),
        ("entry_num", c_uint16),
    ]


class Packet:

    def __init__(self):
        pass

    # payload is a double list
    def pkt2Buf(self, _src, _dst, _port, _opt, _time, _param0, _param1,
                _apply_time, _cycle_period, _entry_num, _gate_time,
                _gate_status):

        header_buf = Header(
            _src,
            _dst,
            _port,
            _opt,
            _time,
            _param0,
            _param1,
            _apply_time,
            _cycle_period,
            _entry_num,
        )

        double_arr = c_uint64 * _entry_num

        payload_buf = double_arr(*_gate_time)

        buf = bytes(header_buf) + bytes(payload_buf) + bytes(_gate_status)
        return buf

    def buf2Pkt(self, buffer):
        self.header = Header.from_buffer_copy(buffer[:34])
        double_arr = c_uint64 * self.header.entry_num
        self._gate_time = double_arr.from_buffer_copy(
            buffer[34:34 + 8 * self.header.entry_num])
        self._gate_status = buffer[34 + 8 * self.header.entry_num:34 +
                                   (8 + 1) * self.header.entry_num]
        return self.header._fields_, self._gate_time, self._gate_status


if __name__ == "__main__":
    pkt = Packet()
    buf = pkt.pkt2Buf(1, 0, 2, 0x7F, 0, 0, 0, 0, int(1e8 / 2), 2, [650, 650],
                      [0x01, 0xff])
    out_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # out_sock.sendto(buf, ("192.168.0.3", 54321))
    out_sock.sendto(buf, ("127.0.0.1", 54321))