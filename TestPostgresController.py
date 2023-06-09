# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 22:41:56 2023

@author: iwill
"""

from Myutil.DummiyDictionary import DummiyDictionary

from PostgresController.User import User
from PostgresController.SchemaCreator import SchemaCreator
from PostgresController.TableCreator import TableCreator
from PostgresController.Reader import Reader
from PostgresController.Writer import Writer


if __name__ == "__main__":
    """
    \c postgres
    DROP DATABASE test;
    CREATE DATABASE test;
    \c test
    """
    
    user = User(database="test",password="kpqocxz6%")
    assert user.canConnect(), "接続できません。"
    
    #// Create schema
    creator = SchemaCreator(user)
    #print(creator)
    creator.commit()
    #// Create table
    tableCreator = TableCreator(user)
    tableCreator.set_querys_from_csv()
    #print(tableCreator)
    
    #// +演算子で足せる
    creator = creator + tableCreator
    #//wirter
    writer = Writer(user)
    for i in range(10):
        datas = DummiyDictionary.random_dict()
        writer.set_query("user_info.user_info", datas)
    #print(writer)
    creator = creator + writer
    print(creator)
    creator.commit()
    
    #//reader
    reader = Reader(user)
    columns = ["id","name","age","rank"]
    #whereはパターンがありすぎるので直接つくって入れる
    df = reader.getDataFrame("user_info.user_info", columns, where="")
    """
    Dummiyを消す。
    DELETE FROM user_info.user_info;
    """

    
    
    
    
    
    