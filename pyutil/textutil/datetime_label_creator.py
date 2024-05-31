from datetime import datetime, timedelta


class DatetimeLabelCreator:
    """現在の時刻に基づいてyyyymmdd hh:mm:ssのラベルを作成する。"""
    DATETIME_FORMAT = r"%Y-%m-%d %H:%M:%S"
    def __init__(self) -> None:
        pass
    
    def get_now_label(self) -> str:
        """今の時間ラベルを得る"""
        return datetime.now().strftime(self.DATETIME_FORMAT)

    def get_past_time_label(self,hours=1, minutes=0):
        """撒き戻ったラベルを得る。"""
        rewind = datetime.now() - timedelta(hours=hours, minutes=minutes)
        return rewind.strftime(self.DATETIME_FORMAT)
