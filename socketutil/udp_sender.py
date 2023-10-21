# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 21:16:47 2023

@author: nanik
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 17:02:59 2023

@author: nanik
"""
import socket
import json
from datetime import datetime

class Sender:
    HOST = "127.0.0.1"
    PORT = 58888
    ENCODING = "utf-8"
    BUFFER = 1024
    
    def __init__(self):
        self.responce = None
    
    def request(self, data: dict):

        data["timestamp"] = str(datetime.now())
        json_data: bytes = json.dumps(data).encode(self.ENCODING)
        
        sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            sender_socket.connect((self.HOST, self.PORT))
            sender_socket.sendall(json_data)
        except Exception as error:
            print(error)
        finally:
            sender_socket.close()
    
    def get_response(self):
        if not hasattr(self, "responce"):
            raise Exception("NOT recieved responce")
        return self.responce
        


if __name__ == "__main__":
    
    data = dict(message="you can fly !!")
    sender = Sender()
    sender.request(data)
    print(sender.get_response())
    