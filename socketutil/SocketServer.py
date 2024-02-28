from abc import ABC, abstractmethod


class SocketServer(ABC):
    @abstractmethod
    def run(self):...