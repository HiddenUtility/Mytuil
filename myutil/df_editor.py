# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 05:39:57 2023

@author: iwill
"""
from __future__ import annotations
from pandas import DataFrame


class DataFrameEditor:
    def __init__(self, df: DataFrame = DataFrame()):
        if not isinstance(df, DataFrame): raise TypeError("arg is NOT DataFrame")
        self.__df = df
        
    @property
    def df(self):
        return self.__df
    
    def __chk_column(self, column: str):
        if column not in set(self.__df.columns): raise NotColumnsContainsError("Not in Column at DataFrame")
    
    def narrow_down_contains(self, column:str, key: str) -> DataFrameEditor:
        if key.upper() == "ALL":return self
        self.__chk_column(column)
        return DataFrameEditor(self.__df[self.__df[column].str.contains(key)])
    def narrow_down_key(self, column:str, key: any) -> DataFrameEditor:
        if key.upper() == "ALL":return self
        self.__chk_column(column)
        return DataFrameEditor(self.__df[self.__df[column]==key])
    
    def __narrow_query(self, rows: dict, query: str):
        new_rows = {}
        for i, v in rows.items():
            if query in v:  new_rows[i] = v
        return new_rows
    
    def narrow_down_query(self, search_query: str) -> DataFrameEditor:
        rows = {}
        for i, row in self.__df.iterrows():
            #row : pandas.Serires
            rows[i] = " ".join([str(v) for v in row])
            
        querys = SearchQuery(search_query).querys
        for query in querys:
            rows = self.__narrow_query(rows, query)
        return DataFrameEditor(self.__df[list(rows.keys())])

class SearchQuery:
    ...
    
    
    
class NotColumnsContainsError(Exception):
    pass