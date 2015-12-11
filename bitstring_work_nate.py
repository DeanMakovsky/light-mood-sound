import bitstring
from bitstring import BitArray
from mood import constructBody

def make_frame():
	# Frame
	#size # 2 bytes
	# origin      = BitArray(uint=0,	length=2)
	# tagged      = BitArray(bool=True,	length=1)
	# addressable = BitArray(bool=True,	length=1)
	# protocol    = BitArray(uintle=1024,	length=12)
	protocol    = BitArray('0x0034')
	source      = BitArray(uintle=0,	length=32)

	# Frame address
	# target       = BitArray(uintle=229195914516597,	length=64)	# MAC address: d0:73:d5:11:98:75
	target       = BitArray(uintle=0,	length=64)	# MAC address: d0:73:d5:11:98:75
	reserved0    = BitArray(uint=0,				length=48)
	reserved1    = BitArray(uint=0,				length=6)
	ack_required = BitArray(bool=False)
	res_required = BitArray(bool=False)
	sequence     = BitArray(uintle=0,				length=8)

	header = protocol + source 	+ target + reserved0 + reserved1 + ack_required + res_required + sequence
	return header

def make_power(level):


	# Protocol header
	reserved2 = BitArray(uintle=0,	 length=64)
	# _type     = BitArray(uintle=102, length=16)  # set color
	_type     = BitArray(uintle=21, length=16)  # power level (2 byte payload)
	reserved3 = BitArray(uintle=0,	 length=16)

	# PayLoad
	# reserved4 = BitArray(uintle=0, length=8)
	# duration  = BitArray(uintle=)
	payload = BitArray(uintle=level, length=16)

	temp = make_frame() + reserved2 + _type + reserved3 # + constructBody( (0,65535, 52428) , 500 )

	temp += payload

	size = BitArray(uintle=len(temp + 16)/8, length = 16)

	toSend = size + temp
	return toSend

def make_color(hue, sat, bright):
	# Protocol header
	reserved2 = BitArray(uintle=0,	 length=64)
	# _type     = BitArray(uintle=102, length=16)  # set color
	_type     = BitArray(uintle=102, length=16)  # color (HSBK & time + padding)
	reserved3 = BitArray(uintle=0,	 length=16)

	# PayLoad
	# reserved4 = BitArray(uintle=0, length=8)
	# duration  = BitArray(uintle=)
	payload = constructBody((hue, sat, bright), 500)

	temp = make_frame() + reserved2 + _type + reserved3

	temp += payload

	size = BitArray(uintle=len(temp + 16)/8, length = 16)

	toSend = size + temp
	return toSend

# toSend = BitArray('0x240000342855fb6600000000000000000000000000000100000000000000000036000000')
# 2600003400000000000000000000000000000000000000000000000000000000150000000000
# 2600003400000000000000000000000000000000000000000000000000000000150000000100


import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

import time

theip = "255.255.255.255"

toSend = make_power(0)
s.sendto(toSend.bytes,(theip, 56700))
time.sleep(5)
toSend = make_power(65535)
s.sendto(toSend.bytes,(theip, 56700))
time.sleep(5)
toSend = make_power(0)
s.sendto(toSend.bytes,(theip, 56700))
time.sleep(5)
toSend = make_power(65535)
s.sendto(toSend.bytes,(theip, 56700))
