from socket import *

#Client
clientInput = int(input("Enter a port number: "))

try:
    clientPort = clientInput
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', clientPort))
    serverSocket.listen(10)
    print("The server is ready to receive")
    while True:
        connectionSocket, addr = serverSocket.accept()
        sentence = connectionSocket.recv(1024).decode()
        capitalizedSentence = sentence.upper()
        connectionSocket.send(capitalizedSentence.encode())
        connectionSocket.close()
except Exception as e:
    print("An error occurred:", e)
