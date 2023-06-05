# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 22:31:33 2023

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


class PostgresInsert(AbstractPostgres):
    def __init__(self, info: InformationSQL):
        super().__init__(info)
        
    def delete_duplicate(self,table_name, *columns: list[str]):
        if len(columns) == 0:return
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
        
        self.querys.append(query, key, )