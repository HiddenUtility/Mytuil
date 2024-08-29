from time import sleep
from datetime import datetime, timedelta


class LoopTimer:
    """タイマー詰め合わせ"""
    __target_time: datetime

    def __init__(self,
                hour:int = 4,
                minute:int = 0,
                second:int = 0,
                ):
        """決まった時間を保持

        Args:
            hour (int, optional): 時. Defaults to 4.
            minute (int, optional): 分. Defaults to 0.
            second (int, optional): 秒. Defaults to 0.
        """
        self.__target_time = self.__get_next_hour(hour=hour,minute=minute,second=second)


    def __get_next_hour(self, hour:int = 4, minute:int = 0, second:int = 0):
        """次の時間を得る

        Args:
            hour (int, optional): _description_. Defaults to 4.
            minute (int, optional): _description_. Defaults to 0.
            second (int, optional): _description_. Defaults to 0.

        Returns:
            _type_: _description_
        """
        current_time = datetime.now()
        target_time = current_time.replace(hour=hour, minute=minute, second=second)
        if target_time > current_time:
            return target_time
        target_time += timedelta(days=1)
        return target_time
    
    def is_target(self) -> bool:
        """決まった時間

        Returns:
            bool: _description_
        """
        return datetime.now() > self.__target_time

    def __remaining_time(self):
        """残り時間を計算する"""
        remaining_time =  self.__target_time - datetime.now()
        if remaining_time.total_seconds() <= 0:
            return "目標の日時は既に過ぎています。"
        else:
            hours = int(remaining_time.total_seconds() // 3600)
            minutes = int((remaining_time.total_seconds() % 3600) // 60)
            seconds = int(remaining_time.total_seconds() % 60)
            return "残り時間: {}時間 {}分 {}秒".format(hours, minutes, seconds)
        

    def wait(self, stop_flag: bool = False):
        """目標時間まで待つ"""
        label = self.__target_time.strftime(r'%Y年%m月%d日 %A %H時%M分%S秒')
        while True:
            if stop_flag: break
            sleep(1)
            print(f"\r{label}まで待ちます.{self.__remaining_time()}", end="")

            if self.__target_time < datetime.now():
                break


