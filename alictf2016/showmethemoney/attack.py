#!/usr/bin/env python
import socket as soc

data = ("py" + b'\x00\x0a')

sock = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
sock.connect(('redacted', 9999))

length = sock.send(data)
print 'Sent %d bytes' % length

buf = sock.recv(4096)

while len(buf) != 0:
	print 'Received: %d bytes' % len(buf)
	print buf
	buf = sock.recv(4096)

sock.close()