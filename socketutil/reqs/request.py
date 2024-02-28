from abc import ABC, abstractmethod


class Request(ABC):
    
    
    @abstractmethod
    def load_dict(self, dict_:dict):
        raise NotImplementedError()
    
    @abstractmethod
    def load_bytes(self, bytes_:bytes):
        raise NotImplementedError()
        
    @abstractmethod
    def to_dict(self) -> dict:
        raise NotImplementedError()
    
    @abstractmethod
    def to_bytes(self) -> bytes:
        raise NotImplementedError()