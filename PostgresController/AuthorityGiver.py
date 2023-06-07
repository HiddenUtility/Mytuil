# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 21:50:41 2023

@author: iwill
"""

from __future__ import annotations
from typing import Final
import abc
import os
from pathlib import Path

import psycopg2
import pandas as pd

from PostgresController.PosgresInterface import AbstractPostgres
from PostgresController.User import User

class AuthorityGiver(AbstractPostgres):
    #//Field
    querys: list[str] 
    def __init__(self, info: User):
        super().__init__(info)