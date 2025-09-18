
clientInput = int(input("Enter a port number: "))

while clientInput != -1:
    print("You entered:", clientInput)
    echoInput = input("Display server echo? (y/n): ")
    if echoInput.lower() == 'y':
        print("Server echo enabled.")
    else:
        print("Server echo disabled.")

    clientInput = int(input("Enter a port number: "))

print("Exiting program.")
