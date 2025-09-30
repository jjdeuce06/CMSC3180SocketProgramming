# Import socket module 
import socket            

# Create a socket object 
s = socket.socket()         
print("----------------Client----------------")
while True:
    # Ask user for the port
    port = int(input("Enter port number: ")) 

    # attempt connect to the server
    try:
        s.connect(('158.83.11.22', port)) 
        print("Connection established")
        serverGreeting = s.recv(1024)
        print("From Server:", serverGreeting.decode())
        break
    #print an error message if no connection can be made
    except ConnectionRefusedError:
        print("Connection refused. Make sure the port number is correct.")

# loop to send and receive data
while True:
    #ask user for a sentence
    sentence = input("Enter a sentence (exit to quit): ")
    #if the user enters exit, close the connection and exit the loop
    if sentence.lower() == 'exit':
        print("Exiting...")
        capitalizedSentence = sentence.upper()
        s.send(capitalizedSentence.encode())
        break
    #if user enters anything else, prompt for echo option
    echo = input("Server echo? (y/n): ")
    #if user enters n, send the sentence and reprompt
    if echo.lower() == 'n':
        capitalizedSentence = sentence.upper()
        s.send(capitalizedSentence.encode())
        modifiedSentence = s.recv(1024)
    #if the user enters y, send the sentence, receive the capitalized sentence back, and print it
    elif echo.lower() == 'y':
        capitalizedSentence = sentence.upper()
        s.send(capitalizedSentence.encode())
        modifiedSentence = s.recv(1024)
        print("From Server:", modifiedSentence.decode())
    #if user enters anything else, restart prompt from the sentence
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

#close the socket
s.close() 