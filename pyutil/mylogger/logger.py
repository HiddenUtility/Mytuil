from abc import ABC, abstractmethod

####//Interface
class Logger(ABC):
    @abstractmethod
    def write(self, other: object, debug=False, out=False) -> None:
        raise NotImplementedError()
    @abstractmethod
    def out(self) -> None:
        raise NotImplementedError()