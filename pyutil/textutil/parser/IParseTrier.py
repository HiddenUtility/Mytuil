from abc import ABC, abstractmethod


class IParseTrier(ABC):
    """ほかの型への変換をトライする"""
    @abstractmethod
    def value(self):...