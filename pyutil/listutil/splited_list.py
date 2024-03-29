# -*- coding: utf-8 -*-
from random import shuffle

class SplitedList:
    def __init__(self, list_: list[any] = []):
        self.__list = list_

    def split(self, n: int, randum = True) -> list[list[any]]:
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
    sl = SplitedList(list_)
    list2 = sl.split(4)
    [
        print(l) for l in list2
    ]

    list_ = list(range(100))
    sl = SplitedList(list_)
    list2 = sl.split(4, False)
    [
        print(l) for l in list2
    ]
   

if __name__ == '__main__':
    _main()




        