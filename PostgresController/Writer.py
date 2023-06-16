# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 22:31:33 2023

@author: iwill
"""

from __future__ import annotations

from copy import copy



from PostgresController.PostgresInterface import AbstractPostgres
from PostgresController.User import User

class Writer(AbstractPostgres):
    #//Field
    querys: list[str] 
    def __init__(self, user: User):
        super().__init__(user)
        
    def set_query(self,table_name: str, datas: dict)->Writer:
        
        conditions = [f"{key} = '{datas[key]}'" for key in datas]
        where_clause = "WHERE " + " AND ".join(conditions)
        delete_query = f"delete from {table_name} {where_clause}"
        
        columns_query = ", ".join(["%s" % key for key in datas])
        values_query = ", ".join([f"'{datas[key]}'" for key in datas])
        insert_query = f"insert into {table_name} ({columns_query}) values ({values_query});"
        return self._return(delete_query,insert_query)


    def delete_duplicate(self,table_name, *columns: list[str])->Writer:
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
        