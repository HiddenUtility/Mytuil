# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 08:53:13 2023

@author: nanik
"""



from __future__ import annotations
import abc
from pathlib import Path
import pickle
import hashlib
from datetime import datetime, timedelta
from enum import Enum, auto
import time


#interface
class InterfaceTimer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def wate_hour(self):
        raise NotImplementedError()
    @abc.abstractmethod
    def stop(self):
        raise NotImplementedError()

class Weekday(Enum):
    MON = auto()
    TUE = auto()
    WED = auto()
    THU = auto()
    FRI = auto()
    SAT = auto()
    SUN = auto()

class Timer(InterfaceTimer):
    def __init__(self):
        pass
    
    @staticmethod
    def _get_week_name(week_num: int):
        if not isinstance(week_num, int): TypeError
        return Weekday(week_num).name
    
    @staticmethod
    def _get_next_hour(hour:int = 4, minute:int = 0, second:int = 0):
        current_time = datetime.now()
        next_ = current_time.replace(hour=hour, minute=minute, second=second, microsecond=0)
        if current_time >= next_:
            next_ += timedelta(days=1)
        return next_
    @staticmethod
    def _get_next_week(weekday:int, hour:int = 4, minute:int = 0, second:int = 0):
        current_time = datetime.now()
        current_weekday = current_time.weekday()
        days_to_next_monday = (7 - current_weekday + 0) % 7
        next_ = current_time.replace(hour=hour, minute=minute, second=second, microsecond=0) + timedelta(days=days_to_next_monday)
        if current_time >= next_:
            next_ += timedelta(days=7)
        return next_
    
    @staticmethod
    def _remaining_time(target_time: datetime):
        remaining_time = target_time - datetime.now()
        if remaining_time.total_seconds() <= 0:
            return "目標の日時は既に過ぎています。"
        else:
            hours = int(remaining_time.total_seconds() // 3600)
            minutes = int((remaining_time.total_seconds() % 3600) // 60)
            seconds = int(remaining_time.total_seconds() % 60)
            return "残り時間: {}時間 {}分 {}秒".format(hours, minutes, seconds)
            
    def wate_datetime(self, target_time: datetime):
        if not isinstance(target_time, datetime): TypeError
        while True:
            if datetime.now() >= target_time: break
            label = target_time.strftime('%Y年%m月%d日 %A %H時%M分%S秒')
            print(f"\r{label}まで待ちます.{self._remaining_time(target_time)}", end="")
            time.sleep(1)
        print("\n Start!!")
        
    def wate_hour(self,weekday:int = None, hour:int = 4, minute:int = 0, second:int = 0):
        if weekday is None:
            target_time = self._get_next_hour(hour=hour,minute=minute,second=second)
            self.wate_datetime(target_time)
        else:
            target_time = self._get_next_week(weekday,hour=hour,minute=minute,second=second)
            self.wate_datetime(target_time)
        
    def stop(self, secondes: int):
        if not isinstance(secondes, int): TypeError
        for i in range(secondes):
            t = "{0:8}".format(secondes - i)
            print(f"\r 一時停止中 残り{t}秒", end="")
            time.sleep(1)
        print()
        
    

if __name__ == "__main__":
    
    timer = Timer()
    
    timer.stop(5) #5秒ストップ
    #timer.wate_hour(hour=4,minute=30) #次の４時半まで待機
    timer.wate_hour(weekday=1,hour=4,minute=30) #次の火曜日の４時半まで待機
    


 