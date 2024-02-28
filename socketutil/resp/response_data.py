
from __future__ import annotations
import json
from json import JSONDecodeError, JSONEncoder


from socketutil.resp.response import Response

from typing import TypedDict, Required, NotRequired

class RequestRow(TypedDict):
  status: Required[str]
    # 100番台「情報」
    # 200番台「成功」
    # 300番台「リダイレクト」
    # 400番台「クライアントエラー」
    # 500番台「サーバエラー」

class RequestHeader(TypedDict):
  status: NotRequired[str] 

class RequestBody(TypedDict):
  value: Required[str] 
  error: NotRequired[str] 

class ResopnseOriginDict(TypedDict):
  status_row: Required[RequestRow]
  header: NotRequired[RequestHeader]
  body: NotRequired[RequestBody]

class ResponseData(Response):
    ENCODING = "utf-8"
    ORIGIN :ResopnseOriginDict = {
        'status_row': { 'status' : '200'},
        'header': {'status':''},
        'body': {'value':''},
    }
    
    def __init__(self, origin:ResopnseOriginDict = ORIGIN, data: bytes = bytes()):
        self.__origin = origin
        self.__data = data

    def __str__(self) -> str:
        return str(self.__origin)

    # //@override
    def load_dict(self, origin:ResopnseOriginDict=ORIGIN) -> ResponseData:
        try:
            bytes_ :bytes = json.dumps(origin).encode(self.ENCODING)
            return ResponseData(origin, bytes_)
        except JSONEncoder as e:
           raise e

    # //@override
    def load_bytes(self,data: bytes) ->  ResponseData:
        try:
            origin:ResopnseOriginDict = json.loads(data.decode(self.ENCODING))
            return ResponseData(origin, data)
        except JSONDecodeError as e:
           raise e
    
        
    # //@override
    def to_bytes(self) -> bytes:
        return self.__data
    
    # //@override
    def to_dict(self) -> dict:
        return self.__origin

    def set_error(self, 
                  error_status: str | int,
                  error_value: str,
                  ) -> ResponseData:
        try:
           error_status = int(error_status)
           if not 400 <= error_status < 600:
              raise Exception()
        except:
           raise Exception('error_statusでとれる値は400,500番代です。')

        origin = {
        'status_row': { 'status' : f'{error_status}'},
        'header': {'status' : f'{error_status}'},
        'body': {
           'value':'',
           'error':f'{error_value}'
           },
        }
        return ResponseData(
           origin=origin,
           data = self.__data
        )
    
    def set_value(self, 
                  status: str, 
                  header: dict[str, str] = {'status':''},
                  body: dict[str, str] = {'value':''},
                  ) -> ResponseData:
        origin = {
        'status_row': { 'status' : f'{status}'},
        'header': header,
        'body': body,
        }
        return ResponseData(
           origin=origin,
           data = self.__data
        )
    
    def set_test(self,) -> ResponseData:
        origin = {
        'status_row': { 'status' : '200'},
        'header': '',
        'body': {'value':'test'},
        }
        return ResponseData(
           origin=origin,
           data = self.__data
        )

    
    def is_error(self) -> bool:
       status = self.__origin['status_row']['status']
       return int(status) >= 400

    def get_error_value(self) -> str:
       if self.is_error():
          return ''
       return f"{self.__origin['status_row']['status']} :: {self.__origin['body']['error']}"

    @property
    def body(self) -> dict[str, str]:
        return self.__origin['body']
    
    @property
    def body_value(self) -> str:
        return self.__origin['body']['value']
    
    def is_test(self) -> bool:
       return 'test' == self.body_value
    