from socket import *

#Client
clientInput = int(input("Enter a port number: "))

try:
    clientPort = clientInput
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(('158.83.11.22', clientPort))
    print("Connection established.")
    #while True:
    #connectionSocket, addr = clientSocket.accept()
        #print("Connected to:", addr)
        #sentence = connectionSocket.recv(1024).decode()
        #capitalizedSentence = sentence.upper()
        #connectionSocket.send(capitalizedSentence.encode())
    clientSocket.send("Hello")
    clientSocket.close()
except Exception as e:
    print("An error occurred:", e)
