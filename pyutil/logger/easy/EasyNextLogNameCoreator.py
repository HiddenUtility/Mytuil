from pyutil.textutil import TextNaturalNumberExtractor


from pathlib import Path


class EasyNextLogNameCoreator:
    """次のログの名前を付ける
    ないなら[1]になる
    """
    def __init__(self, now_name: str) -> None:
        now_num = self.__extract_num(now_name)
        next_num = now_num + 1
        old_name = now_name.replace(f' [{now_num}]', '')
        self.__next_name = f'{old_name} [{next_num}].log'

    def __extract_num(self, string) -> int:
        return TextNaturalNumberExtractor(string).square

    @property
    def name(self) -> Path:
        """拡張子つき"""
        return self.__next_name