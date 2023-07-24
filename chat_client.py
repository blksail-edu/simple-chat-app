import socket as skt

def client_program():
    host = "10.29.122.55"
    port = 6345

    clientSocket = skt.socket()
    clientSocket.connect((host, port))

    message = input("Message: ")

    setBoolean = True

    while setBoolean: # adding condition later
        clientSocket.send(message.encode())
        data = clientSocket.recv(1024).decode # data is the message sent back to the client
        print("Username: " + data)
        message = input("Message: ")
    clientSocket.close()

if __name__ == '__main__':
    client_program()