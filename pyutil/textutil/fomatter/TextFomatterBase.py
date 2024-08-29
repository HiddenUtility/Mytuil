


import string
import unicodedata


class TextFomatterBase():
    """stringを指定のルールに従って変換する

    - ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    - ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    - digits = '0123456789'
    - punctuation = 記号

    """
    CHARACTERS = string.digits + string.ascii_letters + string.punctuation
    """全文字"""
    DIGITS : str = string.digits
    """10進数"""
    ASCII_LOWERCASE : str = string.ascii_lowercase
    """小文字のアルファベット"""
    ASCII_UPPERCASE : str = string.ascii_uppercase
    """大文字のアルファベット"""
    ASCII_LETTERS : str = string.ascii_letters
    """大文字小文字のアルファベット"""
    PUNCTUATION : str = string.punctuation
    """記号"""

    _text : str


    @staticmethod
    def normalize(text: str) -> str:
        """全角を半角に変化する"""
        normalized_text = unicodedata.normalize('NFKC', text)
        return normalized_text

    def __init__(self, text: str) -> None:
        """文字列を変換する
        - 変換の結果空文字になるかしれないので必要ならemptyプロパティで確認してね。
        Args:
            text (str): 変換したい文字
        """
        self._text = self.normalize(text)


    
    