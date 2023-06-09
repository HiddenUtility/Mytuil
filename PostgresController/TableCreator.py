# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 22:37:54 2023

@author: iwill
"""

from __future__ import annotations
from typing import Final
import abc
import os
from pathlib import Path

import psycopg2
import pandas as pd


from PostgresController.PostgresInterface import AbstractPostgres
from PostgresController.User import User
from PostgresController.SchemaCreator import SchemaCreator

class TableCreator(AbstractPostgres):
    DIRNAME_TABLE: Final = SchemaCreator.DIRNAME_TABLE
    COL_COLUMN = "column"
    COL_TYPE = "type"
    COL_DEFAULT = "default"
    COL_NOT_NULL = "not_null"
    
    #//Field
    querys: list[str] 
    
    def __init__(self, info: User):
        super().__init__(info)
        self.filepaths = [f for f in Path(self.DIRNAME_TABLE).glob("*.csv") if f.is_file()]
        
    def _set_querys_from_csv(self, filepath: Path):
        df = pd.read_csv(filepath, engine="python", encoding="cp932", dtype=str)
        tableName = filepath.stem
        rows = []
        for _, row in df.iterrows():
            rows.append(row)
        self._set_table_create_query(tableName, rows)
        
    def _set_table_create_query(self,
                               tableName:str,
                               rows: list[pd.Series]):
        querys =[]
        for row in rows:
            col = row[self.COL_COLUMN]
            typeName = row[self.COL_TYPE]
            defaultValue = row[self.COL_DEFAULT]            
            isNotNull = bool(row[self.COL_NOT_NULL])
            if isNotNull:
                query = "{} {} DEFAULT '{}' NOT NULL".format(col, typeName, defaultValue)
            else:
                query = "{} {} DEFAULT '{}'".format(col, typeName, defaultValue)
                
            
            querys.append(query)
        
        query = "CREATE TABLE IF NOT EXISTS {} ({})".format(tableName,", ".join(querys))
        self.querys.append(query)
        
    def set_querys_from_csv(self):
        list(map(self._set_querys_from_csv, self.filepaths))
        
    def set_query(self,
                  table_name: str,
                  columns:list[str],
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
                
        query = "CREATE TABLE IF NOT EXISTS {} ({})".format(table_name,", ".join(querys))
        self.querys.append(query)
        