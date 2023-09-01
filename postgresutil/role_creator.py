# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 21:48:33 2023

@author: iwill
"""

from __future__ import annotations
from postgresutil.creator import Creator


class RoleCreator(Creator):
    #//Field
    querys: list[str] 
        
    def set_query(self, user_name: str, passwrod: str,conection_limit=16) -> RoleCreator:
        querys = []
        querys.append(
            f"""
            DO $$
            BEGIN
              IF NOT EXISTS (SELECT * FROM pg_user WHERE usename = '{user_name}') THEN
                CREATE ROLE {user_name} LOGIN PASSWORD '{passwrod}';
              END IF;
            END $$;
            """
            )
        querys.append(f"ALTER ROLE {user_name} CONNECTION LIMIT {conection_limit}")
        return self._return(*querys)
        