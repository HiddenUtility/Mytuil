# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 22:41:56 2023

@author: iwill
"""

from PostgresController.User import User



if __name__ == "__main__":
    user = User(password="@@@@")
    if not user.canConnect(): raise Exception("接続できません。")