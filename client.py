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
        except socket.error as err: 
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
    print("Your name: ", end ='')
    name = input()
    client.connect(('localhost', port))
    client.sendall(name.encode())
    receiverThread = Thread(target = receiver, args = (client, ))
    receiverThread.start()
    senderThread = Thread(target = sender, args = (client, ))
    senderThread.start()

main()