# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 23:12:13 2023

@author: nanik
"""

from threading import Thread
from time import sleep
from random import choice

class Main:
    
    def __init__(self):
        
        self.__logger = {}
        self.__thred = {}
        
    def process(self, index: any):
        print(index, "start")
        self.__thred[index] = 1
        #/* 処理　ログとか
        
        sleep(choice(list(range(1,10))))
        
        #*/
        self.__thred[index] = 0
    
    def __confirm_runing(self, indexs) -> int:
        alives = 0
        for i in indexs:
            alives += self.__thred[i]
        return alives
    
    def run(self):
        indexs = list(range(100))
        for i in indexs:
            Thread(target=self.process, args=(i,)).start()
            
        while True:
            sleep(0.1)
            alives = self.__confirm_runing(indexs)
            if alives == 0: break
            print(f"\r{alives}スレッドが処理中です。　　　　",end="")
        print("\nすべてのスレッドが終了しました。")
        
        #log処理とか

            

        
if __name__ == '__main__':
    
    obj = Main()
    obj.run()