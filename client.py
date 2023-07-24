class Client:
    def __init__(self, username: str, ip_address: str, password: str, uuid: str):
        self.username = username
        self.ip_address = ip_address
        self.password = password
        self.uuid = uuid