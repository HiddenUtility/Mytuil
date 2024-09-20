
from abc import ABC, abstractmethod


class IHashCheacker(ABC):
    @abstractmethod
    def is_same(self):
        raise NotImplementedError
