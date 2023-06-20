# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 22:31:40 2023

@author: iwill
"""

from __future__ import annotations

import psycopg2
import pandas as pd

from PostgresController.PostgresInterface import AbstractPostgres
from PostgresController.User import User

class Reader(AbstractPostgres):
    #//Field
    querys: list[str] 
    def __init__(self, info: User):
        super().__init__(info)


    def set_query(self, table_name: str, 
                  values: dict[str:str] = None,
                  columns: list[str] = None) -> Reader:
        """
        

        Parameters
        ----------
        table_name : str
            Target Talbe name
        values : dict[str:str], optional
            検索したい値を辞書で指定する. The default is None.
        columns : list[str], optional
            得たい列名指定があれば指定する. The default is None.

        Returns
        -------
        Reader
            DESCRIPTION.

        """
        columns_query = "*" if columns is None else ", ".join(columns)
        where = "" if values is None else " where " + " AND ".join([ f"{key} = '{values[key]}'" for key in values])
        query = f"select {columns_query} from {table_name} {where};"
        
        return self._return(query)
        

    def read(self) -> (list[list[str]],list[str]):
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
        colnames = [col.name for col in cur.description]
        # close connection
        cur.close()
        conn.close()
        self.querys = []
        return rows, colnames
    
    def getDataFrame(self, table_name: str, 
                  values: dict[str:str] = None,
                  columns: list[str] = None) -> pd.DataFrame:
        new = self.set_query(table_name, values, columns)
        rows,columns = new.read()
        if len(rows) == 0:return pd.DataFrame()
        return pd.DataFrame(rows, columns=columns)
                
                

