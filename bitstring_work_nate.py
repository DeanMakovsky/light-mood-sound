import bitstring

# Frame
#size
origin      = BitArray(uintle=0,	length=2)
tagged      = BitArray(bool=True,	length=1)
addressable = BitArray(bool=True,	length=1)
protocol    = BitArray(uintle=1024,	length=12)
source      = BitArray(uintle=73,	length=32)

# Frame address
target       = BitArray(uintle=229195914516597,	length=64)	# MAC address: d0:73:d5:11:98:75
reserved0    = BitArray(uintle=0,				length=48)
reserved1    = BitArray(uintle=0,				length=6)
ack_required = BitArray(bool=False,				length=1)
res_required = BitArray(bool=False,				length=1)
sequence     = BitArray(uintle=0,				length=8)

# Protocol header
reserved2 = BitArray(uintle=0,	 length=64)
_type     = BitArray(uintle=102, length=16)
reserved3 = BitArray(uintle=0,	 length=16)

# PayLoad
reserved4 = BitArray(uintle=0, length=8)

duration  = BitArray(uintle=)