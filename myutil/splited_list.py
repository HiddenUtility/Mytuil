# -*- coding: utf-8 -*-
import random

class SplitedList:
    def __init__(self, list_: list[any] = []):
        self.__list = list_

    def random_split(self, n: int):
        if not isinstance(n, int): raise TypeError()
        length = len(self.__list)
        if n < 0: raise ValueError()
        if n > length: raise ValueError()
        list2 = [list() for _ in range(n)]
        samples = random.sample(self.__list, length)
        while True:
            if len(samples) == 0: break
            for i in range(n):
                list2[i].append(samples.pop(0))
                if len(samples) == 0: break
        return list2
            
        
if __name__ == "__main__":
    list_ = list(range(100))
    sl = SplitedList(list_)
    list2 = sl.random_split(4)
    
        