# Import socket module 
import socket            

# Create a socket object 
s = socket.socket()       
print("----------------Client----------------")
while True:
    # Ask user for the port
    port = int(input("Enter port number: ")) 
    echo = 1

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


print("---------------Commands---------------\n1. :echo off\n2. :echo on\n3. :help\n4. :exit")
# loop to send and receive data
while True:
    
    #ask user for a sentence
    sentence = input("Enter a sentence (:exit to quit): ")
    #if the user enters exit, close the connection and exit the loop
    if sentence.lower() == ':exit':
        print("Exiting...")
        break
    
    if sentence.lower() == ':help':
        print("---------------Commands---------------\n1. :echo off\n2. :echo on\n3. :help\n4. :exit")
        continue
    
    #echo control
    if sentence.lower() == ':echo off':
        echo = 0
        continue
            
    if sentence.lower() == ':echo on':
        echo = 1
        continue
    
    
    #print control  
    if echo == 1:
        capitalizedSentence = sentence.upper()
        s.send(capitalizedSentence.encode())
        modifiedSentence = s.recv(1024)
        print("From Server:", modifiedSentence.decode())
    else:
        capitalizedSentence = sentence.upper()
        s.send(capitalizedSentence.encode())
        #recieves the message but does not save it
        s.recv(1024)
        continue

#close the socket
s.close() 