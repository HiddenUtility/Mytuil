

import re

class WindowsAvailablePathName:
    """WindowsPathで使用可能な文字に変換する"""
    __name : str
    def __init__(self,text: str, replase_text = '-'):
        """WindowsPathで使用可能な文字に変換する"""
        self.__name =  re.sub(r'[\\|/|:|?|.|"|<|>|\|]', replase_text, text)

    @property
    def value(self):
        return self.__name
    
