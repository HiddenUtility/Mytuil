
from pathlib import Path
from shutil import copy


from pyutil.pathuil.directory_creator import DirectoryCreator
from pyutil.pathuil.DirectoryTreeCopierCanCopyNamePolicy import DirectoryTreeCopierCanCopyNameIgnoredPolicy


class DirectoryTreeCopier:
    """再回帰で指定したディレクトリにコピーしたいディレクトリ自体コピーする。
        無視するファイルやディレクトリを指定可能。
        すでにdestがいた場合は削除しないためclearオプションを使用のこと
        無視するディレクトリ名やファイル名を指定できる。

        Args:
            src (str | Path): コピーするディレクトリ
            dest (str | Path): 出力するディレクトリ
            ignore_dirname_patterns (set[str]): 無視するディレクトリ名。パターン可
            ignore_filename_patterns (set[str]): 無視するファイル名。パターン可
            clear (bool, optional): すでにdestがいた場合は削除する。. Defaults to True.
    """
    __src : Path
    __dest : Path
    __igno_dirnames : set[str]
    __igno_filenames : set[str]
    __is_clear : bool
    def __init__(self,
                 src : str|Path,
                 dest : str|Path,
                 ignore_dirname_patterns: set[str] = set(),
                 ignore_filename_patterns: set[str] = set(),
                 clear = False,
                 ) -> None:
        """再回帰でディレクトリをコピーする。
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
        self.__igno_filenames.add("LICENSE")


    def __copy(self, target:Path, dest:Path):
        fs = [p for p in target.glob('*') if p.is_file()]
        ds = [p for p in target.glob('*') if p.is_dir()]

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
        root_dest = self.__dest / self.__src.name
        DirectoryCreator(root_dest,clear=self.__is_clear)
        self.__copy(self.__src, root_dest)


