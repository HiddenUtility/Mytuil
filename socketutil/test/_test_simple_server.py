from socketutil.simpleserver.socket_server_base import SocketServerBase
import socket


class TestSinpleServer(SocketServerBase):
    def __init__(self, host:str="0.0.0.0", port:int=8080) -> None:
        self.server=(host,port,)
        super().__init__(timeout=1, buffer=1024)

    # @override
    def _respond(self, message:str) -> str:
        print(f'<message>\n{message}\n</message>')
        strs = message.split(" ")
        print(f'method = {strs[0]}')
        print(f'uri = {strs[1]}')
        return "200 : Server accepted !!"
    
    def run(self):
        while True:
            self._accept(self.server, socket.AF_INET, socket.SOCK_STREAM, 0)
