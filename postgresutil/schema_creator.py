# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 22:35:41 2023

@author: iwill
"""

from __future__ import annotations
from typing import Final

from copy import copy
from pathlib import Path

from postgresutil.creator import Creator
from postgresutil.user import User

class SchemaCreator(Creator):
    DIRNAME_TABLE: Final = "postgresutil/parent_table"
    
    #//Field
    querys: list[str] 

    def _get_querys_from_csv(self) -> list[str]:
        filenames = [f.stem for f in Path(self.DIRNAME_TABLE).glob("*.csv") if f.is_file()]
        schema_names = []
        for filename in filenames:
            strs = filename.split(".")
            if len(strs) == 1: str_ = "public"
            elif len(strs) == 2: str_ = strs[0]
            else: continue
            if str_ not in schema_names: schema_names.append(str_)
        return [self._get_query(s) for s in schema_names]

    def _get_query(self,schema_name: str) -> str:
        return f"CREATE SCHEMA IF NOT EXISTS {schema_name};"
        
    def set_schemas(self,schema_name: str) -> SchemaCreator:
        query = self._get_query(schema_name)
        return self._return(query)
    
    def set_schemas_from_csv(self) -> SchemaCreator:
        querys = self._get_querys_from_csv()
        return self._return(*querys)