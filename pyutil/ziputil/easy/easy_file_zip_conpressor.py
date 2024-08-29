
from typing import override

from zipfile import ZipFile
from pathlib import Path

from pyutil.ziputil.ZipFileCompressionMethod import ZipFileCompressionMethod
from pyutil.ziputil.i_zip_compressor import IZipCompressor
from pyutil.hashutil.zipfile_hash_cheacker import ZipFileHashCheacker
from pyutil.ziputil.error.CanNotFileUnlinkError import CanNotFileUnlinkError
from pyutil.ziputil.error.ZipFileExistsError import ZipFileExistsError
from pyutil.ziputil.error.NotSameCompressionDataBinaryError import NotSameCompressionDataBinaryError
from pyutil.ziputil.error.CanNotCompressionError import CanNotCompressionError



class EasyFileZipConpressor(IZipCompressor):
    """ファイルをzipに圧縮する
    
    圧縮中は仮拡張子を付与し、問題なく圧縮されていれば.zipを付与する。
    """
    __filepath:Path
    __temp_path:Path
    __zip_path:Path
    __zipfile_cheacker: ZipFileHashCheacker

    __overwrite : bool
    __unlink_src : bool

    def __init__(self,target_path: Path, overwrite = True, unlink_src = True):
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

        if not isinstance(target_path, Path): raise TypeError(f"{target_path}はパスオブジェクトではありません。")
        if not target_path.is_file(): raise FileNotFoundError(f"{target_path}というファイルは存在しません。")
        self.__filepath = target_path
        self.__temp_path = self.__filepath.with_suffix(".ziptemp")
        self.__zip_path = self.__filepath.with_suffix(".zip")
        self.__zipfile_cheacker = ZipFileHashCheacker(target_path)

    def __unlink_temp(self) -> None:
        if not self.__temp_path.exists():
            return
        try:
            self.__temp_path.unlink()
        except:
            raise CanNotFileUnlinkError(f"{self.__temp_path}を削除出来ませんでした。")

    @override
    def to_zip(self):
        self.__unlink_temp()
        
        if self.__zip_path.exists():
            if self.__overwrite:
                pass
            elif self.__zipfile_cheacker.is_same(self.__zip_path):
                raise ZipFileExistsError(f"{self.__filepath}はすでに圧縮されています。")
            else:
                raise NotSameCompressionDataBinaryError(f"{self.__filepath}と内容が異なる圧縮されたファイルがあります。")
        
        try:
            with ZipFile(self.__temp_path, "w", compression=ZipFileCompressionMethod.ZIP_DEFLATED.value) as f:
                f.write(self.__filepath, arcname=self.__filepath.name)
        except Exception as e:
            if self.__temp_path.exists():
                self.__temp_path.unlink()
            raise CanNotCompressionError(f"{self.__filepath}の圧縮失敗\n{e}")
        
        if not self.__zipfile_cheacker.is_same(self.__temp_path):
            self.__unlink_temp()
            raise NotSameCompressionDataBinaryError()
            
        self.__temp_path.rename(self.__zip_path)

        if self.__unlink_src:
            self.__filepath.unlink(missing_ok=True)
    


