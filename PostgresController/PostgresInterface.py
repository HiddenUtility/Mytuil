# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 22:34:15 2023

@author: iwill
"""
from __future__ import annotations
import abc
import psycopg2
from PostgresController.User import User

    
class InterfacePostgres(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def commit(self):
        pass
    @abc.abstractmethod
    def get(self):
        pass

class AbstractPostgres(InterfacePostgres):
    #//Field
    querys: list[str] 
    
    def __init__(self, info: User):
        if not info.canConnect():raise ConnectionError("SQLに接続できません。")
        self.host = info.host
        self.user = info.user
        self.port = info.port
        self.database = info.database
        self.password = info.password
        
        self.querys = []
        
    def commit(self) -> None:
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
        conn.commit()
        
        # close connection
        cur.close()
        conn.close()
        
    def get(self) -> None:
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
        