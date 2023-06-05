# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 22:31:12 2023

@author: iwill
"""


from __future__ import annotations
from typing import Final
import abc
import os
from pathlib import Path

import psycopg2
import pandas as pd



class User:
    def __init__(self):
        pass

class ConnectingInfomation:
    def __init__(self, 
                 host: str="localhost",
                 user: str="postgres",
                 port: int=5432, 
                 database: str="postgres", 
                 password: str="postgres"):
        self.host = host
        self.user = user
        self.port = port
        self.database = database
        self.password = password
        
    def canConnect(self):
        try:
            conn = psycopg2.connect(
                host=self.host, 
                port=self.port, 
                user=self.user, 
                password=self.password, 
                database=self.database
            )
        except:
            return False
        
        cur = conn.cursor()
        can = False
        if not conn.closed:
            can = True
        cur.close()
        conn.close()
        return can