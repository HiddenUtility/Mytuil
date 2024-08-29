####//Interface
from abc import ABC, abstractmethod


class ILogger(ABC):
    @abstractmethod
    def write(self, other: object, debug=False, out=False) -> None:
        raise NotImplementedError()
    @abstractmethod
    def out(self) -> None:
        raise NotImplementedError()