import socket
import os
from _thread import*

#create socket
s = socket.socket()
host = input(str("\n Enter server ip address: "))
port = 8000
s.connect((host,port))
print(" Successfully Connected ...\n")

respons = s.recv(1024)
print(respons)

#requested file from the server
Input = input('\n Enter name of the requested file: ')
s.send(str.encode(Input))
response = s.recv(1024)
print(response.decode('utf-8'))

#receive file from server
filename = input(str("\nEnter name of the incoming file: "))
file = open(filename, 'wb')
file_data = s.recv(1024)
file.write(file_data)
file.close()
print("File has been successfully received!\n")

s.close()
