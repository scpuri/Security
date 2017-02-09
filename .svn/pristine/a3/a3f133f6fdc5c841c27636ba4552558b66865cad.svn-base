# -*- coding: utf-8 -*-
# strip() remove any leading or trailing whitespace characters
import re
import sys
import base64
from Crypto.Cipher import AES
from Crypto import Random
import binascii,os


cipherinput = sys.argv[1]
keyinput = sys.argv[2]
ivfile = sys.argv[3]
outfile = sys.argv[4]

with open(keyinput) as f:
	key = f.read().strip()
with open(cipherinput) as f:
	ciphertext = f.read().strip()
with open(ivfile) as f:
	iv = f.read().strip()
iv = iv.decode('hex')
key = key.decode('hex')
ciphertext = ciphertext.decode('hex')
 
decryptor = AES.new(key, AES.MODE_CBC, iv)
plaintext = decryptor.decrypt(ciphertext)

f = open(outfile, 'w')
f.write(plaintext)
f.close()
