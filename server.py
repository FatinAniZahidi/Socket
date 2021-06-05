import socket
import os
from _thread import*

s = socket.socket()
host = ('192.168.56.104')
print("\n")
port = 8000
ThreadCount = 0

s.bind((host,port))

#allow the server to listen incoming connection
s.listen(2000)
print(host)
print(port)
print("\n Waiting for incoming connections ...\n")
print("----------------------------------------------")

#receive requested file from client
def threaded_client(connection):

        connection.send(str.encode(' File available = file.py'))
        while True:

                data = connection.recv(1024)
                reply = ' Server notice your requested file : '+data.decode('utf-8')
                if not data:
                        break
                connection.sendall(str.encode(reply))
        connection.close()

#connection between client and server
while True:

        connect, addr = s.accept()
        print('\n Connected to :'+addr[0]+':'+str(addr[1]))
        start_new_thread(threaded_client, (connect, ))

       #count the number of client
        ThreadCount += 1
        print(' Client Number : '+str(ThreadCount))
        print("----------------------------------------------")

        #read the file that has been transmitted
        filename = input(str("\n Enter name of the sending file : "))
        file = open(filename , 'rb')
        file_data = file.read(1024)
        connect.send(file_data)
        print(" Data has been successfully transmitted!\n")

s.close()
