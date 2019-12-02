class ClientsManager:
    def __init__(self):
        super().__init__()
        self.clients = []
    
    def addClient(self, client):
        # if len(self.clients) == 2:
        #     return 'Server full'
        for cli in self.clients:
            if client.name == cli.name:
                return 'Nickname already exists'
        self.clients.append(client)
        return True

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
