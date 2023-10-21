# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 21:14:27 2023

@author: nanik
"""



import socket
import json
import time
from datetime import datetime

class Server:
    HOST = ""
    PORT = 58888
    ENCODING = "utf-8"
    BUFFER = 1024
    
    def __init__(self):
        pass
    
    def process(self,dict_: dict) -> dict:
        
        mess = dict_.get("message")
        if mess is None:return dict(flag="Failure!!")
        print(dict_["timestamp"],dict_["message"])
        # /* 何かの処理
        time.sleep(3)
        # */
        return_data = dict(flag="Success!!")
        return_data["timestamp"] = str(datetime.now())
        return return_data
        
    def recieved(self,server_socket: socket):
        print("waiting...")
        conn, _ = server_socket.accept()
        try:
            data = conn.recv(self.BUFFER)
            print(datetime.now(),"Recived Request !!")
        except Exception as error:
            conn.close()
            raise Exception(error)
        
        try:
            json_data: bytes = data.decode(self.ENCODING)
            dict_ = json.loads(json_data)
            # /* 何かの処理
            self.process(dict_)
            # */
        except Exception as error:
            conn.close()
            raise Exception(error)
             

    
    def run(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_socket.bind((self.HOST, self.PORT))
        server_socket.listen() #セッション数設定可
        print(" ++++++++++++++++ running ++++++++++++++++")
        while True:
            try:
                self.recieved(server_socket)
            except Exception as error:
                server_socket.close()
                print(error)
        

if __name__ == "__main__":
    Server().run()