# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 22:34:15 2023

@author: iwill
"""
from __future__ import annotations
import abc
import psycopg2
from PostgresController.User import User
from copy import copy

    
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
        self.port = user.port
        self.database = user.database
        self.username = user.username
        self.password = user.password
        self.querys = []
        
    def __repr__(self):
        return "\n".join(self.querys)
    
    def __add__(self,obj):
        if not isinstance(obj, InterfacePostgres): raise TypeError
        self.querys += obj.querys
        return self

    def _return(self,*querys:str):
        if len(querys)==0:return self
        new = copy(self)
        for query in querys:
            if not isinstance(query, str): raise TypeError
            new.querys.append(query)
        return new
          
    def commit(self) -> None:
        # connect to PostgreSQL 
        conn = psycopg2.connect(
            host=self.host, 
            port=self.port, 
            user=self.username, 
            password=self.password, 
            database=self.database
        )
        cur = conn.cursor()
        for query in self.querys: cur.execute(query)
        conn.commit()
        
        # close connection
        cur.close()
        conn.close()
        # reset
        self.querys =[]
        

        