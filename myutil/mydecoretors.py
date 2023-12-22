# -*- coding: utf-8 -*-
import time
from datetime import datetime

def timelogr(func):
    def wrapper(*args, **kwargs):
        print(datetime.now())
        print("_______________________<start>___________________________")
        startTime = time.time()
        v = func(*args, **kwargs)
        endTime = time.time()
        print(datetime.now())
        print("_______________________< end >___________________________")
        print("{}の処理時間は{:5f}sでした。".format(func.__name__, endTime-startTime))
        return v
    return wrapper


if __name__ == "__main__":
    
    @timelogr
    def wite():
        time.sleep(1)
    wite()
        
    