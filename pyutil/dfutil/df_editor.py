# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 05:39:57 2023

@author: iwill
"""
from __future__ import annotations
from pandas import DataFrame
import unicodedata

class DataFrameEditor:
    def __init__(self, df: DataFrame = DataFrame()):
        if not isinstance(df, DataFrame): raise TypeError("arg is NOT DataFrame")
        self.__df = df
        
    def __chk_column(self, column: str):
        if column not in set(self.__df.columns): raise NotColumnsContainsError().set_message(column)
    
    def narrow_down_contains(self, column:str, key: str) -> DataFrameEditor:
        if key.upper() == "ALL":return self
        self.__chk_column(column)
        return DataFrameEditor(self.__df[self.__df[column].str.contains(key)])
    
    def narrow_down_key(self, column:str, key: any) -> DataFrameEditor:
        if key.upper() == "ALL":return self
        self.__chk_column(column)
        return DataFrameEditor(self.__df[self.__df[column]==key])
    
    def __narrow_query(self, rows: dict, query: str) -> dict:
        new_rows = {}
        for i, v in rows.items():
            if query in v:  new_rows[i] = v
        return new_rows
    
    def narrow_down_query(self, search_query: str) -> DataFrameEditor:
        rows = {}
        for i, row in self.__df.iterrows():
            #row : pandas.Serires
            rows[i] = " ".join([str(v) for v in row])
            
        querys:set = SearchQuery(search_query).querys
        for query in querys:
            rows = self.__narrow_query(rows, query)
        return DataFrameEditor(self.__df[list(rows.keys())])
    
    @property
    def df(self):
        return self.__df
    

class SearchQuery:
    __search_query: str
    
    def __init__(self, search_query: str):
        self.__search_query = self.__normalize(search_query)
    
    @staticmethod
    def __normalize(search_query:str) -> str:
        return unicodedata.normalize('NFKC', search_query)
    
    @property
    def querys(self) -> set[str]:
        return set(self.__search_query.split(" "))
    
    
    
class NotColumnsContainsError(Exception):
    def set_message(self, colmun:str) -> NotColumnsContainsError:
        message = f"{colmun}はDataFrameに含まれません。"
        return NotColumnsContainsError(message)