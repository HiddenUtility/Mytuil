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
        """パターンに一致した
        - 前方一致

        Returns:
            bool: パターンのどれかに一致
        """
        for pattern in self.__patterns:
            try:
                if re.match(pattern, self.__text) is not None:
                    return True
            except Exception as e:
                e.add_note(pattern)
                raise e
        return False
    
    def is_parts_ok(self) -> bool:
        """パターンに部分一致した
        - サーチ

        Returns:
            bool: パターンに部分一致した
        """
        for pattern in self.__patterns:
            try:
                if re.search(pattern, self.__text) is not None:
                    return True
            except Exception as e:
                e.add_note(pattern)
                raise e
        return False


    def is_all_ok(self) -> bool:
        """パターンすべてに一致した

        Returns:
            bool: すべてに一致
        """
        for pattern in self.__patterns:
            if not re.search(pattern, self.__text):
                return False
        return True