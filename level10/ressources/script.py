#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 6969))
s.listen(1)
while True:
	conn, addr = s.accept()
	while True:
		data = conn.recv(64)
		if not data:
			break
		print(data.decode(errors='ignore'))
