from abc import ABC, abstractmethod


class IZipCompressor(ABC):
    @abstractmethod
    def to_zip(self):
        """圧縮を開始する"""