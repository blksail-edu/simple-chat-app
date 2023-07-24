import socket
import unittest

class Chatroom (object):

    def __init__(self, name: str, uuid: str, messages: list):
        if name is None:
            print("Please enter a name for the chatroom.")
        else:
            self.name = name
            print("Your name is" + name, self.name)

        if len(name) > 16:
            RaiseError
        
        self.uuid = uuid
        self.messages = messages


    


    

    

    
