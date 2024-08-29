from datetime import datetime
from pyutil.myerror import ConvertError
from pyutil.textutil.datelabel.DatetimeLabelCreator import DatetimeLabelCreator


class DataBaseTimestampLabelCreator(DatetimeLabelCreator):
    """DBのTimestampでよく使うDatetimeラベルを作成する。"""
    PATTERN = r"%Y-%m-%d %H:%M:%S"
    def __init__(self) -> None:
        """DBのTimestampよく使うDatetimeラベルを作成する。
        yyyymmdd hh:mm:ssを生成
        Args:
            pattern (str, optional): パターンを設定. Defaults to '%Y-%m-%d %H:%M:%S'.
        """
        super().__init__(self.PATTERN)

