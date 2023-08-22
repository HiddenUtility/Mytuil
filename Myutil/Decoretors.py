# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 16:42:12 2023

@author: nanik
"""
import time
from datetime import datetime

def timelogr(func):
    def wrapper(*args, **kwargs):
        print(datetime.now())
        print("_______________________<start>___________________________")
        startTime = time.time()
        func(*args, **kwargs)
        endTime = time.time()
        print(datetime.now())
        print("_______________________< end >___________________________")
        print("{}の処理時間は{:5f}sでした。".format(func.__name__,endTime-startTime))
    return wrapper


if __name__ == "__main__":
    
    @timelogr
    def wite():
        time.sleep(1)
    wite()
        
    

 