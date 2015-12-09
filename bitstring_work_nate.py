import bitstring
from bitstring import BitArray
from mood import constructBody


# Frame
#size # 2 bytes
# origin      = BitArray(uint=0,	length=2)
# tagged      = BitArray(bool=True,	length=1)
# addressable = BitArray(bool=True,	length=1)
# protocol    = BitArray(uintle=1024,	length=12)
protocol    = BitArray('0x0034')
source      = BitArray(uintle=73,	length=32)

# Frame address
target       = BitArray(uintle=229195914516597,	length=64)	# MAC address: d0:73:d5:11:98:75
reserved0    = BitArray(uint=0,				length=48)
reserved1    = BitArray(uint=0,				length=6)
ack_required = BitArray(bool=True)
res_required = BitArray(bool=False)
sequence     = BitArray(uintle=0,				length=8)

# Protocol header
reserved2 = BitArray(uintle=0,	 length=64)
_type     = BitArray(uintle=102, length=16)
reserved3 = BitArray(uintle=0,	 length=16)

# PayLoad
# reserved4 = BitArray(uintle=0, length=8)

# duration  = BitArray(uintle=)

temp = protocol + source \
	+ target + reserved0 + reserved1 + ack_required + res_required + sequence \
	+ reserved2 + _type + reserved3 + constructBody( (0,65535, 52428) , 500 )

size = BitArray(uintle=len(temp + 16)/8, length = 16)

hexToBinary = {
	'0':'0000',
	'1':'0001',
	'2':'0010',
	'3':'0011',
	'4':'0100',
	'5':'0101',
	'6':'0110',
	'7':'0111',
	'8':'1000',
	'9':'1001',
	'a':'1010',
	'b':'1011',
	'c':'1100',
	'd':'1101',
	'e':'1110',
	'f':'1111',
}

foo = str(size + temp).replace('0x','')
toSend = ''.join([hexToBinary[c] for c in foo])

print toSend

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.sendto(toSend.bytes,("255.255.255.255", 56700))