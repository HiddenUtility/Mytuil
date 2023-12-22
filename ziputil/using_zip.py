# -*- coding: utf-8 -*-
from zipfile import ZipFile, ZIP_DEFLATED
from pathlib import Path
from hashutil import ZipFileHashCheacker


class UsingZip:
    __filepath:Path
    __zi_path:Path
    __zippath:Path
    __zipfile_cheacker: ZipFileHashCheacker

    def __init__(self,target: Path):
        if not isinstance(target, Path): raise TypeError(f"{target}はパスオブジェクトではありません。")
        if not target.is_file(): raise FileNotFoundError(f"{target}というファイルは存在しません。")
        self.__filepath = target
        self.__zi_path = self.__filepath.with_suffix(".zi_")
        self.__zippath = self.__filepath.with_suffix(".zip")
        self.__zipfile_cheacker = ZipFileHashCheacker(target)

    def __unlink(self, target: Path) -> None:
        if not target.exists():
            return
        try:
            target.unlink()
        except:
            raise CanNotFileUnlinkError(f"{target}を削除出来ませんでした。")

    def to_zip(self):
        self.__unlink(self.__zi_path)
        if self.__zippath.exists():
            if self.__zipfile_cheacker.is_same(self.__zippath):
                raise ZipFileExistsError(f"{self.__filepath}はすでに圧縮されています。")
            else:
                raise NotSameCompressionDataBinaryError(f"{self.__filepath}と内容が異なる圧縮されたファイルがあります。")
        try:
            with ZipFile(self.__zi_path, "w", compression=ZIP_DEFLATED) as f:
                f.write(self.__filepath, arcname=self.__filepath.name)
        except Exception as e:
            if self.__zi_path.exists():
                self.__zi_path.unlink()
            raise CanNotCompressionError(f"{self.__filepath}の圧縮失敗\n{e}")
        
        if not self.__zipfile_cheacker.is_same(self.__zi_path):
            self.__unlink(self.__zi_path)
            raise NotSameCompressionDataBinaryError()
            
        self.__zi_path.rename(self.__zippath)
        
            
class CanNotFileUnlinkError(Exception):...
class ZipFileExistsError(FileExistsError):...
class CanNotCompressionError(Exception):...
class NotSameCompressionDataBinaryError(Exception):...