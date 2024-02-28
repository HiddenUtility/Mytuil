
import socket
from abc import abstractclassmethod, ABC


class SocketServerBase(ABC):
    __socket: socket.socket
    __timeout: int
    __buffer: int

    def __init__(self, timeout:int=60, buffer:int=1024):
        self.__socket = None
        self.__timeout = timeout
        self.__buffer = buffer
        self.close()

    def __del__(self):
        self.close()

    def close(self) -> None:
        try:
            self.__socket.shutdown(socket.SHUT_RDWR)
            self.__socket.close()
        except:
            pass

    def _accept(self, address:tuple[str, int], family:int, typ:int, proto:int) -> None:
        print("Server started :", address)
        self.__socket = socket.socket(family, typ, proto)
        self.__socket.bind(address)
        self.__socket.listen(1)
        print("Server waiting")
        conn, info = self.__socket.accept()
        print(f'''
#####################################
{info}
#####################################
''')
        conn.settimeout(self.__timeout)
        try:
            message_recv = conn.recv(self.__buffer).decode('utf-8')
            message_resp = self._respond(message_recv)
            conn.send(message_resp.encode('utf-8'))
        finally:
            conn.close()
            self.close()

    @abstractclassmethod
    def _respond(self, message:str) -> str:
        print(f'<message>\n{message}\n</message>')
        strs = message.split(" ")
        print(f'method = {strs[0]}')
        print(f'uri = {strs[1]}')
        return "200 : Server accepted !!"
