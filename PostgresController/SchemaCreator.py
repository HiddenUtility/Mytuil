# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 22:35:41 2023

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

class SchemaCreator(AbstractPostgres):
    DIRNAME_TABLE: Final = "PostgresController/parent_table"
    
    #//Field
    querys: list[str] 
    def __init__(self, info: User):
        super().__init__(info)
        self.schema_names = []
        self._set_schemas()
        self._set_querys()
        
    def _set_schemas(self):
        filenames = [f.stem for f in Path(self.DIRNAME_TABLE).glob("*.csv") if f.is_file()]
        for filename in filenames:
            strs = filename.split(".")
            if len(strs) == 1: str_ = "public"
            elif len(strs) == 2: str_ = strs[0]
            else: continue
            if str_ not in self.schema_names:
                self.schema_names.append(str_)

    def _set_querys(self):
        for schema_name in self.schema_names:
            query = f"CREATE SCHEMA IF NOT EXISTS {schema_name};"
            self.querys.append(query)
            
