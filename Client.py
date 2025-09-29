from socket import *

#Client
clientInput = int(input("Enter a port number: "))

try:
    clientPort = clientInput
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(('158.83.11.22', clientPort))
    print("Connection established with server on port", clientPort)
    while True:
        sentence = input("Enter a sentence: ")
        if sentence.lower() == 'exit':
            print("Exiting...")
            break
        capitalizedSentence = sentence.upper()
        clientSocket.send(capitalizedSentence.encode())
        modifiedSentence = clientSocket.recv(1024)
        print("From Server:", modifiedSentence.decode())
except Exception as e:
    print("An error occurred:", e)
    clientSocket.close()

clientSocket.close()
