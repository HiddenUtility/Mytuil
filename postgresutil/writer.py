# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 22:31:33 2023

@author: iwill
"""

from __future__ import annotations

from postgresutil.editor import Editor


class Writer(Editor):
    #//Field
    querys: list[str] 

        
    def set_query(self,table_name: str, datas: dict)->Writer:
        
        conditions = [f"{key} = '{datas[key]}'" for key in datas]
        where_clause = "WHERE " + " AND ".join(conditions)
        delete_query = f"delete from {table_name} {where_clause}"
        
        columns_query = ", ".join(["%s" % key for key in datas])
        values_query = ", ".join([f"'{datas[key]}'" for key in datas])
        insert_query = f"insert into {table_name} ({columns_query}) values ({values_query});"
        return self._return(delete_query,insert_query)



        