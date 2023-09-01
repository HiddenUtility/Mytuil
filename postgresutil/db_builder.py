# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 17:52:15 2023

@author: nanik
"""

from postgresutil.user import User
from postgresutil.schema_creator import SchemaCreator
from postgresutil.table_creator import TableCreator

class DataBaseBuilder:
    def __init__(self, user: User):
        self.user = user
        if not user.can_connect():
            raise Exception(f"接続できません。\n{user}")
        self.schema_creator = SchemaCreator(user)
        self.table_ceator = TableCreator(user)
    
    def create_schema(self):
        creator = self.schema_creator.set_schemas_from_csv()
        creator.commit()
        