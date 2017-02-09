# -*- coding: utf-8 -*-
# strip() remove any leading or trailing whitespace characters
import sys
import math

cipherinput = sys.argv[1]
keyinput = sys.argv[2]
modulofile = sys.argv[3]
outfile = sys.argv[4]

with open(keyinput) as f:
	key = f.read().strip()
with open(cipherinput) as f:
	ciphertext = f.read().strip()
with open(modulofile) as f:
	modulo = f.read().strip()

ciphertext = int(ciphertext,16)
modulo = int(modulo,16)
key = int(key,16)


plaintext = pow(ciphertext, key) % modulo
plaintext = hex(plaintext).rstrip("L").lstrip("0x") or "0"

f = open(outfile, 'w')
f.write(plaintext)
f.close()
