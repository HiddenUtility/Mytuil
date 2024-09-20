from pyutil.pathuil.DirectoryTreeCopierCanCopyNamePolicy import DirectoryTreeCopierCanCopyNameIgnoredPolicy
from pyutil.pathuil.directory_creator import DirectoryCreator


from pathlib import Path
from shutil import copy


class ToInsideDirectoryTreeCopier:
    """再回帰で指定したディレクトリにソースディレクトリの中身をコピーする。
        すでにdestがいた場合は削除しないためclearオプションを有効のこと
        無視するディレクトリ名やファイル名を指定できる。

        Args:
            src (str | Path): コピーしたい中身が入ったディレクトリ
            dest (str | Path): 出力するディレクトリ
    """
    __src : Path
    __dest : Path
    __igno_dirnames : set[str]
    __igno_filenames : set[str]
    __is_clear : bool
    def __init__(self,
                 src : str|Path,
                 dest : str|Path,
                 ignore_dirname_patterns = set(),
                 ignore_filename_patterns = set(),
                 clear = False,
                 ) -> None:
        """再回帰でディレクトリの中身をコピーする。
        すでにdestがいた場合は削除するためclearオプションを無効のこと
        無視するディレクトリ名やファイル名を指定できる。

        Args:
            src (str | Path): コピーするディレクトリ
            dest (str | Path): 出力するディレクトリ(destの中にsrcができる)
            ignore_dirname_patterns (_type_, optional): 無視するディレクトリ名。パターン可. Defaults to set().
            ignore_filename_patterns (_type_, optional): 無視するファイル名。パターン可. Defaults to set().
            clear (bool, optional): すでにdestがいた場合は削除する。. Defaults to False.

        Raises:
            NotADirectoryError: _description_
        """


        self.__src = Path(src)
        if not self.__src.is_dir():
            raise NotADirectoryError(f'{src}というディレクトリは存在しません。')
        self.__dest = Path(dest)
        self.__igno_dirnames = set(ignore_dirname_patterns)
        self.__igno_filenames = set(ignore_filename_patterns)
        self.__is_clear = clear

        self.__igno_dirnames.add(".venv")
        self.__igno_dirnames.add(".git")

    def __copy(self, target:Path, dest:Path):
        fs = [p for p in target.glob('*') if p.is_file()]
        ds = [p for p in target.glob('*') if p.is_dir()]

        DirectoryCreator(self.__dest,clear=self.__is_clear)

        for f in fs:
            if not DirectoryTreeCopierCanCopyNameIgnoredPolicy(self.__igno_filenames, f.name).is_ok():
                continue
            copy(f, dest / f.name)

        for d in ds:
            if not DirectoryTreeCopierCanCopyNameIgnoredPolicy(self.__igno_dirnames, d.name).is_ok():
                continue
            new_dest = dest / d.name
            DirectoryCreator(new_dest,clear=self.__is_clear)
            self.__copy(d, new_dest)

    def run(self):
        self.__copy(self.__src, self.__dest)

