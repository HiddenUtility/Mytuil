
from pathlib import Path
from pyutil.pathuil.directory_creator import DirectoryCreator

from pyutil.filetransfer.file_data_coping import FileDataCoping
from pyutil.filetransfer.file_data_remover import FileSourceDataRemover


class FileDataTransfer:
    """ファイルを転送する"""
    __src : Path
    __dst : Path
    def __init__(self, src_filepath: Path, dest_dirpath:Path):
        """ファイルを転送する

        Args:
            src_filepath (Path): コピー対象のファイルパス
            dest_dirpath (Path): コピー先のディレクトリパス

        """

        if not isinstance(src_filepath, Path): raise TypeError()
        if not isinstance(dest_dirpath, Path): raise TypeError()
        if not src_filepath.exists(): raise FileNotFoundError(f'{src_filepath}は存在しません。')
        self.__src = src_filepath
        self.__dst = dest_dirpath

    def __mkdir(self, path: Path):
        DirectoryCreator.mkdir(path)

    def run(self, overwrite=True, unlink_src=True):
        """転送開始

        Args:
            overwrite (bool, optional): 既に存在していたら上書きするかどうか. Defaults to True.
            unlink_src (bool, optional): 移動に成功したらソースを消すかどうか. Defaults to True.
        """
        self.__mkdir(self.__dst)
        FileDataCoping(self.__src, self.__dst, overwrite=overwrite).run()
        if unlink_src:
            FileSourceDataRemover(self.__src).run()


        
        