# -*- coding: utf-8 -*-
from random import shuffle

class AdvanceListSpliter:
    """リストを分ける"""
    def __init__(self, list_: list[any] = []):
        self.__list = list_

    def to_equal_list(self, n: int, randum = True) -> list[list[any]]:
        """リストを等分する

        Args:
            n (int): 何等分にするか
            randum (bool, optional): 要素はランダムにするか. Defaults to True.

        Raises:
            TypeError: _description_
            ValueError: _description_
            ValueError: _description_

        Returns:
            list[list[any]]: _description_
        """
        if not isinstance(n, int): raise TypeError()
        length = len(self.__list)
        if n < 0: raise ValueError()
        if n > length: raise ValueError(f'配列の要素 {length} は n = {n}より多くしなければなりません。')
        list2 = [list() for _ in range(n)]
        samples = self.__list.copy()
        if randum:
            shuffle(samples)
        while True:
            if len(samples) == 0: break
            for i in range(n):
                list2[i].append(samples.pop(0))
                if len(samples) == 0: break
        return list2
            


def _main():
    list_ = list(range(100))
    sl = AdvanceListSpliter(list_)
    list2 = sl.to_equal_list(4)
    [
        print(l) for l in list2
    ]

    list_ = list(range(100))
    sl = AdvanceListSpliter(list_)
    list2 = sl.to_equal_list(4, False)
    [
        print(l) for l in list2
    ]
   

if __name__ == '__main__':
    _main()




        