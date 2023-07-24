import socket as skt

def create_socket():
    protocol = skt.SOCK_STREAM  # Protocol = TCP
    addressFamily = skt.AF_INET  # Address family = IPv4

    # socket creation
    socket = skt.socket(addressFamily, protocol)
    # Bind information
    serverIp = "10.29.122.55"
    serverPrt = 6345

    #hostname:
    hostName = socket.gethostname()

    # Binding port and IP
    socket.bind((serverIp, serverPrt))

    print("Binded successfully!")

    print(f"The IP for the server is: {serverIp}")
    print(f"The IP for the server is: {serverPrt}")

    return socket

def broadcast(msg): #broadcasting message to all clients
    for client in clients:
        client.send(msg.encode('utf-8'))

def client_handling(client):
    """If the client raises an exception, then break out of the loop, remove everything"""
    while True:
        try:
            message = client.recv(2048)
            broadcast(message)
        except:
            i = clients.index(client) #keep client socket here, and update it later
            client.close() #close client socket
            username = usernames[i]
            broadcast(f"user: {username} have left the chat.")
            break


if name == "main":
    socket = create_socket()

    socket.listen(20)

    clients = []
    usernames = []
    ipAddresses = []
    passwords = []
    uuids = []

    setBoolean =  True # variable for the true or false of the server running

    while setBoolean:
        # accept a connection from the client
        client, addr = socket.accept()
        print(f'connected to computer: {addr}')

        #initial message login or sign up
        client.send("Login in or sign up".encode('utf-8'))