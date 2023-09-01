# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 17:52:15 2023

@author: nanik
"""

from postgresutil.user import User
from postgresutil.schema_creator import SchemaCreator
from postgresutil.table_creator import TableCreator
from postgresutil.role_creator import RoleCreator

class DataBaseBuilder:
    def __init__(self, user: User):
        self.user = user
        if not user.can_connect():
            raise Exception(f"接続できません。\n{user}")
        self.schema_creator = SchemaCreator(user)
        self.table_ceator = TableCreator(user)
        self.role_ceator = RoleCreator(user)
    
    def create_schema(self):
        self.schema_creator.set_schemas_from_csv().commit()

    def create_table(self):
        self.table_ceator.set_querys_from_csv().commit()

    def create_role(self):
        self.table_ceator.set_querys_from_csv().commit()