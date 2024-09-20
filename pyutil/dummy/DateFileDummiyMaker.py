import random
from datetime import datetime, timedelta
from pathlib import Path
from typing import overload

from pyutil.pathuil.directory_creator import DirectoryCreator
from pyutil.textutil.random.RandomStringGenerator import RandomStringGenerator

class RandomDummyMaker:
    """適当にダミー作る
    - 作った記憶を持っているので，後で確認できる
    
    """
    __dest : Path
    __made_memory : set[Path]
    def __init__(self,target: Path = Path('../dest/test.pyutil/RandomDummyMaker')):
        self.__dest = target
        DirectoryCreator(self.__dest)
        self.__made_memory = set()

    @overload
    def create_file(self, name : str, size = 100):
        """_summary_

        Args:
            name (str): _description_
            size (int, optional): _description_. Defaults to 100.
        """
    @overload
    def create_file(self, filepath : Path, size = 100):
        """_summary_

        Args:
            filepath (Path): _description_
            size (int, optional): _description_. Defaults to 100.
        """
        
    def create_file(self, filepath : str | Path, size = 100):
        if isinstance(filepath, str):
            filepath = self.__dest / filepath
        self.__create_file(size, filepath)

    def __create_file(self, size:int, filepath: Path):
        chars = RandomStringGenerator.to_str(size)
        with open(filepath, "wb") as f:
            if size > 0:
                f.write(chars.encode())
        self.__made_memory.add(filepath)



    def create_ramdom_files(self, dirpath : Path = None, num : int = 10, size = 100):
        """_summary_

        Args:
            dirpath (Path, optional): 出力先指定したければ変更可能. Defaults to None.
            num (int, optional): 何個作るか. Defaults to 10.
            size (int, optional): ファイルサイズ. Defaults to 100.
        """

        target = dirpath if dirpath is not None else self.__dest
        names = RandomStringGenerator().create_strs(num=num, length=64,no_punctuation=True)
        for name in names:
            fs = target / f'{name}.txt'
            self.create_file(fs,size=size)

   

    def ramdom_create(self, num : int = 10):
        """適当にフォルダとファイルを作る

        Args:
            num (int, optional): _description_. Defaults to 10.
        """
        dirnames = RandomStringGenerator().create_strs(num=num,length=10,no_punctuation=True)

        for name in dirnames:
            dirpath = self.__dest / name
            DirectoryCreator(dirpath)
            self.create_ramdom_files(dirpath=dirpath,num=num)

    def get_created_filepaths(self) -> tuple[Path]:
        """作ったダミーのファイルパス達を出す

        Returns:
            tuple[Path]: _description_
        """

        return tuple(self.__made_memory)





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

        