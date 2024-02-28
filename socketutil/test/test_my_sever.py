from socketutil.myserver.my_scoket_server import MySocketServer


class TestMyServer:
    def __init__(self) -> None:
        pass
    def run(self):
        server = MySocketServer()
        server.run()
