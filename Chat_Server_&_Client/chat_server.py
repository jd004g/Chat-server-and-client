#!/usr/bin/env python

import sys
import socket

print 'Server started'

host = ''
port = 6666
#Connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port)) 
sock.listen(1)
conn, addr = sock.accept()
print 'Connected: ', addr
#Main loop
while True:
	print 'Waiting for Message'
	data = conn.recv(2000)
	print 'Message Recieved: ', repr(data)
	reply = raw_input("Reply: ")
	conn.sendall(reply)

#Close connection
conn.close()
