from pyutil.pathuil.DirectoryTreeCopierCanCopyNamePolicy import DirectoryTreeCopierCanCopyNameIgnoredPolicy

from os import rmdir
from pathlib import Path


class DirectoryTreeRemover:
    """再回帰でディレクトリ内を削除する。
    - .venv, .git, .gitignoreは消さない

        target (Path): 出力するディレクトリ
        ignore_dirname_patterns (_type_, optional): 無視するディレクトリ名。正規表現の前方一致. Defaults to set().
        ignore_filename_patterns (_type_, optional): 無視するファイル名。正規表現の前方一致. Defaults to set().
    """
    __target : Path
    __igno_dirnames : set[str]
    def __init__(self,
                 target: Path,
                 ignore_dirname_patterns  = set(),
                 ignore_filename_patterns  = set(),
                 ) -> None:
        """再回帰でディレクトリ内を削除する。

        Args:
            target (Path): 出力するディレクトリ
            ignore_dirname_patterns (_type_, optional): 無視するディレクトリ名。正規表現の前方一致. Defaults to set().
            ignore_filename_patterns (_type_, optional): 無視するファイル名。正規表現の前方一致. Defaults to set().
        """


        self.__target = Path(target)
        self.__igno_dirnames = set(ignore_dirname_patterns)
        self.__igno_filenames = set(ignore_filename_patterns)
        
        self.__igno_dirnames.add('.venv')
        self.__igno_dirnames.add('.git')
        self.__igno_filenames.add('.gitignore')

    def __unlink(self, target:Path):
        fs = [p for p in target.glob('*') if p.is_file()]
        ds = [p for p in target.glob('*') if p.is_dir()]


        for f in fs:
            if not DirectoryTreeCopierCanCopyNameIgnoredPolicy(self.__igno_filenames, f.name).is_ok():
                continue
            f.unlink()

        for d in ds:
            if not DirectoryTreeCopierCanCopyNameIgnoredPolicy(self.__igno_dirnames, d.name).is_ok():
                continue
            self.__unlink(d)
            rmdir(d)


    def run(self):
        if not self.__target.exists():
            return
        self.__unlink(self.__target)