import socket as skt
import unittest
class Server:
    """you input your server Ip and server port number,
    and the progran will check for validity for both input"""
def __init__(self, serverIp: str, serverPrt: int):
        self.serverPrt = serverPrt 
        if serverPrt != range(6000,49000):
            raise ValueError
        self.serverPrt = serverPrt
        self.serverIp = serverIp
"""this tests for the validity of ip address by using the inet_aton to convert the ip address to a 32 bit
data, if it can successfully convert """
def validate_ip_address(self, serverIp):
        try:
            skt.inet_aton(self, serverIp)
            return self.serverIp
        except skt.error:
            return "Invalid input"

if __name__ == "__main__":                                                                                                                               
    if __name__ == "__main__":
        unittest.main()

#trials
def test_serverPrt(self):
    self.assertTrue(Server.validate_ip_address("10.29.33.207"), "10.29.33.207")
