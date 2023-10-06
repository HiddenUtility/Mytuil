# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 16:05:24 2023

@author: nanik
"""

from __future__ import annotations
import subprocess
from subprocess import CalledProcessError

class Command:
    def __init__(self, command: str = ""):
        if not isinstance(command, str) : raise TypeError(f"{command} is Not string")
        self.__command = command
    def __str__(self):
        return self.__command
    def __repr__(self):
        return self.__command.split(" ")
        
    def set_command(self, command: str) -> Command:
        return Command(command)
    
    def send(self, ignore=False) -> None:
        if self.__command == "": raise NotImplementedError()
        args: list[str] = self.__command.split(" ")
        try:
            res = subprocess.run(args, shell=True, capture_output=True)
        except CalledProcessError as e:
            raise e
        except Exception as e:
            raise e
        else:
            print(res.stdout.decode("cp932"))
            err = res.stderr.decode("cp932")
        if not ignore:
            if err != "": raise Exception(*args, err)