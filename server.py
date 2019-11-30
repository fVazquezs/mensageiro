import socket

ser = socket.socket()
print("Socket created")

port = 8080

ser.bind(('', port))
print("Server created in %s" %(port))

ser.listen(1)

while True:
    c, addr = ser.accept()
    print("Connected from ", addr)

    c.send(b'thanks')
    answer = c.recv(1024).decode()
    print(answer)
    c.close()