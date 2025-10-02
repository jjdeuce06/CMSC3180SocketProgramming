# Import socket module 
import socket            

# Create a socket object 
run = True  
print("----------------Client----------------")
while run:
    # Ask user for the port
    s = socket.socket() 
    echo = 1 
    port_input = input("Enter port number (:exit to quit): ")
    if port_input.lower() == ':exit':
        print("Exiting Program...")
        break
    if not port_input.isdigit():
        print("Invalid input. Please enter a valid port number.")
        continue
    # attempt connect to the server
    try:
        port = int(port_input)
        s.connect(('158.83.11.22', port)) 
        print("Connection established")
        serverGreeting = s.recv(1024)
        print("From Server:", serverGreeting.decode())
        print("---------------Commands---------------\n1. :help\n2. :echo off\n3. :echo on\n4. :new port\n5. :exit")
        # loop to send and receive data
        while True:
            #ask user for a sentence
            sentence = input("Enter a sentence (:exit to quit): ")

            #if the user enters nothing, reprompt to stop breakages
            if sentence == '':
                print("Please enter a valid sentence.")
                continue

            #if the user enters exit, close the connection and exit the loop
            if sentence.lower() == ':exit':
                print("Exiting Connection...")
                capitalizedSentence = sentence.upper()
                s.send(capitalizedSentence.encode()) 
                run = False
                #close the socket
                s.close() 
                break
            
            if sentence.lower() == ':new port':
                print("Allowing New Port...")
                #close the socket
                s.close() 
                break
            
            if sentence.lower() == ':help':
                print("---------------Commands---------------\n1. :help\n2. :echo off\n3. :echo on\n4. :new port\n5. :exit")
                continue

            if sentence.lower() == ':echo off':
                echo = 0
                continue
        
            if sentence.lower() == ':echo on':
                echo = 1
                continue

            #if user enters n, send the sentence and reprompt
            if echo == 0:
                capitalizedSentence = sentence.upper()
                s.send(capitalizedSentence.encode())
                modifiedSentence = s.recv(1024)
            #if the user enters y, send the sentence, receive the capitalized sentence back, and print it
            elif echo == 1:
                capitalizedSentence = sentence.upper()
                s.send(capitalizedSentence.encode())
                modifiedSentence = s.recv(1024)
                print("From Server:", modifiedSentence.decode())
            #if user enters anything else, restart prompt from the sentence
            else:
                print("Invalid input. Please enter :echo on or :echo off.")
                continue
    #print an error message if no connection can be made
    except ConnectionRefusedError:
        print("Connection refused. Make sure the port number is correct.")
    except OverflowError:
        print("Port number must be in the range 0-65535.")

    

#close the socket
s.close() 