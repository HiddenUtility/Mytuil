from abc import ABCMeta, abstractmethod

class HashCheacker(metaclass=ABCMeta):
    @abstractmethod
    def is_same(self):
        raise NotImplementedError