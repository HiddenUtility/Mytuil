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
    def __init__(self, user: User):
        super().__init__(user)
        self.schema_names = []
    
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
            
    def set_schemas_from_csv(self) -> SchemaCreator:
        new = copy(self)
        new._set_schemas()
        new._set_querys()
        return new
        
    def set_schemas(self,schema_name: str) -> SchemaCreator:
        query = f"CREATE SCHEMA IF NOT EXISTS {schema_name};"
        return self._return(query)