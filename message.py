import socket
import datetime

class Message:
    def __init__(self, sender: str, payload: str, timestamp: datetime.datetime, chatroom_id: str, uuid: str):
        self.sender = sender  
        self.payload = payload
        self.timestamp = timestamp
        self.chatroom_id = chatroom_id
        self.uuid = uuid

    
