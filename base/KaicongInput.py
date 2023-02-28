#import threading
import socket
from urllib.parse import urlparse

#TODO: Extend threading.Thread
class KaicongInput():
    
    def __init__(self, callback, domain, uri_format, packet_size, user="admin", pwd="123456"):
        """ domain:   Camera IP address or web domain 
                      (e.g. 385345.kaicong.info)
        """
        self.callback = callback
        self.running = False
        self.packet_size = packet_size
        self.uri = uri_format % (domain, user, pwd)
        self.stream = None
        self.domain = domain
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def connect(self):
        print ("Opening url: %s" % self.uri)
        url = urlparse(self.uri)
        self.socket.connect((self.domain, 81))
        self.socket.send(b"GET %s HTTP/1.1\r\nHost:%s\r\n\r\n" % ( str.encode(url.path+"?"+url.query), str.encode(self.domain)))
        self.stream = self.socket.recv(self.packet_size)
        
        if not self.stream:
            raise Exception("Error connecting")
    
    def handle(self, data):
        pass
        
    def shutdown(self):
        self.running = False
    
    def read(self):
        result = None
        
        # Loop for things like Video, where multiple reads required to
        # retrieve a frame.
        while not result:
            result = self.handle(self.socket.recv(self.packet_size))
        return result
    
    def run(self):
        try:
            if self.stream:
                self.socket.close()
        
            self.connect()
            self.running = True
            
            while self.running:
                result = self.handle(self.socket.recv(self.packet_size))
                if result:
                    self.callback(result)
        
        finally:
            if self.stream:
                self.socket.close()
                
                
                

