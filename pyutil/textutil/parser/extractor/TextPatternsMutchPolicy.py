import re


class TextPatternsMutchPolicy:
    """テキストがパターン達に一致するか調べる"""
    __patterns : set[str]
    __text : str
    def __init__(self, patterns : set[str] | str, text : str) -> None:
        """テキストがパターン達に一致するか調べる

        Args:
            patterns (set[str] | str): 調査するパターンたち
            text (str): 調査するテキスト
        """

        if isinstance(patterns, str):
            patterns = [patterns]
        self.__patterns = set(patterns)
        self.__text = text

    def is_ok(self) -> bool:
        """パターンのどれかに一致した

        Returns:
            bool: パターンのどれかに一致
        """
        for pattern in self.__patterns:
            if re.search(pattern, self.__text):
                return True
        return False


    def is_all_ok(self) -> bool:
        """パターンのどれかに一致した

        Returns:
            bool: すべてに一致
        """
        for pattern in self.__patterns:
            if not re.search(pattern, self.__text):
                return False
        return True