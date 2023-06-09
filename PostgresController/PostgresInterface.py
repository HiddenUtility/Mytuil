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


class AbstractPostgres(InterfacePostgres):
    #//Field
    querys: list[str] 
    
    def __init__(self, user: User):
        if not isinstance(user, User): raise TypeError("NOT User Object")
        if not user.canConnect():raise ConnectionError("SQLに接続できません。")
        self.host = user.host
        self.user = user.user
        self.port = user.port
        self.database = user.database
        self.password = user.password
        self.querys = []
        
    def __repr__(self):
        return "\n".join(self.querys)
    
    def __add__(self,obj):
        if not isinstance(obj, InterfacePostgres): raise TypeError
        self.querys += obj.querys
        return self
        
        
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
        self.querys =[]
        

        