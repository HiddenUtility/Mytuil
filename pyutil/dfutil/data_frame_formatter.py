from __future__ import annotations

from pandas import DataFrame
import re

from pyutil.dfutil.search_query_formatter import SearchQueryTransformer


class DataFrameFormatter:
    """DataFrameを成形するイミュータブルなオブジェクト"""
    __df: DataFrame
    ALL = 'ALL'
    def __init__(self, df : DataFrame):
        if not isinstance(df, DataFrame):
            raise TypeError(f'dfは{type(df)}です。DataFrameオブジェクトではありません。')
        self.__df = df.copy()
    
    @staticmethod
    def __filter_by_query(rows:dict, query:str) -> dict[int, str]:
        new_rows = {}
        for i,v in rows.items():
            if re.search(query, v):
                new_rows[i] = v
        return new_rows
    
    def filter_contained_key(self,colmun:str, key:str = ALL) -> DataFrameFormatter:
        """カラムに特定のキーを含むむかどうかで絞り込む

        Args:
            colmun (str): 調査したいカラム
            key (str): 含まれるkey. Defaults to ALL.

        Returns:
            DataFrameFormatter: 絞った結果
        """
        if key.upper() == self.ALL:return self
        df = self.__df[self.__df[colmun].str.contains(key)]
        return DataFrameFormatter(df)
    

    def filter_contained_keys(self, colmuns_keys: dict[str, str]) -> DataFrameFormatter:
        """カラムに特定のキーを含むかどうか複数で絞り込む

        Args:
            colmuns_keys (dict[str, str]): 検索したいカラムと値を辞書で渡す

        Returns:
            _type_: 含んでいた
        """

        for colmun, key in colmuns_keys.items():
            dff = self.filter_contained_key(colmun, key)
        return dff

    
    def filter_key(self,colmun:str, key:str = ALL) -> DataFrameFormatter:
        """カラムに特定のキーとの完全一致かどうかで絞り込む

        Args:
            colmun (str): 調査したいカラム
            key (str): 一致させたいkey. Defaults to ALL.

        Returns:
            DataFrameFormatter: 絞った結果
        """
        if key.upper() == self.ALL:return self
        df = self.__df[self.__df[colmun]==key]
        return DataFrameFormatter(df)
    
    def filter_keys(self, colmuns_keys: dict[str, str]) -> DataFrameFormatter:
        """カラムに特定のキーとの完全一致かどうか複数で絞り込む

        Args:
            colmuns_keys (dict[str, str]): 検索したいカラムと値を辞書で渡す

        Returns:
            _type_: 含んでいた
        """

        for colmun, key in colmuns_keys.items():
            dff = self.filter_key(colmun, key)
        return dff

    
    def filter_query(self, search_query:str = ALL, target_columns: list[str] = []) -> DataFrameFormatter:
        """全カラムから調査したいクエリを含むかどうかで絞り込む

        Args:
            search_query (str): 調査したいクエリ. Defaults to ALL.
            columns (list[str], optional): 調査対象を指定したい場合. Defaults to [].

        Returns:
            DataFrameFormatter: 絞った結果
        """


        if search_query.upper() == self.ALL:return self
        if target_columns:
            target_df = self.__df[target_columns]
        else:
            target_df = self.__df.copy()
        rows = {}
        for i, row in target_df.iterrows():
            rows[i] = "||".join([f"{k}={v}" for k, v in row.to_dict().items()]).lower()
        querys = SearchQueryTransformer(search_query).get_querys()
        
        for query in querys:
            rows = self.__filter_by_query(rows, query)
    
        new = self.__df.iloc[list(rows.keys())]
        return DataFrameFormatter(new)
    

    
    def to_df(self) -> DataFrame:
        """DataFrameに変換する

        Returns:
            DataFrame: It is DataFrame Object.
        """
        return self.__df
    
    @property
    def df(self):
        return self.to_df()
    
    @property
    def columns(self):
        return list(self.__df.columns)
    
    @property
    def empty(self) -> bool:
        return self.__df.empty

