# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 22:37:54 2023

@author: iwill
"""

from __future__ import annotations
from typing import Final

from pathlib import Path

import pandas as pd


from postgresutil.creator import Creator
from postgresutil.schema_creator import SchemaCreator

class TableCreator(Creator):
    DIRNAME_TABLE: Final = SchemaCreator.DIRNAME_TABLE
    COL_COLUMN = "column"
    COL_PRIMARY_KYE = "primary_key"
    COL_TYPE = "type"
    COL_CONST = "constraints"
    COL_DEFAULT = "default"
    COL_NOT_NULL = "not_null"
    #//Field
    querys: list[str] 
    
    def _get_table_create_query(self,
                               table_name:str,
                               df: pd.DataFrame) -> str:
        querys =[]
        primary_keys = []
        for _, row in df.iterrows():
            col = row[self.COL_COLUMN]
            primary = row[self.COL_PRIMARY_KYE]
            type_name = row[self.COL_TYPE]
            constraints = row[self.COL_CONST]
            default_value = row[self.COL_DEFAULT]            
            is_not_null = bool(row[self.COL_NOT_NULL])
            if is_not_null:
                query = "{} {} {} DEFAULT '{}' NOT NULL".format(col, type_name, constraints, default_value)
            else:
                query = "{} {} {} DEFAULT '{}'".format(col, type_name, constraints, default_value)
            querys.append(query)
            if bool(primary):
                primary_keys.append(col)
        
        if len(primary_keys) == 0: raise Exception("primary_keyがありません。")
        query = "CREATE TABLE IF NOT EXISTS {} ({}, PRIMARY KEY({}))".format(
            table_name,", ".join(querys), ", ".join(primary_keys))
        return query
    
    def _get_query_from_csv(self, filepath: Path) -> str:
        try:
            df = pd.read_csv(filepath, engine="python", encoding="cp932", dtype=str).fillna("")
        except Exception as ex:
            raise Exception(f"{filepath} is Not reading. {ex}")
        table_name = filepath.stem
        return self._get_table_create_query(table_name, df)
    
    def _get_querys_from_csvfiles(self) -> list[str]:
        filepaths = [f for f in Path(self.DIRNAME_TABLE).glob("*.csv") if f.is_file()]
        if len(filepaths) == 0 : raise FileNotFoundError(f"{self.DIRNAME_TABLE}内にファイルがありません。") 
        return list(map(self._get_query_from_csv, filepaths))
        
    def set_query(self,
                  table_name: str,
                  columns:list[str],
                  primary_keys: list[str],
                  type_names:list[str],
                  default_values:list[str],
                  not_null=True
                  ):
        """
        Parameters
        ----------
        table_name : str
            テーブル名。スキーマある場合はSchema_name.table_name
        columns : list[str]
            列名のリスト.
        type_names : list[str]
            列の制約のリスト.
        default_values : list[str]
            列のデフォルト値のリスト.
        not_null : TYPE, optional
            NOT　NULLを付与する. The default is True.
        Returns
        -------
        None.

        """
        
        querys =[]
        for i, column in enumerate(columns):
            if not_null:
                query = "{} {} DEFAULT '{}' NOT NULL".format(
                    column, type_names[i], default_values[i])
            else:
                query = "{} {} DEFAULT '{}'".format(column, type_names[i], default_values[i])
                
        query = "CREATE TABLE IF NOT EXISTS {} ({}, PRIMARY KEY ({}))".format(table_name,
                                                            ", ".join(querys),
                                                            ", ".join(primary_keys)
                                                            )
        
        return self._return(query)

    def set_querys_from_csv(self) -> TableCreator:
        querys = self._get_querys_from_csvfiles()
        return self._return(*querys)

        