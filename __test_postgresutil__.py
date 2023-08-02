# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 22:41:56 2023

@author: iwill
"""

from postgresutil.dummiy_dictionary import DummiyDictionary

from postgresutil.user import User
from postgresutil.schema_creator import SchemaCreator
from postgresutil.table_creator import TableCreator
from postgresutil.reader import Reader
from postgresutil.writer import Writer
from postgresutil.role_creator import RoleCreator
from postgresutil.authority_giver import AuthorityGiver
from postgresutil.remover import Remover

if __name__ == "__main__":
    """
    \c postgres
    pqsl -U postgres
    DROP DATABASE test;
    CREATE DATABASE test;
    DROP OWNED BY Taro CASCADE;
    DROP ROLE Taro;
    
    """
    
    user = User(database="test",password="password")
    assert user.canConnect(), "接続できません。"
    
    #// Create schema
    schemaCreator = SchemaCreator(user)
    schemaCreator = schemaCreator.set_schemas_from_csv()
    print(schemaCreator)
    schemaCreator.commit()
    
    #// Create table
    tableCreator = TableCreator(user)
    tableCreator = tableCreator.set_querys_from_csv()\
        .set_query("user_info.administrator", ["id"], ["text"], ["f"*32])
    print(tableCreator)
    tableCreator.commit()
    

    #// ロール作成
    roleCreator = RoleCreator(user)
    roleCreator = roleCreator.set_query("taro", "password")
    #// 権限付与
    authorityGiver = AuthorityGiver(user)
    authorityGiver = authorityGiver.set_query_to_edit("Taro", "user_info")
    #//足せる
    creator = roleCreator + authorityGiver
    print(creator)
    creator.commit()
    
    #太郎で操作する
    userTaro = User(database="test",username="taro",password="password")
    print(userTaro)
    
    #//wirter
    writer = Writer(userTaro)
    for i in range(10):
        datas = DummiyDictionary.random_dict()
        writer = writer.set_query("user_info.user_info", datas)
    print(writer)
    writer.commit()
    
    #//reader
    reader = Reader(userTaro)
    reader = reader.set_query("user_info.user_info",datas)
    rows,columns = reader.read()
    #Table全データ
    df = reader.getDataFrame("user_info.user_info")
    
    #最後消す
    #//remover
    remover = Remover(userTaro).set_query_table_all_data("user_info.user_info")
    print(remover)
    remover.commit()
    
    
    
    """
    \c test
    \dn
    \dt user_info.*
    \du
    
    
    
    
    Dummiyを消す。
    select * from user_info.user_info;
    DELETE FROM user_info.user_info;
    """

    
    
    
    
    
    