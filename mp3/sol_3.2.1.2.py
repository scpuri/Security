from pymd5 import md5,padding
import urllib
import sys

query = sys.argv[1]
command = sys.argv[2]
output = sys.argv[3]
with open(query) as f:
	query = f.read().strip()
with open(command) as f:
	command = f.read().strip()

outString='http://ece422.org/project3/api?token='
h=md5(state=query[6:38].decode("hex"), count=512)
h.update(command)
outString+=h.hexdigest()
outString+=query[39:]
outString+=urllib.quote(padding(len(query[39:])*8))
outString+=command

f = open(output, 'w')
f.write(outString)
f.close()


