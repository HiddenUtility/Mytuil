from datetime import datetime, timedelta


from pyutil.textutil.datelabel.DatetimeLabelCreator import DatetimeLabelCreator


class DateStampLabelCreator(DatetimeLabelCreator):
    """yyyy-mm-dd-aaラベルを作成する。"""
    PATTERN = r"%Y-%m-%d-%a"
    def __init__(self) -> None:
        """ファイルでよく使うDatetimeラベルを作成する。
        yyyymmddhhmmssを生成
        Args:
            pattern (str, optional): パターンを設定. Defaults to "Y%m%d%H%M%S"
        """
        super().__init__(self.PATTERN)


    def get_label_from_reference_time(self, datetime_: datetime, reference_houre = 5)-> str:
        """_summary_

        Args:
            datetime_ (datetime): _description_
            previous (int, optional): ある時間. Defaults to 5.

        Returns:
            str: ある時間を基準にそれ以前なら前日して扱う
        """

        if datetime_.hour < reference_houre: ##5時までは昨日の２直とする。
            previous_day = datetime_ - timedelta(days=1)
            return previous_day.strftime(self._string_format)
        else:
            return datetime_.strftime(self._string_format)
        
