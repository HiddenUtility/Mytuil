from __future__ import annotations
from datetime import datetime, timedelta
import time


class MyTimer:
    __start_time: float
    def __init__(self):
        self.__start_time = time.time()

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
        
    @classmethod  
    def wate_datetime(cls, target_time: datetime):
        if not isinstance(target_time, datetime): TypeError
        while True:
            if datetime.now() >= target_time: break
            label = target_time.strftime('%Y年%m月%d日 %A %H時%M分%S秒')
            print(f"\r{label}まで待ちます.{cls._remaining_time(target_time)}", end="")
            time.sleep(1)
        print("\r Start!!  \n")
        
    @classmethod
    def wate_hour(cls,weekday:int = None, hour:int = 4, minute:int = 0, second:int = 0):
        if weekday is None:
            target_time = cls._get_next_hour(hour=hour,minute=minute,second=second)
            cls.wate_datetime(target_time)
        else:
            target_time = cls._get_next_week(weekday,hour=hour,minute=minute,second=second)
            cls.wate_datetime(target_time)

    @staticmethod
    def stop(secondes: int, free_message="一時停止中"):
        if not isinstance(secondes, int): TypeError
        for i in range(secondes):
            t = "{0:8}".format(secondes - i)
            print(f"\r {free_message} 残り{t}秒", end="")
            time.sleep(1)
        print("\r Start!!                        \n")
    
    def stop_need_elapsed_time(self,secondes: int, free_message="速すぎるため処理を遅延中"):
        """設定時間より早く処理終わってしまった場合、処理を待機する。"""
        elapsed_time  = int(time.time() - self.__start_time)
        if elapsed_time > secondes:
            return
        self.stop(secondes - elapsed_time, free_message=free_message)


if __name__ == "__main__":
    
    timer = MyTimer()
    timer.stop(5) #5秒ストップ
    #timer.wate_hour(hour=4,minute=30) #次の４時半まで待機
    timer.stop_need_elapsed_time(20)
    
    
    
    # timer.wate_hour(weekday=1,hour=4,minute=30) #次の火曜日の４時半まで待機
    
