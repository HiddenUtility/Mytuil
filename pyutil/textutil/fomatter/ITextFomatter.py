from abc import ABC, abstractmethod


class ITextFomatter(ABC):

    @abstractmethod
    def empty(self) -> bool:
        """空文字かどうか

        Returns:
            bool: 空文字
        """

    @abstractmethod
    def value(self) -> str:
        """変換結果

        Returns:
            str: 文字列
        """
       