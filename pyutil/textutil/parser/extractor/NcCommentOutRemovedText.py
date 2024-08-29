import re


class NcCommentOutRemovedText:
    """文字列から()が追加部分を削除する。"""
    __origin : str
    def __init__(self, text: str) -> None:
        self.__origin = text
        self.__value = text
        for target in re.findall(r"\(.+\)", text):
            self.__value = self.__remove(self.__value, target)

    def __remove(self, text: str, removed: str) -> str:
        return text.replace(removed, '')

    @property
    def value(self) -> str:
        return self.__value

    @property
    def origin(self) -> str:
        return self.__origin