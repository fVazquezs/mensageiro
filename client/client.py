import socket
import sys
from threading import Thread

def receiver(client):
    openned = True
    while openned:
        try:
            message = client.recv(1024).decode()
            print(message)
            if message == 'quit':
                openned = False
                client.close()
        except socket.error: 
            openned = False
            print("Bye")

def sender(client):
    openned = True
    while openned:
        send = input()
        client.send(send.encode())
        if send == 'quit':
            openned = False
            client.close()


def main():
    client = socket.socket()
    port = 8080
    client.connect(('localhost', port))
    print(client.recv(1024).decode())
    print("Your name: ", end ='')
    name = input()
    client.sendall(name.encode())
    success = client.recv(1024).decode()
    if success == 'OK':
        receiverThread = Thread(target = receiver, args = (client, ))
        receiverThread.start()
        senderThread = Thread(target = sender, args = (client, ))
        senderThread.start()
    else:
        print(success) 
        client.close()
main()