# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 22:31:48 2023

@author: iwill
"""

from __future__ import annotations
from datetime import datetime

from PostgresController.PostgresInterface import AbstractPostgres
from PostgresController.User import User

class Remover(AbstractPostgres):
    #//Field
    querys: list[str] 
    def __init__(self, user: User):
        super().__init__(user)
        
    def set_query(self,table_name: str, datas: dict=None)->Remover:
        if datas is None: return self.set_query_table_all_data(table_name)
        conditions = [f"{key} = '{datas[key]}'" for key in datas]
        where_clause = "WHERE " + " AND ".join(conditions)
        delete_query = f"delete from {table_name} {where_clause};"
        return self._return(delete_query)
    def set_query_table_all_data(self,table_name: str)->Remover:
        delete_query = f"delete from {table_name};"
        return self._return(delete_query)
    
    def set_query_delete_datetime(self,
                                  table_name: str, 
                                  column_datetime, 
                                  start=datetime(2000,1,1),
                                  end=datetime(2099,12,31))->Remover:
        delete_query = f"delete from {table_name} where {column_datetime} > '{start}' AND {column_datetime} < '{end}'"
        return self._return(delete_query)
        
    def delete_duplicate(self,table_name, *columns: list[str])->Remover:
        if len(columns) == 0:return self
        key = ", ".join([f"{column}" for column in columns])
        andQuery = "WHERE "  + " AND ".join(["t2.{column} = t1.{column}" for column in columns])
        query = """
        DELETE FROM {0} t1
        WHERE EXISITS(
        SELECT {1}
        FROM {0} t2
        {2}
        AND t2.ctid > t1.ctid
        );
        """.format(table_name, key, andQuery)
        return self._return(query)