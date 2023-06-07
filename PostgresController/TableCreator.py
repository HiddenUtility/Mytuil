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


from PostgresController.PosgresInterface import AbstractPostgres
from PostgresController.User import User
from PostgresController.SchemaCreator import SchemaCreator

class Remover(AbstractPostgres):
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
        
        

    def set_querys_from_csv(self, filepath: Path):
        df = pd.read_csv(filepath, engine="python", encoding="cp932", dtype=str)
        tableName = filepath.stem
        
        rows = []
        for _, row in df.iterrows():
            rows.append(row)
        
        self._set_table_create_query(tableName, rows)
        
    def _set_table_create_query(self,
                               tableName:str,
                               rows: list[pd.Series]):
        """
        CREATE TABLE new_table (
        column1 datatype1 DEFAULT default_value1 NOT NULL,
        column2 datatype2 DEFAULT default_value2 NOT NULL,
        column3 datatype3 DEFAULT default_value3 NOT NULL,
        ...
        );
        
        """
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
        
    def run(self):
        list(map(self.set_querys_from_csv, self.filepaths))
        self.commit()
        