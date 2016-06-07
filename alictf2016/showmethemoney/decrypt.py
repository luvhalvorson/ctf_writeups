#!/usr/bin/env python
import base64
from Crypto.Cipher import AES

key = "58897d583d888978b62469889d584472"
cipher = AES.new(key, AES.MODE_ECB, '')

with open('flag.txt', 'rb') as fstream:
	data = base64.b64decode(fstream.read())
	output = cipher.decrypt(data)
	
with open('flag_out', 'wb') as fstream:
	fstream.write(output)
	