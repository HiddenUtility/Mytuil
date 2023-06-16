# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 21:50:41 2023

@author: iwill
"""

from __future__ import annotations
from typing import Final
import abc
import os
from pathlib import Path


from copy import copy

from PostgresController.PostgresInterface import AbstractPostgres
from PostgresController.User import User

class AuthorityGiver(AbstractPostgres):
    #//Field
    querys: list[str] 
    def __init__(self, user: User):
        super().__init__(user)
        
    def set_query_to_edit(self, user_name: str, schema) -> AuthorityGiver:
        querys = []
        querys.append(f"GRANT USAGE ON SCHEMA {schema} TO {user_name};")
        querys.append(f"GRANT ALL ON ALL TABLES IN SCHEMA {schema} TO {user_name};")
        return self._return(*querys)
    def set_query_to_read(self, user_name: str, schema) -> AuthorityGiver:
        querys = []
        querys.append(f"GRANT USAGE ON SCHEMA {schema} TO {user_name};")
        querys.append(f"GRANT SELECT ON ALL TABLES IN SCHEMA {schema} TO {user_name};")
        return self._return(*querys)
    def set_query_to_write(self, user_name: str, schema) -> AuthorityGiver:
        querys = []
        querys.append(f"GRANT USAGE ON SCHEMA {schema} TO {user_name};")
        querys.append(f"GRANT SELECT, UPDATE, DELETE, INSERT ON ALL TABLES IN SCHEMA {schema} TO {user_name};")
        return self._return(*querys)