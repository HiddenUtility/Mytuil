from abc import ABC, abstractmethod
from datetime import datetime


class IDatetimeLabelCreator(ABC):
    """パターンからDatetimeラベルを作成する。"""

    @abstractmethod
    def get_label(self, datetime_ : datetime)-> str:
        """datetimeをラベル(str)へ変換する"""

    @abstractmethod
    def get_now_label(self) -> str:
        """今の時間ラベルを得る"""

    @abstractmethod
    def get_past_time_label(self,hours=1, minutes=0):
        """現時刻からまき戻ったラベルを得る。"""
        
    @abstractmethod
    def load_str(self, value: str) -> datetime:
        """strからdatetimeを得る"""
