import socket
import time
from traceback import print_exc, format_exc
from json import JSONDecodeError, JSONEncoder
from socketutil.SocketServer import SocketServer
from socketutil.reqs.request_data import RequestData
from socketutil.resp.response_data import ResponseData

class MySocketServer(SocketServer):
    HOST = '0.0.0.0' #全IPOK
    PORT = 54321
    ENCODING = 'utf-8'
    BUFFER = 4096
    TIMEOUT = 10

    __port: int
    __buffer: int
    __time_out : int

    def __init__(self, 
                 port=PORT, 
                 buffer=BUFFER, 
                 time_out=TIMEOUT,
                 ):
        self.__port = port
        self.__buffer = buffer
        self.__time_out = time_out


    def __process(self,request: RequestData) -> ResponseData:
        resp = ResponseData()
        # /* 何かの処理
        print(request)
        time.sleep(3)
        # */
        return resp
        
    def __recieved(self,server_socket: socket.socket):
        print(f"Bind:{self.__port} Buffer: {self.__buffer} TimeOut: {self.__time_out}")
        print("waiting...")
        
        socket_connection, addores_info = server_socket.accept()
        print(addores_info)
        resp = ResponseData()
        try:
            data:bytes = socket_connection.recv(self.__buffer)
            print(f'received -> {data.decode()}')
            request = RequestData().load_bytes(data)
        except JSONDecodeError:
            resp = ResponseData().set_error(404,'不明なリクエスト')
        except Exception as e:
            socket_connection.close()
            raise Exception(e)
        
        if not resp.is_error():
            try:
                resp = self.__process(request)
            except Exception:
                resp = resp.set_error(500, format_exc())

        try:
            socket_connection.sendall(resp.to_bytes())
            print(resp.to_dict())
        except Exception as error:
            raise Exception(error)
        finally:
            socket_connection.close()  
    
    def __run(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.HOST, self.__port))
        server_socket.listen() #セッション数設定可
        try:
            self.__recieved(server_socket)
        except Exception as e:
            server_socket.close()
            raise e
        finally:
            server_socket.close()


    def run(self):
        while True:
            # 本番はlogger等入れる
            try:
                self.__run()
            except Exception as e:
                print_exc()