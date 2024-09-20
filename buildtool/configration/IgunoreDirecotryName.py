#!/usr/bin/python
# -*- coding: utf-8 -*-
"""IgunoreDirecotryName.py

Explain : デフォルトで無視するディレクトリ名
          
Create  : 2024-06-13(木): H.U
          
Todo    : 
          
"""


class IgunoreDirecotryName:
    """デフォルトで無視するディレクトリ名"""

    __value =  [
        ".git",
        ".venv",
        "__pycache__",
    ]

    VALUE : list[str] = __value


