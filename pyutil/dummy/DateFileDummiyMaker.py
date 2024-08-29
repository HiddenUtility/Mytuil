import random
from datetime import datetime, timedelta
from pathlib import Path

from pyutil.textutil.random.RandomStringGenerator import RandomStringGenerator


class DummyDatetimeLabelFileMaker:
    """ターゲットディレクトリの中にyyyymmddHHMMSSのダミーファイルを作成する"""
    __dest : Path
    __num : int
    __size : int
    __header : str
    __footer : str
    __suffix : str
    __timestamps : tuple[datetime, datetime]

    def __init__(self,target: Path, 
                 days=60, 
                 file_num=100, 
                 file_size=1000,
                 suffix = '.csv',
                 header = '',
                 footer = '',
                 ):
        """ターゲットディレクトリの中にyyyymmddHHMMSSのダミーファイルを作成する

        Args:
            dest (Path): 出力先
            days (int, optional): 何日前までのデータか. Defaults to 60.
            file_num (int, optional): 何個つくるか. Defaults to 100.
            file_size (int, optional): ダミーのファイルのバイトサイズ. Defaults to 1000.
            suffix (str, optional): 拡張子. Defaults to '.csv'.
            header (str, optional): ファイルの先頭につける. Defaults to ''.
            header (str, optional): ファイルの先頭につける. Defaults to ''.

        """

        self.__dest = target
        self.__num = file_num
        self.__size = file_size
        self.__header = header
        self.__footer = footer
        self.__suffix = suffix
  
        end = datetime.now()
        start = end - timedelta(days=days)
        self.__timestamps = (
            start.timestamp(),
            end.timestamp(),
        )


    def __create_dummy_file(self, filepath : Path):

        chars = RandomStringGenerator.to_str(self.__size)
        with open(filepath, "wb") as f:
            if self.__size > 0:
                f.write(chars.encode())

    def __create_filenames(self):
        return [
            f'{self.__header}{self.__get_random_datetime()}{self.__footer}{self.__suffix}'
            for _ in range(self.__num)
        ]

    def __create_dummy_files(self, dest : Path):
        filenames = self.__create_filenames()
        for name in filenames:
            self.__create_dummy_file(dest.joinpath(name))

    def __get_random_datetime(self) -> str:
        random_timestamp = random.uniform(*self.__timestamps)
        return datetime.fromtimestamp(random_timestamp).strftime(r"%Y%m%d%H%M%S")


    def run(self):
        """実行"""
        print(f"{self.__dest}にダミー作成中")
        self.__create_dummy_files(self.__dest)

        