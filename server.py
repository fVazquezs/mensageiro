import socket
from threading import Thread

def threaded(c, addr, sockets, client):
    openned = True
    while openned:
        answer = c.recv(1024).decode()
        if answer == 'quit':
            sockets.quit(client)
            openned = False
        else:
            sockets.say(answer, client)

def main():
    ser = socket.socket()
    print("Socket created")

    port = 8080

    ser.bind(('', port))
    print("Server created in %s" %(port))

    ser.listen(2)
    sockets = Socket()

    while True:
        c, addr = ser.accept()
        print("Connected from ", addr)
        c.send("You are connected".encode())
        name = c.recv(1024).decode()
        client = Client(c, name)
        sockets.addClient(client)
        thread = Thread(target = threaded, args = (c, addr, sockets, client, ))
        thread.start()
    c.close()

class Client:
    def __init__(self, socket, name):
        super().__init__()
        self.socket = socket
        self.name = name

class Socket:
    def __init__(self):
        super().__init__()
        self.clients = []
    
    def addClient(self, client):
        self.clients.append(client)

    def say(self, message, client):
        for cli in self.clients:
            if client.name != cli.name:
                send = client.name + " says: " + message
                cli.socket.sendall(send.encode())
    
    def quit(self, client):
        self.clients.remove(client)
        for cli in self.clients:
            send = client.name + " quit"
            cli.socket.sendall(send.encode())

main()