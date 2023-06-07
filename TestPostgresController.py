# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 22:41:56 2023

@author: iwill
"""

from PostgresController.User import User
from PostgresController.SchemaCreator import SchemaCreator
from PostgresController.TableCreator import TableCreator


if __name__ == "__main__":
    """
    DROP DATABASE test;
    CREATE DATABASE test;
    """
    
    user = User(database="test",password="kpqocxz6%")
    assert user.canConnect(), "接続できません。"
    
    #// Create schema
    schemaCreator = SchemaCreator(user)
    print(schemaCreator)
    schemaCreator.commit()