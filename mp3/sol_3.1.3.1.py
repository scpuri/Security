# -*- coding: utf-8 -*-
# strip() remove any leading or trailing whitespace characters
import sys
import math
import itertools
import hashlib

input1 = sys.argv[1]
input2 = sys.argv[2]
outfile = sys.argv[3]

with open(input1) as f:
	input1 = f.read().strip()
with open(input2) as f:
	input2 = f.read().strip()

hash1 = hashlib.sha256(input1)
hash2 = hashlib.sha256(input2)
hash1 = hash1.hexdigest()
hash2 = hash2.hexdigest()

hamm_dist = sum(itertools.imap(str.__ne__, hash1, hash2))
hamm_dist = hex(hamm_dist).lstrip("0x")

f = open(outfile, 'w')
f.write(hamm_dist)
f.close()
