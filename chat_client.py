import socket as skt
import chatroom
import client
import message
import server
import chat_server

def client_program():
    """Allows client to send and recieve message to and from server after authentication.

    """
    host = "10.29.122.55" # Currently the IP address of Emily's rasp-pi
    port = 6345 # best number fr

    clientSocket = skt.socket() # creates client socket
    clientSocket.connect((host, port)) # connect client socket to server

    setBoolean = True # when True, client socket remains open

    message = input("Message: ") 
    while setBoolean: 
        clientSocket.send(message.encode())
        data = clientSocket.recv(1024).decode() # data is the message sent back to the client
        print(data) # prints data from server into client terminal
        message = input("Message: ") # allows user to send more message to 
        if message.strip().lower() == "Shutdown": # "Shutdown" from client is not sent to server. Closes client socket
            setBoolean = False
    clientSocket.close()

if __name__ == '__main__':
    client_program()