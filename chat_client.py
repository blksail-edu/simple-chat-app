import socket as skt
import chatroom
import client
import message
import server
import chat_server
import threading

def client_program():
    """Allows client to send and recieve message to and from server after authentication.

    """
    host = "10.29.63.52" # Currently the IP address of Emily's rasp-pi
    port = 6347 # best number fr

    server = skt.socket() # creates client socket
    server.connect((host, port)) # connect client socket to server

    chatting = False # when True, client socket remains open
    registering = True # when True, client is undergoing registering process


    while registering:
        # server.recv(1024).decode('utf-8') # receives Signup/Login request
        registerType = input("Sign up or Login?")
        server.send(registerType.encode('utf-8')) # prompts for Signup/Login

        if registerType.lower().replace(" ", "") == "login":
            # server.send("login".encode('utf-8'))
            server.send(input("Username: ").encode('utf-8'))
            server.send(input("Password: ").encode('utf-8'))
            if server.recv(1024).decode('utf-8') == "connection complete":
                chatting = True
                print("Login Complete")
                registering = False
                data = server.recv(1024).decode('utf-8')
                print(data)
            else: 
                pass
        if registerType.lower().replace(" ", "") == "signup":
            server.send(input("Create Username: ").encode('utf-8'))
            server.send(input("Create Password: ").encode('utf-8'))
            if server.recv(1024).decode('utf-8') == "Thank you for joining! Connection complete.":
                chatting = True
                print("Thank you for joining! Sign Up complete.")
                registering = False
                data = server.recv(1024).decode('utf-8')
                print(data)
                readThread = threading.Thread(target=read, args=(server,))
                readThread.start()
                writeThread = threading.Thread(target=write, args=(server,))
                writeThread.start()
            else:
                pass


    # while chatting: 
    #     # server.send(message.encode('utf-8')) #Im not sure I understand what this is for - Daniel
    #     data = server.recv(1024).decode('utf-8') # data is the message sent back to the client
    #     print(data) # prints data from server into client terminal
    #     message = input("Message: ").encode('utf-8') # allows user to send more message to 
    #     if message.strip().lower() == "shutdown": # "Shutdown" from client is not sent to server. Closes client socket
    #         setBoolean = False
    # server.close()

def write(server):
    while True:
        try:
            message = input("Message: ").encode('utf-8')
            server.send(message)
        except:
            break

def read(server):
    while True:
        try:
            data = server.recv(1024).decode('utf-8')
            if data:
                print(data)
        except:
            break

if __name__ == '__main__':
    client_program()



