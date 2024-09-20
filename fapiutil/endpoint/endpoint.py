#!/usr/bin/python
# -*- coding: utf-8 -*-
"""endpoint.py

Explain : 依存性を注入したエンドポイント

共通化したいやつは依存性を注入してしばる
もちろん共通化したい＝同じ系統という原則は忘れないで
          
Create  : 2024-09-12(木): H.U
          
Todo    : 
          
"""



from fastapi import Depends, FastAPI, Request
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

from fastapi.responses import JSONResponse


app = FastAPI()


# CORSを回避するために追加
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,   # 追記により追加
    allow_methods=["*"],      # 追記により追加
    allow_headers=["*"]       # 追記により追加
)
    
class MyQueryParameter(BaseModel):
    """定義できる"""
    user_id: str
    secret: str

def get_login_info(user: str="", secret:str="") -> MyQueryParameter:
    """クエリパラメータから分解する
    - kwargsにすることでクエリパラメータから値を抜くことができる
    - エンドポイントおよびパラメータを解析してその結果を返してあげる
    - 例ではBaseModelを返しているが、別になんでもいい
    - 色々したいならクラス設計したほうがいいかな
    """
    return MyQueryParameter(
        user_id=user,
        secret=secret,
    )


@app.get("/{args}",response_model=dict)
def get_home(request:Request, args: str, params: MyQueryParameter = Depends(get_login_info)):
    """_summary_

    Args:
        request (Request): httpリクエストの情報をバラス便利なオブジェクト
        params (QueryParameter, optional): Depends辞書返すのでBaseModelにぶち込めばパラメータ風に取り出せる. Defaults to Depends().
    """

    print(f'{request.client.host}:{request.client.port}')
    
    request.query_params # クエリパラメータはこれから抜ける
    request.path_params
    request.headers # ヘッダー情報
    request.body() # body bytes

    return JSONResponse(
        status_code=200,
        headers=None,
        media_type=None,
        content= {'mesage': 'Hello FastApi'}
    )