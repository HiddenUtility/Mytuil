# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 17:02:44 2023

@author: nanik
"""

import socket
from traceback import print_exc, format_exc
import time
from datetime import datetime

from socketutil.request_data import RequestData
from socketutil.response_data import ResponseData

class Server:
    HOST = ""
    PORT = 58888
    BUFFER = 1024
    
    def __init__(self):
        pass
    
    def process(self,request: RequestData) -> ResponseData:
        
        # /* 何かの処理
        time.sleep(3)
        # */
        
        data = dict(status="200", body="")
        return ResponseData().load_dict(data)

        
    def recieved(self,server_socket: socket):
        print("waiting...")
        conn, _ = server_socket.accept()
        try:
            data:bytes = conn.recv(self.BUFFER)
            print(datetime.now(),"Recived Request !!")
        except Exception as error:
            conn.close()
            raise Exception(error)
        
        request = RequestData().load_bytes(data)
        
        try:
            response:ResponseData = self.process(request)
        except Exception:
            data = dict(status="500", body=format_exc())
            response = ResponseData().load_dict(data)

        try:
            conn.sendall(response.to_bytes())
            print(datetime.now(),"Return Response!!")
        except Exception as error:
            raise Exception(error)
        finally:
            conn.close()  
    
    def run(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.HOST, self.PORT))
        server_socket.listen() #セッション数設定可
        print(" ++++++++++++++++ running ++++++++++++++++")
        while True:
            try:
                self.recieved(server_socket)
            except Exception:
                server_socket.close()
                print_exc()
                
