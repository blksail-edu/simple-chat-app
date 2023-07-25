import socket
import unittest

class Chatroom (object):

    def __init__(self, name: str, uuid: str, messages: list):
        if name is None:
            print("Please enter a name for the chatroom.")
        else:
            self.name = name
            print("Your name is" + name, self.name)

        if len(name) > 20:
            raise ValueError ("Chatroom name must be between 1 and 20 characters.")
        
        self.uuid = uuid
        self.messages = messages
    
    def changeNickname():
        if message.lower() == "change nickname": #message function
            new_nickname = input("Enter your new nickname")
            if new_nickname == user.nickname:
                print("Your new nickname is the same as your current nickname.")
            else:
                user.nickname == new_nickname
                print("You new nickname is " + new_nickname)
                