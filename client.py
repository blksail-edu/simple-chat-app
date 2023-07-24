import socket as skt

class Client:
    def __init__(self, username: str, ip_address: str, password: str, uuid: str):
        self.username = username
        
        if username is None:
            raise Exception("Username can't be blank")
        else:
            self.username = username


        self.ip_address = skt.gethostbyname(skt.gethostname())


        if len(password) < 8 or len(password) > 16:
            raise Exception("Password should be between 8 and 16 characters")
        else:
            self.password = password

        self.uuid = uuid


