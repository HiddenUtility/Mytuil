from __future__ import annotations
from pandas import DataFrame
import re

from pyutil.dfutil.search_query import SearchQuery


class DataFrameEditor:
    df: DataFrame
    def __init__(self,df):
        if not isinstance(df, DataFrame): raise TypeError()
        self.__df = df
        
    def _return(self,df) -> DataFrameEditor:
        return DataFrameEditor(df)
    
    @staticmethod
    def __narow_query(rows:dict, query:str) -> dict[int, str]:
        new_rows = {}
        for i,v in rows.items():
            if re.search(query, v):
                new_rows[i] = v
        return new_rows
    
    def narrow_down_contains(self,colmun:str, key:str) -> DataFrameEditor:
        if key.upper() == "ALL":return self
        df = self.__df[self.__df[colmun].str.contains(key)]
        return self._return(df)
    
    def narrow_down_key(self,colmun:str, key:str) -> DataFrameEditor:
        if key.upper() == "ALL":return self
        df = self.__df[self.__df[colmun]==key]
        return self._return(df)
    
    def narow_down_query(self, search_query:str):
        if search_query.upper() == "ALL":return self
        rows = {}
        for i, row in self.__df.iterrows():
            rows[i] = "||".join([f"{k}={v}" for k, v in row.to_dict().items()]).lower()
            
        
        querys = SearchQuery(search_query).get_querys()
        print(querys)
        for query in querys:
            rows = self.__narow_query(rows, query)
    
        new = self.__df.iloc[list(rows.keys())]
        return self._return(new)
    
    def to_df(self) -> DataFrame:
        return self.__df
    
    @property
    def df(self):
        return self.to_df()
    
    @property
    def columns(self):
        return list(self.__df.columns)

