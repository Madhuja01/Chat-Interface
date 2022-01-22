import socket
import sys
import time

s = socket.socket()
host = socket.gethostname()
print("You are online : ", host)
port = 8080
s.bind((host,port))
s.listen(1)
conn, addr = s.accept()
print("Sithara is online...")
print("")
while 1:
    message = input(str(">> "))
    message = message.encode()
    conn.send(message)
    print("Delivered...")
    print("")
    incoming_message = conn.recv(1024)
    incoming_message = incoming_message.decode()
    print("Sithara :", incoming_message)
    print("")
