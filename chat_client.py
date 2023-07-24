import socket as skt
import chatroom
import client
import message
import server
import chat_server

def client_program():
    """Allows client to send and recieve message to and from server after authentication.

    """
    host = "10.29.122.55"
    port = 6345

    clientSocket = skt.socket()
    clientSocket.connect((host, port))

    setBoolean = True

    message = input("Message: ")
    while setBoolean: # adding condition later
        clientSocket.send(message.encode())
        data = clientSocket.recv(1024).decode() # data is the message sent back to the client
        print("Username: " + data)
        message = input("Message: ")
        if input == "Shutdown":
            setBoolean = False
    clientSocket.close()

if __name__ == '__main__':
    client_program()