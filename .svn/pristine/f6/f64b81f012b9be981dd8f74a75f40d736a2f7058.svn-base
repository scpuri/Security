#WHA:
#Input{inStr: a binary string of bytes}
#Output{outHash: 32-bit hashcode for the inStr in a series of hex values}
#Mask: 0x3FFFFFFF
#outHash: 0
#for byte in input
#intermediate_value = ((byte XOR 0xCC) Left Shift 24) OR
#((byte XOR 0x33) Left Shift 16) OR
#((byte XOR 0xAA) Left Shift 8) OR
#(byte XOR 0x55)
#outHash =(outHash AND Mask) + (intermediate_value AND Mask)
#return outHash
# -*- coding: utf-8 -*-
import sys
import math
import itertools
import hashlib
import binascii
import random
import string

def WHA(inputstr):
	mask = 1073741823
	outhash = 0
	for i in range(len(inputstr)/8):
		temp = int(inputstr[0+i*8:8+i*8], 2)
		intermediate_val = ((temp ^ 0xcc) << 24) | ((temp ^ 0x33) << 16) | ((temp ^ 0xaa) << 8) | (temp ^ 0x55)
		outhash = (outhash & mask) + (intermediate_val & mask)
 	outputhash = format(outhash, 'x')
	return outputhash


input1 = sys.argv[1]
outfile = sys.argv[2]

with open(input1) as f:
	input1 = f.read().strip()

input_binary = ''.join('{0:08b}'.format(ord(x), 'b') for x in input1)

f = open(outfile, 'w')
f.write(WHA(input_binary))
f.close()

#for j in range(8, 64, 8):
#	for i in range(2**20):
#		input1 = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(j))
#		input1 = ''.join('{0:08b}'.format(ord(x), 'b') for x in input1)
#		print WHA(input1)
#		if WHA(input_binary) == WHA(input1):
#			print input1
#			print WHA(input1)
#			break
#	if WHA(input_binary) == WHA(input1):
#		break
#		

