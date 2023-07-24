import socket
import datetime
import client


now = datetime.datetime.now()
class Message:
    def __init__(self, sender: str, payload: str, timestamp: datetime.datetime, chatroom_id: str, uuid: str):
        self.sender = sender  

        if payload is None:
            Exception("Message can't be blank")
        else:
            self.payload = payload
        self.timestamp = now
        
        self.chatroom_id = chatroom_id
        self.uuid = uuid

    
