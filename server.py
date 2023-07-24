import socket as skt
# import unittest
class SERVER:
    """you input your server Ip and server port number,
    and the progran will check for validity for both input"""
def init(self, serverIp, serverPrt):
        self.serverPrt = int(serverPrt)
        if serverPrt != range(6000,49000):
            raise ValueError
        self.serverPrt = serverPrt
"""this tests for the validity of ip address by using the inet_aton to convert the ip address to a 32 bit
data, if it can successfully convert """
def validate_ip_address(self, serverIp):
        try:
            skt.inet_aton(self, serverIp)
            return self.serverIp
        except skt.error:
            return "Invalid input"

# if __name__ == "__main__":
#     unittest.main()
