import socket
import sys
import time

s = socket.socket()
host = input(str("Please enter friend's name : "))
port = 8080
s.connect((host,port))
print("Madhuja is online...")
print("")
while 1:
        incoming_message = s.recv(1024)
        incoming_message = incoming_message.decode()
        print("Madhuja :", incoming_message)
        print("")
        message = input(str(">> "))
        message = message.encode()
        s.send(message)
        print("Delivered...")
        print("")
