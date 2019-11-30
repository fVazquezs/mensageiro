import socket
import sys

client = socket.socket()

port = 8080

client.connect(('localhost', port))

print(client.recv(1024))

print("Send a message: ")

message = input()

client.send(message.encode())

client.close()