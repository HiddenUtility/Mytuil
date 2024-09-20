from __future__ import annotations


from pyutil.pathuil.directory_creator import DirectoryCreator
from pyutil.pickleutil.error.PickleFileLoadingFailureError import PickleFileLoadingFailureError
from pyutil.pickleutil.error.PickleFileOutputFailureError import PickleFileOutputFailureError


import bz2
import pickle
from pathlib import Path


class PickleCompressor:
    """重いオブジェクトだとストレージ効率が悪いため圧縮と組み合わせる"""
    __path : Path
    __obj : object
    __over_write : bool
    TEMP_SUFFIX = '.pkltemp'
    COMPRESS_LEVEL = 9

    def __init__(self, 
                filepath : Path,
                obj : object,
                ok_mkdir=True,
                over_write=True
                ) -> None:
        """圧縮しつつ出力する

        Args:
            filepath (Path, optional): 出力するファイルパス
            obj (object, optional): 出力したいオブジェクト
            ok_mkdir (bool, optional): 出力先ディレクトリを作る. Defaults to True.
            over_write (bool, optional): 上書きするかどうか. Defaults to True.

        """
        
        self.__path = filepath
        self.__obj = obj
        self.__over_write = over_write
        if ok_mkdir:
            DirectoryCreator(filepath.parent)

    @classmethod
    def __load(cls, filepath : Path) -> object:
        with bz2.BZ2File(filepath, 'rb', compresslevel=cls.COMPRESS_LEVEL) as fin:
            pkl = fin.read()
            return pickle.loads(pkl)

    def __dump(self):
        """出力する

        tempあったら消す
        上書き可かどうかはオプション

        """
        pkl = pickle.dumps(self.__obj)
        temppath = self.__path.with_suffix(self.TEMP_SUFFIX)
        if temppath.exists():
            temppath.unlink(missing_ok=True)

        try:
            with bz2.BZ2File(temppath, 'wb', compresslevel=self.COMPRESS_LEVEL) as fout:
                fout.write(pkl)
        except Exception as e:
            temppath.unlink(missing_ok=True)
            raise e
        
        if self.__over_write:
            if self.__path.exists():
                self.__path.unlink(missing_ok=True)

        temppath.rename(self.__path)


    def dump(self)-> None:
        """出力する

        Raises:
            AttributeError: インスタンス時の引数不足
            AttributeError: インスタンス時の引数不足
            PickleFileOutputFailureError: 出力失敗
        """

        if self.__path is None:
            raise AttributeError()
        if self.__obj is None:
            raise AttributeError()
        try:
            self.__dump()
        except Exception as e:
            raise PickleFileOutputFailureError(str(e))

    @classmethod
    def load(cls, src : Path) -> PickleCompressor:
        """PickeCommpresserで出力したファイルを読み込む

        Args:
            src (Path): ファイルパス

        Raises:
            FileNotFoundError: ない

        Returns:
            PickleCommpressor: new
        """
        if not src.is_file():
            raise FileNotFoundError()
        try:
            obj = cls.__load(src)
        except Exception as e:
            raise PickleFileLoadingFailureError(str(e))

        return PickleCompressor(src, obj, ok_mkdir=False)


    @property
    def obj(self) -> object:
        return self.__obj
    
    @property
    def filepath(self) -> Path:
        return self.__path
