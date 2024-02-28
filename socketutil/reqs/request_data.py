
from __future__ import annotations
import json
from json import JSONDecodeError, JSONEncoder
from socketutil.reqs.request import Request
from typing import TypedDict, Required, NotRequired

class RequestRow(TypedDict):
  method: Required[str] # GET, POSTぐらいか

class RequestHeader(TypedDict):
  accept: NotRequired[str] 

class RequestBody(TypedDict):
  value: Required[str] 

class RequestOriginDict(TypedDict):
  request_row: Required[RequestRow]
  header: NotRequired[RequestHeader]
  body: NotRequired[RequestBody]

class RequestData(Request):
    ENCODING = "utf-8"
    ORIGIN_DICT:RequestOriginDict = {
        'request_row': { 'method' : "GET"},
        'header': {'accept':''},
        'body': {'value':''},
    }

    def __init__(self, origin:RequestOriginDict = ORIGIN_DICT, data: bytes = bytes()):
        self.__origin = origin
        self.__data = data

    def __str__(self) -> str:
        return str(self.__origin)

        
    # //@override
    def load_dict(self, origin:RequestOriginDict) -> RequestData:
        try:
            bytes_ :bytes = json.dumps(origin).encode(self.ENCODING)
            return RequestData(origin, bytes_)
        except JSONEncoder as e:
           raise e
            
    # //@override
    def load_bytes(self,data: bytes) ->  RequestData:
        try:
            origin:dict = json.loads(data.decode(self.ENCODING))
            return RequestData(origin, data)
        except JSONDecodeError as e:
           raise e


    # //@override
    def to_bytes(self) -> bytes:
        return self.__data
    
    # //@override
    def to_dict(self) -> dict:
        return self.__origin
    

    def set_test(self,) -> RequestData:
        origin = {
        'request_row': { 'method' : "GET"},
        'header': {'accept':''},
        'body': {'value':'test'},
        }
        return RequestData(
           origin=origin,
           data = self.__data
        )
    
    def set_value(self, 
                  method: str, 
                  header: dict[str, str] = {'accept':''},
                  body: dict[str, str] = {'value':''},
                  ) -> RequestData:
        origin = {
        'request_row': { 'method' : f'{method}'},
        'header': header,
        'body': body,
        }
        return RequestData(
           origin=origin,
           data = self.__data
        )

    @property
    def method(self) -> str:
       return self.__origin['request_row']['method'].upper()
    
    def is_GET(self) -> bool:
       return 'GET' == self.method
       
    def is_POST(self) -> bool:
       return 'POST' == self.method
    
    @property
    def body(self) -> dict[str, str]:
       return self.__origin['body']
    
    def is_test(self)->bool:
       return 'tset' == self.__origin['body']['value']