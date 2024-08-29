import os
from datetime import datetime
from pathlib import Path


class FileTimestampUpdater:
    """ファイルの更新日を変更する"""
    __path: Path
    __datetime : datetime
    __missing_ok : bool
    def __init__(self, target_path: Path | str,
                 datetime_ : datetime,
                 missing_ok : bool = True,
                 ):
        """ファイルの更新日を変更する

        Args:
            target_path (Path): 変更したいファイル
            datetime_ (datetime): _description_
            missing_ok (bool, optional): _description_. Defaults to True.
        """
        target_path = Path(target_path)
        if not target_path.is_file():
            raise ValueError()
        self.__path = target_path
        self.__datetime = datetime_
        self.__missing_ok = missing_ok


    def update(self) -> None:
        try:
            os.utime(self.__path, (self.__datetime.timestamp(), self.__datetime.timestamp()))
        except Exception as e:
            if self.__missing_ok:
                return
            raise e