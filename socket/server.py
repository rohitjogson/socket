#! /usr/bin/python3

import socket
import json
import re

_HOST='localhost'
_PORT=9000

#new socket
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('socket created')
#bind the socket with localhost and port 9000

server_socket.bind((_HOST,_PORT))
print('socket binded on '+ _HOST)
#now socket is listening for new connection
print('server is listening.....')
server_socket.listen(1)

#it create only one connection

(client_conn,adderss)=server_socket.accept()
print(adderss)
print('server sending massage.... ')
while True:
    print(len(client_conn.recv(24)))
    try:
        if(len(client_conn.recv(24))>1):
            print(client_conn.recv(1024).decode())
        else:
            server_massage=input('<Server> : ')
            server_massage=server_massage.encode()
            client_conn.send(server_massage)
            print('')
    except socket.error as e:
        print(e)



server_socket.close()






