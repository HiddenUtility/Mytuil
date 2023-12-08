from abc import ABCMeta, abstractmethod

class HashChecker(metaclass=ABCMeta):
    @abstractmethod
    def is_same(self):
        raise NotImplementedError