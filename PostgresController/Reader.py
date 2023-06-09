# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 22:31:40 2023

@author: iwill
"""

from __future__ import annotations
from typing import Final
import abc
import os
from pathlib import Path

import psycopg2
import pandas as pd

from PostgresController.PostgresInterface import AbstractPostgres
from PostgresController.User import User

class Reader(AbstractPostgres):
    #//Field
    querys: list[str] 
    def __init__(self, info: User):
        super().__init__(info)

    def set_query(self, table_name: str, columns: list[str] = None, where=""):
        if isinstance(columns, str): columns = [columns]
        columns_query = ", ".join(columns) if columns is not None else "*"
        where = f"WHERE {where}" if where != "" else where
        query = f"SELECT {columns_query} FROM {table_name} {where};"
        self.querys.append(query)


    def read(self) -> None:
        # connect to PostgreSQL and create table
        conn = psycopg2.connect(
            host=self.host, 
            port=self.port, 
            user=self.user, 
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
    
    def getDataFrame(self, table_name: str, columns: list[str], where="") -> pd.DataFrame:
        if not isinstance(columns, list):raise TypeError
        self.set_query(table_name, columns, where=where)
        rows = self.read()
        if len(rows) == 0:return pd.DataFrame()
        dictionary = {}
        for column in columns:
            dictionary[column] = []
        for row in rows:
            for i, column in enumerate(columns):
                dictionary[column].append(row[i])
        return pd.DataFrame(dictionary)
                
                

