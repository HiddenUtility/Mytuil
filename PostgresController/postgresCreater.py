# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 21:04:20 2023

@author: iwill
"""
from __future__ import annotations
from typing import Final
import abc
import os
from pathlib import Path

import psycopg2
import pandas as pd



    

        


    

        

        
        

        

        

class PostgresUpdate(AbstractPostgres):
    def __init__(self, info: InformationSQL):
        super().__init__(info)


class PostgresDelete(AbstractPostgres):
    def __init__(self, info: InformationSQL):
        super().__init__(info)
        


if __name__ =="__main__":
    info = InformationSQL()
    if not info.canConnect(): raise ConnectionError("SQLに接続できません。")
    print("Success Connecting!!")
    
    import sys
    sys.exit()
    schemaCreator = PostgresSchemaCreator(info).run()
    tableCreator = PostgresTableCreator(info).run()
    
    
    

    
