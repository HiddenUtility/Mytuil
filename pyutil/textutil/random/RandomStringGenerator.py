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
    NO_PUNCTUATION_CHARACTERS = string.digits + string.ascii_letters

    def __init__(self) -> None:
        pass


    @classmethod
    def to_str(cls, length=64, no_punctuation = False):
        """英数字記号からランダムで文字列を生成する


        Args:
            length (int, optional): 生成する長さ. Defaults to 64.
            no_punctuation (bool, optional): 記号はやめてくれ. Defaults to False.

        Returns:
            _type_: _description_
        """
        chars = cls.NO_PUNCTUATION_CHARACTERS if no_punctuation else cls.CHARACTERS
        return ''.join(random.choice(chars) for _ in range(length))
    
    def create_strs(self, num = 10,length=64, no_punctuation = False) -> tuple[str]:
        """複数同時に作る

        Args:
            num (int, optional): 作る数. Defaults to 10.
            length (int, optional): 生成する長さ. Defaults to 64.
            no_punctuation (bool, optional): 記号はやめてくれ. Defaults to False.

        Returns:
            tuple[str]: _description_
        """

        return tuple([self.to_str(length=length, no_punctuation = no_punctuation) for _ in range(num)])
