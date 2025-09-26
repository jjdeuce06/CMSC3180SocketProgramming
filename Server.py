from socket import *


serverPort = 31800
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('158.83.11.22', serverPort))
serverSocket.listen(1)
print("The server is ready to receive")
#while True:
connectionSocket, addr = serverSocket.accept()
print("Connected to:", addr)
connectionSocket.send("Hello".encode())
connectionSocket.close()

