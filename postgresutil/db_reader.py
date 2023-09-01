# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 18:13:50 2023

@author: nanik
"""

from postgresutil.reader import Reader

import psycopg2
import pandas as pd

class Reader(Reader):
    querys: list[str] 
    
    def set_query(self, table_name: str,
                  columns: list[str] = None,
                  wheres: dict[str:str] = None
                  ) -> Reader:
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
        where = "" if wheres is None else " where " + " AND ".join([ f"{key} = '{wheres[key]}'" for key in wheres])
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
    
    def get_dataframe(self, table_name: str, 
                  values: dict[str:str] = None,
                  columns: list[str] = None) -> pd.DataFrame:
        new = self.set_query(table_name, values, columns)
        rows,columns = new.read()
        if len(rows) == 0:return pd.DataFrame()
        return pd.DataFrame(rows, columns=columns)