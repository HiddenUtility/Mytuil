

from pathlib import Path
from shutil import copy

from pyutil.pathuil import DirecotryCreator
from pyutil.textutil import TextPatternsMutchPolicy


class TargetDirectoryOnlyCopier:
    """再回帰で指定したディレクトリにソースディレクトリ内の指定ディレクトリをコピーする。
        すでにdestがいた場合は削除しないためclearオプションを使用のこと
        指定したディレクトリ名やファイル名しかコピーしない。
    """
    __src : Path
    __dest : Path
    __target_dirnames : set[str]
    __is_clear : bool
    __root_files : bool
    def __init__(self,
                 src : str|Path,
                 dest : str|Path,
                 target_dirname_patterns: set[str] = set(),
                 clear = True,
                 root_files = False,
                 ) -> None:
        """再回帰で指定したディレクトリにソースディレクトリ内の指定ディレクトリをコピーする。
        すでにdestがいた場合は削除するためclearオプションを無効のこと
        コピーしたいディレクトリ名やファイル名を指定できる。
        指定しない場合はすべて対象になる。

        Args:
            src (str | Path): コピーするディレクトリ
            dest (str | Path): 出力するディレクトリ(destの中にsrcができる)
            target_dirname_patterns (_type_, optional): コピーしたいディレクトリ名。パターン可. Defaults to set().
            clear (bool, optional): すでにdestがいた場合は削除する。. Defaults to True.
            root_files (bool, optional): srcのないのファイルもコピーしたい. Defaults to False.
        """

        self.__src = Path(src)
        if not self.__src.is_dir():
            raise NotADirectoryError(f'{src}というディレクトリは存在しません。')
        self.__dest = Path(dest)
        self.__target_dirnames = set(target_dirname_patterns)
        self.__is_clear = clear
        self.__root_files = root_files


    def __root_copy(self, target:Path, dest:Path):
        ds = [p for p in target.glob('*') if p.is_dir()]
        fs = [p for p in target.glob('*') if p.is_file()]

        for f in fs:
            if not self.__root_files:
                break
            copy(f, dest / f.name)

        for d in ds:
            if TextPatternsMutchPolicy(self.__target_dirnames, d.name).is_ok():
                new_dest = dest / d.name
                DirecotryCreator(new_dest,clear=self.__is_clear)
                self.__sub_copy(d, new_dest)

    def __sub_copy(self, target:Path, dest:Path):
        fs = [p for p in target.glob('*') if p.is_file()]
        ds = [p for p in target.glob('*') if p.is_dir()]

        for f in fs:
            copy(f, dest / f.name)

        for d in ds:
            new_dest = dest / d.name
            DirecotryCreator(new_dest,clear=self.__is_clear)
            self.__sub_copy(d, new_dest)


    def run(self):
        self.__root_copy(self.__src, self.__dest)
