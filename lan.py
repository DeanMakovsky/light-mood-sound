import socket
import bitstring


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("localhost", 5000))


import random
num = int( random.random() * 4000 + 1)
print num


# to_send = (frame_fmt, 16, b'\x00\x00', b'\x01', b'\x01', b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01', num )
s.send(to_send)



s.close()