#!/usr/bin/python2.7
import dpkt
import sys
import socket

def main():
	if (len(sys.argv) < 2):
		print "error: need argument"
		sys.exit(1)
	filename = sys.argv[1]
	#outfile = 'output.txt'
	f = open(filename, "rb") 
	pcap = dpkt.pcap.Reader(f)
	arrIP = []
	arr = []
	for ts, buf in pcap:
		try:
			eth = dpkt.ethernet.Ethernet(buf)
			if eth.type==dpkt.ethernet.ETH_TYPE_IP:
				ip=eth.data
				if ip.p == dpkt.ip.IP_PROTO_TCP:
					tcp = ip.data
					if tcp.flags == 2:
						if(ip.src not in arrIP):
							arrIP.append(ip.src)
							arr.append(1)
						elif(ip.src in arrIP):
							tempsrc = arrIP.index(ip.src)
							arr[tempsrc] = arr[tempsrc] + 1
					if tcp.flags == 18:
						if(ip.dst not in arrIP):
							continue
						elif(ip.dst in arrIP):
							tempdst = arrIP.index(ip.dst)
							arr[tempdst] = arr[tempdst] - 3
					
		except:
			continue
	#out = open('output.txt', 'w')
	for i in range(len(arr)):
		if(arr[i] > 0):
			print socket.inet_ntoa(arrIP[i])
			#out.write(socket.inet_ntoa(arrIP[i]))
			#out.write('\n')
	#out.close()
	f.close()


def tcp_flags(flags):
	ret = ''
	if flags & dpkt.tcp.TH_SYN:
		ret = ret + 'S'
	if flags & dpkt.tcp.TH_ACK:
		ret = ret + 'A'
	return ret



if __name__ == '__main__':
    main()
