# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 18:08:17 2023

@author: nanik
"""


from __future__ import annotations
from postgresutil.creator import Creator


class Editor(Creator):
    #//Field
    querys: list[str] 
    
    def delete_duplicate(self,table_name, *columns: list[str]) -> Editor:
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