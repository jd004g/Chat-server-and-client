import sys
import socket

host = ''

port = ''

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

hostInput = raw_input("Host: ")
if hostInput == hostInput:
        host = hostInput

portInput = input("Port: ")
if portInput == portInput:
        port = portInput

sock.connect((host, port))
while True:
	message = raw_input("Type Here: ")
	sock.send(message)
	print 'Waiting for reply'
	reply = sock.recv(2000)
	print 'Received reply: ', repr(reply)
sock.close()
