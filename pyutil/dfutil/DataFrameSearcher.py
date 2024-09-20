from typing import Any, Generator
from pyutil.dfutil.NotFindAtDaraFrame import NotFindAtDaraFrameError
from pyutil.dfutil.data_frame_formatter import DataFrameFormatter


from pandas import DataFrame

class DataFrameSearcher:
    """DataFrameから特定の情報を取り出す"""
    __dff: DataFrameFormatter
    ALL = 'ALL'

    def __init__(self, df : DataFrame):
        if not isinstance(df, DataFrame):
            raise TypeError(f'dfは{type(df)}です。DataFrameオブジェクトではありません。')
        self.__dff = DataFrameFormatter(df)

    def to_df(self) -> DataFrame:
        """DataFrameに変換する

        Returns:
            DataFrame: It is DataFrame Object.
        """
        return self.__df
    
    def exsists_contained_key(self,colmun:str, key:str) -> bool:
        """カラムに特定のキーを含むむかどうか

        Args:
            colmun (str): _description_
            key (str, optional): 調査したいkey

        Returns:
            bool: 含んでいた
        """
        return not self.__dff.filter_contained_key(colmun=colmun, key=key).empty
    
    def exsists_contained_keys(self, colmuns_keys: dict[str, str]):
        """一致するワードを含むカラムがあるかどうか

        Args:
            colmuns_keys (dict[str, str]): 検索

        Returns:
            _type_: 含んでいた
        """

        for colmun, key in colmuns_keys.items():
            dff = self.__dff.filter_contained_key(colmun, key)
        return not dff.empty
    
    
    def exsists_key(self,colmun:str, key:str = ALL) -> bool:
        """カラムに特定のキーとの完全一致かどうか

        Args:
            colmun (str): 調査したいカラム
            key (str): 一致させたいkey. Defaults to ALL.

        Returns:
            bool: 含んでいた
        """
        return not self.__dff.filter_key(colmun=colmun, key=key).empty

    def exists_keys(self, colmuns_keys: dict[str, str])-> bool:
        """一致するワードを含むカラムがあるかどうか

        Args:
            colmuns_keys (dict[str, str]): 検索

        Returns:
            _type_: 含んでいた
        """

        for colmun, key in colmuns_keys.items():
            dff = self.__dff.filter_key(colmun, key)
        return not dff.empty
    

    def find_keys(self, colmuns_keys: dict[str, str], target_column: str) -> Generator[str, Any, Any]:
        """一致するワードを含むカラムをしらべ、指定したカラムの値を返すジェネリクス

        Args:
            colmuns_keys (dict[str, str]): 検索

        Returns:
            Generator[str]: 一致した1つだけ返すジェネレーター
        """
        if target_column not in self.__dff.columns:
            raise KeyError(f'{target_column}はDataFrameないにありません')

        for colmun, key in colmuns_keys.items():
            dff = self.__dff.filter_key(colmun, key)
        if dff.empty:
            raise NotFindAtDaraFrameError('一致する箇所がありませんでした')
        for _, row in dff.df.iterrows():
            yield str(row[target_column])
        raise StopIteration()
    

    def find_all_keys(self, colmuns_keys: dict[str, str], target_column: str) -> list[str]:
        """一致するワードを含むカラムをしらべ、指定したカラムの値を全て返す

        Args:
            colmuns_keys (dict[str, str]): 検索

        Returns:
            list[str]: 一致した全てを返す。なければ空リスト
        """
        if target_column not in self.__dff.columns:
            raise KeyError(f'{target_column}はDataFrameないにありません')

        for colmun, key in colmuns_keys.items():
            dff = self.__dff.filter_key(colmun, key)
        
        ret = []        
        for _, row in dff.df.iterrows():
            ret.append(str(row[target_column]))
        return ret


    def exists_query(self, search_query:str, target_columns: list[str] = []) -> bool:
        """全カラムから調査したいクエリを含むかどうか

        Args:
            search_query (str): 調査したいクエリ. Defaults to ALL.
            columns (list[str], optional): 調査対象を指定したい場合. Defaults to [].

        Returns:
            bool: 含んでいた
        """
        return not self.__dff.filter_query(search_query, target_columns=target_columns).empty


    

    @property
    def df(self):
        return self.__dff.to_df()

    @property
    def columns(self):
        return list(self.__dff.__df.columns)

    @property
    def empty(self) -> bool:
        return self.__dff.__df.empty