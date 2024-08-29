from __future__ import annotations


from pyutil.textutil.parser.IParseTrier import IParseTrier


class StringParseFloatTrier(IParseTrier):
    """文字からDubleの型へのいったん変換する
    0と0.0を同じと判断したい
    TrueとTRUEは同じと扱う
    
    """
    __value : str | float
    
    def __init__(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError(f'valueは{type(value)}です。strオブジェクトではありません。')
        
        self.__value = value
        try:
            self.__value = float(value)
        except Exception:
            pass

    @property
    def value(self) -> str:
        return str(self.__value)
    
    def __str__(self) -> str:
        return str(self.__value)
    
    def __hash__(self) -> int:
        return hash(self.__value)

    def __eq__(self, value: StringParseFloatTrier) -> bool:
        if not isinstance(value, StringParseFloatTrier):
            raise TypeError(f'valueは{type(value)}です。StringParseFloatTrierオブジェクトではありません。')
        return self.value.lower() == value.value.lower()
    
    def __ne__(self, value: object) -> bool:
        return not self.__eq__(value)
    
