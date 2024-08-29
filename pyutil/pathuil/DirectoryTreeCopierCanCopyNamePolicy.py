from pyutil.textutil import TextPatternsMutchPolicy


class DirectoryTreeCopierCanCopyNameIgnoredPolicy:
    """Ignoreのパターンに一致しないかどうか調べる"""
    __ignore_patterns : set[str]
    __text : str
    def __init__(self, ignore_pattern : set[str] | str, text : str) -> None:
        """Ignoreのパターンに一致しないかどうか調べる

        Args:
            ignore_pattern (set[str] | str): 無視する
            text (str): _description_
        """
        if isinstance(ignore_pattern, str):
            ignore_pattern = [ignore_pattern]
        self.__ignore_patterns = set(ignore_pattern)
        self.__text = text

    def is_ok(self) -> bool:
        """無視パターンに一致したらアウト

        Returns:
            bool: 無視パターンに一致しない
        """
        return not TextPatternsMutchPolicy(self.__ignore_patterns, self.__text).is_ok()