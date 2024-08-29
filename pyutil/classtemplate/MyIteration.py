


class MyIteration:
    """ひな形"""
    __objs : list[object]
    def __init__(self, objs: list[object]) -> None:
        self.__objs = objs
        self.__max = len(objs)
        self.__current = 0

    def __iter__(self):
        return self

    def __next__(self) -> object:
        if self.__current == self.__max:
            raise StopIteration()
        i = self.__current
        self.__current += 1
        return self.__objs[i]
    

