# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 22:39:06 2023

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



class RoleCreator(AbstractPostgres):
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
        