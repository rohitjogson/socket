#! /usr/bin/python3

import socket
import json
import re

_HOST='localhost'
_PORT=9000

#new socket
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('socket created')

client_socket.connect((_HOST,_PORT))

print('your are connected to localhost ')

while True:
    try:
        data=client_socket.recv(24)
        if(data=='quit'):
            break
        else:
            print(data.decode())
    except socket.error as e:
        print(e)
    data=input('<client> :')
    data=data.encode()
    client_socket.send(data)

client_socket.close()
