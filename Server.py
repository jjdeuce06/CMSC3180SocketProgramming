from socket import *


serverPort = 31800
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive")
while True:
    connectionSocket, addr = serverSocket.accept()
    print("Connected to:", addr)
    connectionSocket.close()
    break

