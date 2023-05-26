# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 21:04:20 2023

@author: iwill
"""
from typing import Final
import abc
import os
from pathlib import Path

import psycopg2
import pandas as pd


class InformationSQL:
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
    
    
class InterfacePostgres(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def commit(self):
        pass



class AbstractPostgres(InterfacePostgres):
    #//Field
    querys: list[str] 
    
    def __init__(self, info: InformationSQL):
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

class PostgresSchemaCreator(AbstractPostgres):
    DIRNAME_TABLE: Final = "parent_table"
    
    def __init__(self, info: InformationSQL):
        super().__init__(info)
        self.schema_names = []
        self._set_schemas()
        
    def _set_schemas(self):
        filenames = [f.stem for f in Path(self.DIRNAME_TABLE).glob("*.csv") if f.is_file()]
        for filename in filenames:
            strs = filename.split(".")
            if len(strs) == 1: str_ = "public"
            elif len(strs) == 2: str_ = strs[0]
            else: continue
            if str_ not in self.schema_names:
                self.schema_names.append(str_)

    def _set_querys(self):
        for schema_name in self.schema_names:
            query = f"CREATE SCHEMA IF NOT EXISTS {schema_name};"
            self.querys.append(query)
            

    def run(self):
        self._set_querys()
        self.commit()
        


    

class PostgresTableCreator(AbstractPostgres):
    DIRNAME_TABLE: Final = PostgresSchemaCreator.DIRNAME_TABLE
    
    COL_COLUMN = "column"
    COL_TYPE = "type"
    COL_DEFAULT = "default"
    COL_NOT_NULL = "not_null"
    
    
    def __init__(self, info: InformationSQL):
        super().__init__(info)
        self.filepaths = [f for f in Path(self.DIRNAME_TABLE).glob("*.csv") if f.is_file()]

    def set_querys_from_csv(self, filepath: Path):
        df = pd.read_csv(filepath, engine="python", encoding="cp932", dtype=str)
        tableName = filepath.stem
        
        rows = []
        for _, row in df.iterrows():
            rows.append(row)
        
        self._set_table_create_query(tableName, rows)
        
    def _set_table_create_query(self,
                               tableName:str,
                               rows: list[pd.Series]):
        """
        CREATE TABLE new_table (
        column1 datatype1 DEFAULT default_value1 NOT NULL,
        column2 datatype2 DEFAULT default_value2 NOT NULL,
        column3 datatype3 DEFAULT default_value3 NOT NULL,
        ...
        );
        
        """
        querys =[]
        for row in rows:
            col = row[self.COL_COLUMN]
            typeName = row[self.COL_TYPE]
            defaultValue = row[self.COL_DEFAULT]            
            isNotNull = bool(row[self.COL_NOT_NULL])
            if isNotNull:
                query = "{} {} DEFAULT '{}' NOT NULL".format(col, typeName, defaultValue)
            else:
                query = "{} {} DEFAULT '{}'".format(col, typeName, defaultValue)
                
            
            querys.append(query)
        
        query = "CREATE TABLE IF NOT EXISTS {} ({})".format(tableName,", ".join(querys))
        self.querys.append(query)
        
    def run(self):
        list(map(self.set_querys_from_csv, self.filepaths))
        self.commit()
        
        

class PostgresRoleCreator(AbstractPostgres):
    def __init__(self, info: InformationSQL):
        super().__init__(info)
    
    def create_role(self,user: str, password: str):
        query = "CREATE ROLE IF NOT EXISTS {} WITH LOGIN PASSWORD '{}';".format(user,password)
        self.querys.append(query)
        
    def give_database_ownership(self,old_user: str, new_user: str):
        query = "REASSIGN OWNED BY {} TO {};".format(old_user,new_user)
        self.querys.append(query)
    
    def give_table_authority_all(self,schema_name: str, user: str):
        query = "GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA {} TO {};".format(schema_name,user)
        self.querys.append(query)
        
    def give_table_authority_reading(self,schema_name: str, user: str):
        query = "GRANT SELECT PRIVILEGES ON ALL TABLES IN SCHEMA {} TO {};".format(schema_name,user)
        self.querys.append(query)
        
    def give_table_authority_editing(self,schema_name: str, user: str):
        query = "GRANT SELECT, UPDATE PRIVILEGES ON ALL TABLES IN SCHEMA {} TO {};".format(schema_name,user)
        self.querys.append(query)
        
        
        
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
        

        

class PostgresUpdate(AbstractPostgres):
    def __init__(self, info: InformationSQL):
        super().__init__(info)


class PostgresDelete(AbstractPostgres):
    def __init__(self, info: InformationSQL):
        super().__init__(info)
        


if __name__ =="__main__":
    info = InformationSQL()
    if not info.canConnect(): raise ConnectionError("SQLに接続できません。")
    print("Success Connecting!!")
    
    import sys
    sys.exit()
    schemaCreator = PostgresSchemaCreator(info).run()
    tableCreator = PostgresTableCreator(info).run()
    
    
    

    
