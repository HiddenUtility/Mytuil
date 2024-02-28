from abc import ABC, abstractmethod


class SocketClient(ABC):
    @abstractmethod
    def post_test(self,data: dict):...
        
    @abstractmethod
    def post(self,data: dict):...
        