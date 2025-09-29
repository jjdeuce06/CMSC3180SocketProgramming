# Import socket module 
import socket             

# Create a socket object 
s = socket.socket()         

# Define the port on which you want to connect 
port = int(input("Enter port number: ")) 

# connect to the server on local computer 
s.connect(('127.0.0.1', port)) 

while True:
    sentence = input("Enter a sentence: ")
    if sentence.lower() == 'exit':
        print("Exiting...")
        capitalizedSentence = sentence.upper()
        s.send(capitalizedSentence.encode())
        break
    echo = input("Server echo? (y/n): ")
    if echo.lower() == 'n':
        capitalizedSentence = sentence.upper()
        s.send(capitalizedSentence.encode())
        s.send(echo.encode())
    elif echo.lower() == 'y':
        capitalizedSentence = sentence.upper()
        s.send(capitalizedSentence.encode())
        s.send(echo.encode())
        modifiedSentence = s.recv(1024)
        print("From Server:", modifiedSentence.decode())
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

s.close() 