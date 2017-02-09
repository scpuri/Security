# -*- coding: utf-8 -*-
# strip() remove any leading or trailing whitespace characters
import re
import sys
keyinput = sys.argv[2]
cipherinput = sys.argv[1]
with open(keyinput) as f:
	key = f.read().strip()
with open(cipherinput) as f:
	cipher = f.read().strip()
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet = list(alphabet)

keydict = dict(zip(key, alphabet))

pattern = re.compile('|'.join(keydict.keys()))
plaintxt = pattern.sub(lambda x: keydict[x.group()], cipher)

outfile = sys.argv[3]
f = open(outfile, 'w')
f.write(plaintxt)
f.close()
