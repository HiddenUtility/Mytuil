from pathlib import Path
from pandas import DataFrame

from pyutil.pathuil.directory_creator import DirectoryCreator


class DataFrameCsvTransformer:
    """大きいdfを出力するときに仮の名前にしておく"""
    __df :DataFrame
    TEMP_SUFFIX = '.tempcsv'
    BAKUP_SUFFIX = '.backupcsv'

    def __init__(self, df : DataFrame, dest: Path, encoding='cp932') -> None:
        """大きいdfを出力するときに仮の名前にしておく

        Args:
            df (DataFrame): 出力するdf
            dest (Path): 出力するファイルパス
            encoding (str, optional): エンコード. Defaults to 'cp932'.
        """
        self.__df = df
        self.__dest = dest
        self.__temp = dest.with_suffix(self.TEMP_SUFFIX)
        self.__backpu = dest.with_suffix(self.BAKUP_SUFFIX)
        self.__encoding = encoding

    def __rename(self):
        try:
            self.__temp.rename(self.__dest)
        except Exception as e:
            if self.__backpu.exists():
                self.__backpu.rename(self.__dest)
            raise e
        
    def out(self):
        """出力する
        - 仮拡張子で出力，成功すれば正式な拡張子にrename
        - 前回途中があれば削除
        - すでに同名があれば，バックアップをとり，出力できてから削除
        """
        if self.__temp.exists():
            self.__temp.unlink(missing_ok=True)
        DirectoryCreator(self.__temp.parent)
        self.__df.to_csv(self.__temp, index=False, encoding=self.__encoding)

        if self.__dest.exists():
            self.__dest.rename(self.__backpu)
        
        self.__rename()

        if self.__backpu.exists():
            self.__backpu.unlink()

        print(f'{self.__dest}を出力しました．')

