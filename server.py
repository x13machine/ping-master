from datetime import *
import socket
import sys

#settings
HOST = ''
PORT = 4444
KEY="qgpq6XjqH8m5P7AS" # needs to be random so people don't do hacking thing
TIMEOUT = 30 #seconds

servers = {}
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))

print 'Socket bind complete'

def update():
	servs=[]
	for i in servers:
		if (datetime.now()-servers[i]).total_seconds() > TIMEOUT:
			servs+=[i]
	for i in servs:
		servers.pop(i,None)

while 1:
	# receive data from client (data, addr)
	d = s.recvfrom(1024)
	data = d[0]
	addr = d[1]
	parts=data.split(' ')
	
	if len(parts)<2:
		continue
	
	if parts[0] != KEY:
		continue
	cmd = parts[1].lower()

	info = " ".join(parts[2:])

	
	update()
	if cmd == 'ping':
		if info == '':
			info = addr[0]
		
		servers[info] = datetime.now()
		s.sendto(KEY+' pong' , addr)
	elif cmd == 'ls':
		servs = ''
		for i in servers:
			servs +=' '+i
		s.sendto(KEY+' ls' + servs , addr)
		
	print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()
	 
s.close()
