# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 17:02:59 2023

@author: nanik
"""
import socket
from traceback import print_exc, format_exc

from socketutil.request_data import RequestData
from socketutil.response_data import ResponseData

class Client:
    HOST = "127.0.0.1"
    PORT = 58888
    BUFFER = 1024
    
    def __init__(self):
        pass

    def send(self, request: RequestData) -> ResponseData:
        if not isinstance(request, RequestData): raise TypeError("request is RequestData")
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client_socket.connect((self.HOST, self.PORT))
            client_socket.sendall(request.to_bytes())
            print("waiting resopnce")
            data:bytes = client_socket.recv(self.BUFFER)
            response = ResponseData().load_bytes(data)
            return response
        except Exception:
            print_exc()
            data = dict(status="400",body=format_exc())
            return ResponseData().load_dict(data)
        finally:
            client_socket.close()
    

    