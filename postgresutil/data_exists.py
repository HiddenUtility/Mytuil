# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 22:36:39 2023

@author: iwill
"""

from __future__ import annotations

import psycopg2
import pandas as pd

from PostgresController.PostgresInterface import AbstractPostgres
from PostgresController.User import User



class DataExists(AbstractPostgres):
    #//Field
    querys: list[str] 
    def __init__(self, info: User):
        super().__init__(info)
        
    def _set_query(self, table_name: str, datas: dict[str: str]):
        values = []
        columns = []
        for key in datas:
            if datas[key] == "":continue
            values.append(f"key = '{datas[key]}'")
            columns.append(key)
            
        columns_query = ", ".join(values)
        where = " AND ".join(values)
        query = f"SELECT {columns_query} FROM {table_name} {where};"
        
        self.querys.append(query)
        

    def _read(self) -> None:
        # connect to PostgreSQL and create table
        conn = psycopg2.connect(
            host=self.host, 
            port=self.port, 
            user=self.username, 
            password=self.password, 
            database=self.database
        )
        cur = conn.cursor()
        for query in self.querys: cur.execute(query)
        rows = cur.fetchall()
        # close connection
        cur.close()
        conn.close()
        self.querys = []
        return rows
    
    def exists(self,table_name: str, datas: dict[str: str]) -> bool:
        """
        Parameters
        ----------
        table_name : str
            Target Schema.Tablenmae
        datas : dict[str: str]
            config values
            dict = {colname : value}

        Returns
        -------
        TYPE
            bool.

        """
        self._set_query(table_name,datas)
        rows = self._read()
        return len(rows) > 0
        