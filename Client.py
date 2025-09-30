# Import socket module 
import socket             

# Create a socket object 
s = socket.socket()         

while True:
    # Define the port on which you want to connect 
    port = int(input("Enter port number: ")) 

    # connect to the server on local computer 
    try:
        s.connect(('158.83.11.22', port)) 
        print("Connection established")
        serverGreeting = s.recv(1024)
        print("From Server:", serverGreeting.decode())
        break
    except ConnectionRefusedError:
        print("Connection refused. Make sure the port number is correct.")

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
        #s.send(echo.encode())
        modifiedSentence = s.recv(1024)
    elif echo.lower() == 'y':
        capitalizedSentence = sentence.upper()
        s.send(capitalizedSentence.encode())
        #s.send(echo.encode())
        modifiedSentence = s.recv(1024)
        print("From Server:", modifiedSentence.decode())
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

s.close() 