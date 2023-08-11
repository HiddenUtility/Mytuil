# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 17:02:59 2023

@author: nanik
"""
import socket
import json
from datetime import datetime

class Client:
    HOST = "127.0.0.1"
    PORT = 48888
    ENCODING = "utf-8"
    BUFFER = 1024
    
    def __init__(self):
        self.responce = None
    
    def request(self, data: dict):

        data["timestamp"] = str(datetime.now())
        json_data: bytes = json.dumps(data).encode(self.ENCODING)
        
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client_socket.connect((self.HOST, self.PORT))
            client_socket.sendall(json_data)
            print("waiting resopnce")
            data:bytes = client_socket.recv(self.BUFFER)
            json_data:bytes = data.decode(self.ENCODING)
            self.responce = json.loads(json_data)
        except Exception as error:
            print(error)
        finally:
            client_socket.close()
    
    def get_response(self):
        if not hasattr(self, "responce"):
            raise Exception("NOT recieved responce")
        return self.responce
        


if __name__ == "__main__":
    
    data = dict(message="you can fly !!")
    client = Client()
    client.request(data)
    print(client.get_response())
    