# BitArray('uintle:12=1024')

import socket
from bitstring import BitStream, BitArray
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.connect(("255.255.255.255", 5011))
# bs = BitStream(s.fileno())
bitarr = BitArray('0xff00ff00ff00ff00')
# s.sendto(bitarr.bytes,("127.0.0.1", 5011))
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.sendto(bitarr.bytes,("255.255.255.255", 5011))
