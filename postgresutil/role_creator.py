# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 21:48:33 2023

@author: iwill
"""

from __future__ import annotations
from postgresutil.creator import Creator
import pandas as pd
from pathlib import Path

class RoleCreator(Creator):
    #//Field
    querys: list[str]
    
    USER_NAME = "user_name"
    PASSWORD = "password"
    CONNECTION = "connection_limit"

    def _get_table_create_query(self,
                               table_name:str,
                               df: pd.DataFrame) -> list[str]:
        querys =[]
        for _, row in df.iterrows:
            user_name = row[self.USER_NAME]
            password = row[self.PASSWORD]
            connection_limit = row[self.CONNECTION]
            querys.append(self._get_query(user_name,password,connection_limit))

        return querys
    
    def _get_querys_from_csv(self) -> list[str]:
        filepath = Path(self.DIRNAME_TABLE) / "roles" / "roles.csv"
        try:
            df = pd.read_csv(filepath, engine="python", encoding="cp932", dtype=str)
        except Exception as ex:
            raise Exception(f"{filepath} is Not reading. {ex}")
        table_name = filepath.stem
        return self._set_table_create_query(table_name, df)
    
    def _get_query(self, user_name: str, password: str, connection_limit=16) -> str:
        query = f"""
            
                DO $$
                BEGIN
                  IF NOT EXISTS (SELECT * FROM pg_user WHERE usename = '{user_name}') THEN
                    CREATE ROLE {user_name} LOGIN PASSWORD '{password}' CONNECTION LIMIT {connection_limit};
                  END IF;
                END $$;
                """
        return query
        
    def set_query(self, user_name: str, password: str, connection_limit=16) -> RoleCreator:
        query = self._get_query(user_name, password, connection_limit)
        return self._return(query)
    
    def set_querys_from_csv(self) -> RoleCreator:
        querys = self._get_querys_from_csv()
        return self._return(*querys)
        