# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 16:23:08 2023

@author: nanik
"""
from __future__ import annotations
from command import Command

class ServerConnecting:
    NET_PATTERN = "NET USE {address} /user:{user} {password}"
    def __init__(self,address:str="", user:str="", password:str=""):
        self.__address = address
        self.__user = user
        self.__password = password
    def setter(self,address:str, user:str, password:str) -> ServerConnecting:
        return ServerConnecting(address,user,password)
    def connect(self):
        command = Command(self.NET_PATTERN.format(address=self.__address, user=self.__user, passowrd=self.__password))
        command.send()
        
    
    
