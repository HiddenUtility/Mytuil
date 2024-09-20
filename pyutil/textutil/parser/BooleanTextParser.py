from typing import Self


class BooleanTextParser:
    __value : bool

    def __init__(self, value: str) -> None:
        """文字列'true' か 'false'をboolに変換する

        Args:
            value (str): _description_

        Raises:
            ValueError: 変換失敗
        """
        if not isinstance(value, str):
            raise TypeError(f'valueは{type(value)}です。strオブジェクトではありません。')

        self.__value = self.parse_bool(value)


    @property
    def value(self) -> bool:
        return self.__value

    def __bool__(self) -> bool:
        return self.value

    def __str__(self) -> str:
        return str(self.__value)

    def __hash__(self) -> int:
        return hash(self.__value)

    def __eq__(self, value: Self) -> bool:
        if not isinstance(value, BooleanTextParser):
            raise TypeError(f'valueは{type(value)}です。StringParseFloatTrierオブジェクトではありません。')
        return self.value == value.value

    def __ne__(self, value: object) -> bool:
        return not self.__eq__(value)

    @staticmethod
    def parse_bool(value: str) -> bool:
        value = value.lower()
        if value == 'true':
            return True
        elif value == 'false':
            return False
        else:
            raise ValueError(f"Invalid input: '{value}'. Must be 'true' or 'false'.")