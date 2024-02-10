# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 22:21:11 2023

@author: nanik
"""

import time
from threading import Thread

class Process:
    def __init__(self,arg: any):
        self.arg = arg
        self.status = "waiting"
        
    def start(self):
        print("開始します。")
        self.status = "running"
        while self.status == "running":
            #何かしらの処理
            print(f"{self.arg}を耕します。")
            
            time.sleep(10)
        print("停止しました。")
        self.status = "waiting"
        
    def stop(self):
        self.status = "stop"
        
    def config(self):
        print(self.status)
        
class Controller:
    def __init__(self):
        
        self.threads = {}
        self.processes = {}
    
    def _has_objs(self):
        return len(self.processes) > 0
    
    def set_args(self,args: str):
        args = args.split(" ")
        for arg in args:
            process = Process(arg)
            self.processes[arg] = process
            self.threads[arg] = Thread(target=self.processes[arg].start)
    
    def start(self):
        if not self._has_objs():
            print("開始するプロジェクトがありません。")
            return
        for arg in self.processes:
            if self.processes[arg].status == "waiting":
                self.threads[arg].start()
                
    def stop(self):
        if not self._has_objs():
            print("終了するプロジェクトがありません。")
            return
        for arg in self.processes:
            if self.processes[arg].status == "running":
                self.processes[arg].stop()
                
    def config(self):
        if not self._has_objs():
            print("プロジェクトがありません。")
            return
        for arg in self.processes:
            print(self.processes[arg].status)

                

        
class CUI:
    def __init__(self):
        
        
        self.controller = Controller()
        
    def __help(self):
        print(
            """
#################################
const: 
start:
stop:
config:
end:
#################################
            """
            )
        
        
    
    def run(self):
        
        while True:
            request = input("input>")
            match request:
                case "const":
                    self.controller.set_args(input("    input args>>"))
                case "start":
                    self.controller.start()
                case "stop":
                    self.controller.stop()
                case "config":
                    self.controller.config()
                case "help":
                    self.__help()
                case "end":
                    break
                case _:
                    print(f"{request}　は無効です。")
        
        
        
if __name__ == "__main__":
    
    cui = CUI()
    cui.run()