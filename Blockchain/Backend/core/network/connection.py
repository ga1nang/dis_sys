import socket
from Blockchain.Backend.core.network.network import NetworkEnvelope, FINISHED_SENDING

class Node:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.ADDR = (self.host, self.port)
        
    #start the server and bind it to a port Number
    def startServer(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDR)
        self.server.listen()                                                       
        
        
    def connect(self, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #???????
        self.socket.connect((self.host, self.port))
        print(f"Connected success {self.host} and {self.port}")
        return self.socket
    
    
    def acceptConnection(self):
        self.conn, self.addr = self.server.accept()
        self.stream = self.conn.makefile('rb', None)
        print("Accepted.....")
        return self.conn, self.addr
    
    
    def closeConnection(self):
        self.socket.close()
        
    
    def send(self, message):
        envelope = NetworkEnvelope(message.command, message.serialize())
        self.socket.sendall(envelope.serialize())
        
    
    def read(self):
        envelope = NetworkEnvelope.parse(self.stream)
        return envelope                                      