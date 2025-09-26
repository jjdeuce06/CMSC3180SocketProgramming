from socket import *



#Server
#serverName = 'DRACO1' # I assume this will be Draco?
serverPort = 38100
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(("158.83.11.22", serverPort))
sentence = input('Input lowercase sentence:')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('From Server:', modifiedSentence.decode())
clientSocket.close()

