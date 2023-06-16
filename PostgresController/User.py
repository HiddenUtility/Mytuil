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

    def __init__(self, 
                 host: str="localhost",
                 port: int=5432, 
                 database: str="postgres", 
                 username: str="postgres",
                 password: str="passwrod"):
        self.host = host
        self.port = port
        self.database = database
        self.username = username
        self.password = password
        
    def __str__(self):
        strs = [
            "******************************",
            f"host = {self.host}",
            f"port = {self.port}",
            f"database = {self.database}",
            f"username = {self.username}",
            f"password = {self.password}",
            "******************************"
            ]
        return "\n".join(strs)
    def __repr__(self):
        return self.__str__()
        
    def set_local_user(self, 
                 host: str="localhost",
                 port: int=5432, 
                 database: str="postgres", 
                 username: str="postgres",
                 password: str="passwrod"):
        self.host = host
        self.username = username
        self.port = port
        self.database = database
        self.password = password
        
    def canConnect(self):
        try:
            conn = psycopg2.connect(
                host=self.host, 
                port=self.port, 
                user=self.username, 
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
    
