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

from PostgresController.PosgresInterface import AbstractPostgres
from PostgresController.User import User

class Reader(AbstractPostgres):
    #//Field
    querys: list[str] 
    def __init__(self, info: User):
        super().__init__(info)

    def set_query(self):
        ...
        query = "SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'your_table_name'"


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
        return rows


