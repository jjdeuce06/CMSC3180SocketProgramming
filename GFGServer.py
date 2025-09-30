# first of all import the socket library 
import socket             

# next create a socket object 
s = socket.socket()         
print ("Socket successfully created")

# reserve a port on your computer in our 
# case it is 12345 but it can be anything 
port = 31800                

# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests 
# coming from other computers on the network 
#s.bind(('', port))         
#print ("socket binded to %s" %(port)) 

# put the socket into listening mode 
s.listen(5)     
print ("socket is listening")         

# Establish connection with client. 
c, addr = s.accept()     
print ('Got connection from', addr )

# a forever loop until we interrupt it or 
# an error occurs 
while True: 

    # send a thank you message to the client. encoding to send byte type. 
    sentence = c.recv(1024).decode()
    echo = c.recv(1024).decode()
    print("Echo: ", echo)
    if sentence.lower() == 'exit':
        print("Exiting...")
        break
    if echo.lower() == 'y':
        print("From Client:", sentence)
        capitalizedSentence = sentence.upper()
        c.send(capitalizedSentence.encode())
    elif echo.lower() == 'n':
        print("From Client:", sentence) 

c.close()
    