import socket

class Chatroom (object):

    def __init__(self, name: str, uuid: str, messages: list):
        if name is None:
            print("Please enter a name.")
        else:
            self.name = name
            print("Your name is" + name, self.name)
        
        self.uuid = uuid
        self.messages = messages

        
    


    

    

    
