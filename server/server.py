import socket
from threading import Thread
import clientsManager
import client

def threaded(c, addr, clientManager, client):
    openned = True
    while openned:
        answer = c.recv(1024).decode()
        if answer == 'quit':
            clientManager.quit(client)
            openned = False
        else:
            clientManager.say(answer, client)

def main():
    ser = socket.socket()
    print("Socket created")

    port = 8080

    ser.bind(('', port))
    print("Server created in %s" %(port))

    ser.listen(6)
    clientManager = clientsManager.ClientsManager()

    while True:
        c, addr = ser.accept()
        print("Connected from ", addr)
        c.send("You are connected".encode())
        name = c.recv(1024).decode()
        newClient = client.Client(c, name)
        addClient = clientManager.addClient(newClient)
        if addClient:
            c.sendall('OK'.encode())
            thread = Thread(target = threaded, args = (c, addr, clientManager, newClient, ))
            thread.start()
        else:
            print('error')
            c.sendall(addClient.encode())
            c.close()
    c.close()

main()