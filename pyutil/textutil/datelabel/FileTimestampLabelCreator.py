from datetime import datetime
from pyutil.textutil.datelabel.DatetimeLabelCreator import DatetimeLabelCreator



class FileNameTimestampLabelCreator(DatetimeLabelCreator):
    """File名でよく使うyyyymmddhhmmssのDatetimeラベルを作成する。
    読み込みもできるよ
    """
    PATTERN = r"%Y%m%d%H%M%S"
    def __init__(self) -> None:
        """ファイルでよく使うDatetimeラベルを作成する。
        yyyymmddhhmmssを生成
        Args:
            pattern (str, optional): パターンを設定. Defaults to "Y%m%d%H%M%S"
        """
        super().__init__(self.PATTERN)

        

