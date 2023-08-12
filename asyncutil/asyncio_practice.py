# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 23:10:01 2023

@author: nanik
"""
import abc
import asyncio
import time

class Test:
    def __init__(self, message: str=""):
        self.message = message
        
        
    @abc.abstractmethod
    async def printf(self,str_):
        pass

    async def run(self):
        await self.printf(f"start {self.message}") 
        print(f"end {self.message}")


class TestSleep(Test):
    #@Orveride
    async def printf(self,str_):
        print(str_)
        time.sleep(3)
        
class TestAsyncSleep(Test):
    #@Orveride
    async def printf(self,str_):
        print(str_)
        await asyncio.sleep(3)
        
class TestLoop:
    
    def __init__(self):
        print("loop")
        self.level = 0
        
    async def up(self):
        while True:
            await asyncio.sleep(1)
            print("level up !!")
            self.level+=1
            if self.level == 100:break
            
    async def what_value(self):
        while True:
            await asyncio.sleep(3)
            print(f"現在のlevelは{self.level}です。")
            if self.level == 100:
                print("最高レベルに到達しました。")
                break
    
async def main():
    #//非同期関数ではないので飛ばされない
    test = TestSleep("nomal sleep")
    task = asyncio.create_task(test.run())
    #//非同期なので飛ばされるはず
    test0 = TestAsyncSleep("aysnc0")
    task0 = asyncio.create_task(test0.run())
    test1 = TestAsyncSleep("aysnc1")
    task1 = asyncio.create_task(test1.run())
    print(
        """
非同期処理ではないsleepは飛ばされないため、普通にendまでいってしまう。
しかし、非同期のasyncio.sleepは非同期のため次の処理が実装される
        """
        )
    await task
    await task0
    await task1
    print("++++++++++++++++++++++++++++++++++++++++")

async def main_gather():
    test0 = TestAsyncSleep("aysnc0")
    test1 = TestAsyncSleep("aysnc1")
    print(
        """
非同期どうしであればあたかも並列で動く。
        """
        )
    #awaitable asyncio.gather(*aws, loop=None, return_exceptions=False)
    await asyncio.gather(test0.run(),test1.run())
    print("++++++++++++++++++++++++++++++++++++++++")
    
async def main_loop():
    print(
        """
実際使うとなると、別の処理を走っていて、その時の状態を送るときなどの使える。
        """
        )
    test = TestLoop()
    await asyncio.gather(test.up(),test.what_value())
    print("++++++++++++++++++++++++++++++++++++++++")


    
if __name__ == "__main__":
    
    #非同期関数にはasync つける
    #非同期関数を呼び出すときは　awitをつける
    #非同期処理のときは次の処理が実行されるようになる。
    asyncio.run(main())
    #可変が使えるasyncio.gather使うほうがタスクをセットしやすいかも
    asyncio.run(main_gather())
    #多分一番つかう無限ループ版
    asyncio.run(main_loop())
    
    
    
    
    