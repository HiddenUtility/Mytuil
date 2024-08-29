from pyutil.textutil.fomatter.ITextFomatter import ITextFomatter
from pyutil.textutil.fomatter.TextFomatterBase import TextFomatterBase


class OnlyLowerAciiAndDigitsTextFormatter(ITextFomatter,TextFomatterBase):
    """- 半角英語の小文字と数字のみにする
    - 変換の結果空文字になるかしれないので必要ならemptyプロパティで確認してね。
    """
    __value : str
    def __init__(self, text: str) -> None:
        """半角英語の小文字と数字のみにする
        - 変換の結果空文字になるかしれない.
        - emptyプロパティで空か確認できる.
        Args:
            text (str): 変換したい文字
        """
        
        super().__init__(text.lower())
        self.__value = ''.join(
            [character for character in self._text if self.__is_ok(character)]
        )

    def __is_ok(self, char : str) -> bool:
        if char in self.ASCII_LOWERCASE:return True
        if char in self.DIGITS:return True
        return False

    @property
    def empty(self) -> bool:
        """空文字かどうか

        Returns:
            bool: 空文字
        """
        return '' == self.__value


    @property
    def value(self) -> str:
        """変換結果

        Returns:
            str: 半角英語の小文字と数字のみ
        """
        return self.__value
    
