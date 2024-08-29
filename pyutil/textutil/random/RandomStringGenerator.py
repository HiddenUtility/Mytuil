import random
import string


class RandomStringGenerator:
    """ランダムで文字列を生成する
    - ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    - ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    - digits = '0123456789'
    - punctuation = 記号

    """

    CHARACTERS = string.digits + string.ascii_letters + string.punctuation

    def __init__(self) -> None:
        pass


    @classmethod
    def to_str(cls, length=64):
        """英数字記号からランダムで文字列を生成する

        Args:
            length (int, optional): 文字数. Defaults to 64.

        Returns:
            _type_: _description_
        """
        
        return ''.join(random.choice(cls.CHARACTERS) for _ in range(length))
    
