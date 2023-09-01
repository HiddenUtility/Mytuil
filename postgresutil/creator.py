# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 22:34:15 2023

@author: iwill
"""

import psycopg2
import abc

from postgresutil.psql import Psql

class ICreator(Psql):
    @abc.abstractmethod
    def commit(self):
        pass

class Creator(ICreator):

    
    def __add__(self,obj):
        if not isinstance(obj, Creator): raise TypeError
        self.querys += obj.querys
        return self


    
    #@override
    def commit(self) -> None:
        try:
            conn = psycopg2.connect(
                host=self.host, 
                port=self.port, 
                user=self.username, 
                password=self.password, 
                database=self.database
            )
        except Exception as ex:
            raise ex
        cur = conn.cursor()
        try:
            for query in self.querys: cur.execute(query)
            conn.commit()
            self.querys =[]
        except Exception as ex:
            raise ex
        finally:
            cur.close()
            conn.close()

        