from pyutil.hashutil.zipfile_hash_cheacker import ZipFileHashCheacker
from pyutil.ziputil.error.CanNotCompressionError import CanNotCompressionError
from pyutil.ziputil.error.CanNotFileUnlinkError import CanNotFileUnlinkError
from pyutil.ziputil.error.NotSameCompressionDataBinaryError import NotSameCompressionDataBinaryError
from pyutil.ziputil.error.ZipFileExistsError import ZipFileExistsError
from pyutil.ziputil.i_zip_compressor import IZipCompressor


from pathlib import Path
from typing import override
from zipfile import ZIP_DEFLATED, ZipFile
from shutil import rmtree


class EasyDirectoryCompressor(IZipCompressor):
    """ディレクトリをzipに圧縮する

    圧縮中は仮拡張子を付与し、問題なく圧縮されていれば.zipを付与する。
    """
    __target_dirpath:Path
    __temp_path:Path
    __zip_path:Path


    __overwrite : bool
    __unlink_src : bool

    def __init__(self,target_dirpath: Path, overwrite = True, unlink_src = True):
        """ファイルをzipに圧縮する
        同じディレクトリに出力する
        圧縮中は仮の拡張子にする


        Args:
            target_path (Path): ファイルまはたディレクトリ
            overwite (bool, optional): 同名が存在していたら上書きする. Defaults to True.
            unlink_src (bool, optional): 圧縮ができたらソースを削除する. Defaults to True.

        """
        self.__overwrite = overwrite
        self.__unlink_src = unlink_src
        if not isinstance(target_dirpath, Path): raise TypeError(f"{target_dirpath}はパスオブジェクトではありません。")
        if not target_dirpath.is_dir(): raise NotADirectoryError(f"{target_dirpath}というデレィトリは存在しません。")
        self.__target_dirpath = target_dirpath
        self.__temp_path = self.__target_dirpath.with_suffix(".ziptemp")
        self.__zip_path = self.__target_dirpath.with_suffix(".zip")


    def __unlink_temp(self) -> None:
        if not self.__temp_path.exists():
            return
        try:
            self.__temp_path.unlink()
        except:
            raise CanNotFileUnlinkError(f"{self.__temp_path}を削除出来ませんでした。")

    def __write(self, zipfile : ZipFile, target :Path, parents: list[str]):
        fs = [p for p in target.glob('*') if p.is_file()]
        ds = [p for p in target.glob('*') if p.is_dir()]


        for f in fs:
            arcname = f"{'/'.join(parents)}/{f.name}"
            zipfile.write(f, arcname=arcname)
        
        for d in ds:
            new = parents + [d.name]
            self.__write(zipfile, d, new)


    @override
    def to_zip(self):

        self.__unlink_temp()

        if self.__zip_path.exists():
            if self.__overwrite:
                pass
            else:
                return

        try:
            with ZipFile(self.__temp_path, "w", compression=ZIP_DEFLATED) as zf:

                self.__write(zf, self.__target_dirpath, [])

        except Exception as e:
            if self.__temp_path.exists():
                self.__temp_path.unlink()
            raise CanNotCompressionError(f"{self.__target_dirpath}の圧縮失敗\n{e}")


        self.__temp_path.rename(self.__zip_path)

        if self.__unlink_src:
            rmtree(self.__target_dirpath, ignore_errors=True)

