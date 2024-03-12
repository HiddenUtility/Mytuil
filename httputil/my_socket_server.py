import socket
import json
from traceback import print_exc
from socketutil.SocketServer import SocketServer


class MySocketServer(SocketServer):
    HOST = '0.0.0.0' #全IPOK
    PORT = 8080
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


    def __recieved(self,server_socket: socket.socket):
        print(f"Bind:{self.__port} Buffer: {self.__buffer} TimeOut: {self.__time_out}")
        print("waiting...")
        
        socket_connection, addores_info = server_socket.accept()
        
        data:bytes = socket_connection.recv(self.__buffer)

        print(addores_info)
        text = data.decode()
        # // メソッドが先頭にくるのが仕様
        print("METHOD is",text[:text.find(' ')])
        print('*'*100)
        print(text)
        print('*'*100)

        responce = json.dumps({
            'status' : 200,
            'message' : '平'
        }).encode()
        

        try:
            socket_connection.sendall(responce)
        except Exception as e:
            raise e
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

                