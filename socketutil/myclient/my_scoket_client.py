

from __future__ import annotations
import socket
from socketutil.SocketClient import SocketClient
from socketutil.reqs.request_data import RequestData
from socketutil.resp.response_data import ResponseData

class MySocketClient(SocketClient):
    HOST = 'localhost'
    PORT = 54321
    ENCODING = 'utf-8'
    BUFFER = 4096
    TIMEOUT = 10

    __host: str
    __port: int
    __buffer: int
    __time_out : int

    def __init__(self,host=HOST, port=PORT, buffer=BUFFER, time_out=TIMEOUT):
        self.__host = host
        self.__port = port
        self.__buffer = buffer
        self.__time_out = time_out

    def __connect(self, request: RequestData):
        resp = ResponseData()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((self.__host, self.__port))
            client_socket.settimeout(self.__time_out)
            client_socket.sendall(request.to_bytes())
            received_data:bytes = client_socket.recv(self.__buffer)
            resp = resp.load_bytes(received_data)
        return resp

        
    def set_host(self, host) -> MySocketClient:
        return MySocketClient(host=host, port = self.__port)

    # @orverride
    def post_tset(self) -> ResponseData:
        request = RequestData().set_test()
        return self.post(request)


    # @orverride
    def post(self, request: RequestData) -> ResponseData:
        if not isinstance(request, RequestData): raise TypeError()
        data = request.to_bytes()
        if len(data) > self.__buffer: raise Exception("buffer sizeが足りません。")
        resp = RequestData()
        try:
            resp = self.__connect(request)
        except Exception as e:
            resp = resp.set_error(str)
        return resp
