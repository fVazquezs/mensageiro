class Client:
    def __init__(self, socket, name):
        super().__init__()
        self.socket = socket
        self.name = name