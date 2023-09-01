# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 17:49:58 2023

@author: nanik
"""

from postgresutil.user import User

class Psql():
    #//Field
    querys: list[str] 
    def __init__(self, user: User):
        if not isinstance(user, User): raise TypeError("NOT User Object")
        if not user.can_connect():raise ConnectionError("SQLに接続できません。")
        self.host = user.host
        self.port = user.port
        self.database = user.database
        self.username = user.username
        self.password = user.password
        self.querys = []

