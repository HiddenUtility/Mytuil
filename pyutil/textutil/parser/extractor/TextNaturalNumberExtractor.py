import re


class TextNaturalNumberExtractor:
    """文字列から自然数を抜き取る
    一致しないと0を返す使用なので注意
    intにパース失敗したら普通にValueError
    用意しているパターンは下記
    - parentheses ()
    - square brackets []
    - curly brackets {}
     -angle brackets <>
    """
    def __init__(self, text : str) -> None:
        self.__test = text

    def __extract_num(self, pattern : str) -> int:
        match = re.search(pattern, self.__test)
        if match:
            try:
                num = int(match.group(1))
                return num
            except Exception:
                raise ValueError(f'{match.group(1)}抽出対象が整数にできない')
        else:
            return 0

    @property
    def parentheses(self) -> int:
        """()"""
        return self.__extract_num(r'\((\d+)\)')

    @property
    def square(self) -> int:
        """[]"""
        return self.__extract_num(r'\[(\d+)\]')

    @property
    def curly(self) -> int:
        """{}"""
        return self.__extract_num(r'\{(\d+)\}')

    @property
    def angle(self) -> int:
        """<>"""
        return self.__extract_num(r'\<(\d+)\>)')

    def get(self, pattern : str) -> int:
        return self.__extract_num(pattern)