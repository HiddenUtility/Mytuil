from pyutil.myerror import ConvertError
from pyutil.textutil.datelabel.IDatetimeLabelCreator import IDatetimeLabelCreator


from datetime import datetime, timedelta
from typing import override


class DatetimeLabelCreator(IDatetimeLabelCreator):
    """パターンからDatetimeラベルを作成する。"""
    _string_format : str

    def __init__(self, pattern:str) -> None:
        """パターンからDatetimeラベルを作成する。
        Args:
            pattern (str, optional): パターンを設定. '%Y-%m-%d %H:%M:%S'.
        """
        self._string_format = pattern

    @override
    def get_label(self, datetime_ : datetime)-> str:
        if not hasattr(self, '_string_format'):
            raise NotImplementedError()
        return datetime_.strftime(self._string_format)

    @override
    def get_now_label(self) -> str:
        """今の時間ラベルを得る"""
        if not hasattr(self, '_string_format'):
            raise NotImplementedError()
        return datetime.now().strftime(self._string_format)

    @override
    def get_past_time_label(self, days=0, hours=1, minutes=0):
        """まき戻ったラベルを得る。"""
        if not hasattr(self, '_string_format'):
            raise NotImplementedError()
        rewind = datetime.now() - timedelta(days=days, hours=hours, minutes=minutes)
        return rewind.strftime(self._string_format)

    @override
    def load_str(self, value: str) -> datetime:
        """strからdatetimeを得る"""
        try:
            return  datetime.strptime(value, self._string_format)
        except Exception as e:
            raise ConvertError(e)
        

