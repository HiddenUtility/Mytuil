# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 22:50:37 2023

@author: iwill
"""

from __future__ import annotations

from PostgresController.PostgresInterface import AbstractPostgres
from PostgresController.User import User


class InsertingData(AbstractPostgres):
    #//Field
    querys: list[str] 
    def __init__(self, user: User):
        super().__init__(user)
        
    def set_query(self,table_name: str, datas: dict)->InsertingData:
        
        columns_query = ", ".join(["%s" % key for key in datas])
        values_query = ", ".join([f"'{datas[key]}'" for key in datas])
        insert_query = f"insert into {table_name} ({columns_query}) values ({values_query});"
        return self._return(insert_query)