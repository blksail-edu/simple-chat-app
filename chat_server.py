# first of all import the socket library
import socket            
from server import Server
from client import Client
# next create a socket object

# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 62345    
ip = ''
#Main_server = Server(ip,port)
s = socket.socket()        
clientDict = {#create the client dictionary

}
print ("Socket successfully created")

           
 
s.bind((ip, port))        
print ("socket binded to %s" %(port))
 
# put the socket into listening mode
s.listen(5)    
print ("socket is listening")           
#s.setblocking(False)
# a forever loop until we interrupt it or
# an error occurs
while True:
 
# Establish connection with client.
    
    conn, addr = s.accept() 
    s.setblocking(True)
    print ('Got connection from', addr )
    #check if the client is new, and authenticate them
    conn.send('Send uuid \n'.encode())

    
    uuid = conn.recv(1024 )
    
    s.setblocking(False)
    for uuid in clientDict:
        conn.sendto('New Client, [placeholder] \n',clientDict[uuid].ip_address)

    with conn:# get the actual message
        try:
            data = conn.recv(1024 , socket.MSG_DONTWAIT)
        except BlockingIOError:
            pass #data = bytes("0 0 0 0 0 0 1", 'utf-8')

        if uuid in clientDict.keys():
            pass
        else:
            clientDict[uuid] = Client(uuid,addr)
            conn.send('new user, send username \n'.encode())
            username = conn.recv(1024 , socket.MSG_DONTWAIT)
            clientDict[uuid].username = username
            conn.send('new user, send password\n'.encode())
            password = c.password(1024 , socket.MSG_DONTWAIT)
            clientDict[uuid].password = password
            conn.sendall('new user created\n'.encode())

        for key in clientDict:
            conn.sendto(data,clientDict[key].ip_address)



        

    





  # Close the connection with the client
  #c.close()
   
  # Breaking once connection closed
  #break
