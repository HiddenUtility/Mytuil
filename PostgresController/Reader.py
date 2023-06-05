# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 22:31:40 2023

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