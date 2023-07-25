import socket as skt
import chatroom
import client
import message
import server
import chat_server
import threading

def create_socket():
    # socket creation
    socket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
    # Bind information
    serverIp = "10.29.63.52"
    serverPrt = 6347

    #hostname:
    # hostName = socket.gethostname()

    # Binding port and IP
    socket.bind((serverIp, serverPrt))

    print("Binded successfully!")

    print(f"The IP for the server is: {serverIp}")
    print(f"The IP for the server is: {serverPrt}")

    return socket

def broadcast(msg, username = 'system accouncement'): #broadcasting message to all clients
    for client in clients:
        client.send(f"{username}: {msg}".encode('utf-8'))
    
def client_handling(client, addr, username):
    """If the client raises an exception, then break out of the loop, remove everything"""
    while True:
        try:
            message = client.recv(2048)
            print(message)
            broadcast(message, username)
        except:
            i = clients.index(client) #keep client socket here, and update it later
            client.close() #close client socket
            username = usernames[i]  
            broadcast(f"user: {username} have left the chat.")
            break


if __name__ == "__main__":
    socket = create_socket()

    socket.listen(20)
    
    clients = []
    usernames = ["usernametest"]
    ipAddresses = []
    passwords = ["passwordtest"]
    #NOTE: uuid is the index number

    serverRunning =  True # variable for the true or false of the server running

    while serverRunning:
        # accept a connection from the client
        client, addr = socket.accept()
        print(f'connected to computer: {addr}')

        #initial message login or sign up
        
        testLoginSignUp = client.recv(1024).decode('utf-8').lower().replace(' ', '')

        if testLoginSignUp == "login":
            # client.send("Username: ".encode('utf-8')) in client ask for username/password
            testusername = client.recv(1024).decode('utf-8')
            print(testusername)
            testpassword = client.recv(1024).decode('utf-8')
            print(testpassword)
            if testusername in usernames and testpassword in passwords:
                # clients[passwords.index(tPassword)] = client #update client socket to new client socket
                # ipAddresses[passwords.index(tPassword)] = addr #update ip-address of the new client
                client.send("connection complete".encode('utf-8'))
                #broadcast joining message using the index of the password they gave
                broadcast(f"user: {usernames[passwords.index(testpassword)]} has join the chat")
                thread = threading.Thread(target=client_handling, args=(client, addr, testusername))
                thread.start()
            else:
                client.close()
        elif testLoginSignUp == "signup":
            # client.send("Please Enter Your Username".encode('utf-8'))
            newUsername = client.recv(1024).decode('utf-8')
            print(newUsername)
            # client.send("Please Enter Your Password".encode('utf-8'))
            newPassword = client.recv(1024).decode('utf-8')
            print(newPassword)
            # client.send("Please Re-enter Your Password".encode('utf-8'))
            # checkPassword = client.recv(1024).decode('utf-8')
            checkPassword = newPassword #skip check password process
            if checkPassword == newPassword:
                usernames.append(newUsername)
                passwords.append(newPassword)
                clients.append(client)
                print(str(client))
                ipAddresses.append(addr)
                client.send("Thank you for joining! Connection complete.".encode('utf-8'))
                broadcast(f"user: {usernames[1]} has join the chat")
                thread = threading.Thread(target=client_handling, args=(client, addr, newUsername))
                thread.start()
            else:
                pass