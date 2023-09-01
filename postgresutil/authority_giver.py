# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 21:50:41 2023

@author: iwill
"""

from __future__ import annotations
from postgresutil.creator import Creator


class AuthorityGiver(Creator):
    #//Field
    querys: list[str] 

        
    def set_query_to_edit(self, user_name: str, schema: str) -> AuthorityGiver:
        querys = []
        querys.append(f"GRANT USAGE ON SCHEMA {schema} TO {user_name};")
        querys.append(f"GRANT ALL ON ALL TABLES IN SCHEMA {schema} TO {user_name};")
        return self._return(*querys)
    def set_query_to_read(self, user_name: str, schema: str) -> AuthorityGiver:
        querys = []
        querys.append(f"GRANT USAGE ON SCHEMA {schema} TO {user_name};")
        querys.append(f"GRANT SELECT ON ALL TABLES IN SCHEMA {schema} TO {user_name};")
        return self._return(*querys)
    def set_query_to_write(self, user_name: str, schema: str) -> AuthorityGiver:
        querys = []
        querys.append(f"GRANT USAGE ON SCHEMA {schema} TO {user_name};")
        querys.append(f"GRANT SELECT, UPDATE, DELETE, INSERT ON ALL TABLES IN SCHEMA {schema} TO {user_name};")
        return self._return(*querys)