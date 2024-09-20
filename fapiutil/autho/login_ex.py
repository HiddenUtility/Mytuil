#!/usr/bin/python
# -*- coding: utf-8 -*-
"""jwt_reader.py

Explain : ヘッダーのAuthorazition読んで認証通す例
使い方はこのモジュールコピペして、用意した認証器を埋め込んで各エンドポイントへ依存させればOK
認証部分は各自用意して改造してね

test部はtestsに書いてるのでそっちみて
          
Create  : 2024-09-12(木): H.U
          
Todo    : 
          
"""
from traceback import print_exc

from fastapi import HTTPException, Security
from fastapi.responses import JSONResponse
from fastapi.security.api_key import APIKeyHeader
from fastapi import Depends, FastAPI, Request
from enum import Enum, auto
from starlette.middleware.cors import CORSMiddleware

# //複雑なやつ作りたければ下記のクラスを参考にして自分で作ってね
from pyutil.hashutil.hash_label_maker import HashLableMaker
from pyutil.lightautho.LightAuthorizeError import LightAuthorizeError
from pyutil.lightautho.LightLakeAutholizer import LightLakeAutholizer
from pyutil.lightautho.SampleLoginQueryParameter import SampleLoginQueryParameter 


app = FastAPI()

# CORSを回避するために追加
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,   # 追記により追加
    allow_methods=["*"],      # 追記により追加
    allow_headers=["*"]       # 追記により追加
)

class FastApiHeaderAuthorizationName(Enum):
    """ヘッダーの名前"""
    Authorization = auto()


class JsonResponseKeyName(Enum):
    """レスポンスデータでよく使うkey名"""
    jwt = auto()
    ver = auto()
    pid = auto()
    detail = auto()


def read_login_user_secret(
                    user : str = '',
                    secret : str = '',
    ) -> SampleLoginQueryParameter:
    """依存性注入用。クエリパラメータからログイン情報を読み取る
    
    """
    return SampleLoginQueryParameter(
        user=user,
        secret=secret
    )


class SampleAuthoraizer:
    """サンプルのオーソライザー
    - サンプルはuser名とパスワードのみのLightLakeAutholizerを使っている
    - ほかにpayload欲しければ自分でLightLakeAutholizer参考にAuthoraizerを作ってね

    """
    __user = 'user'
    __secret = HashLableMaker.get_security(__user, 'password')
    __your_login_data = {__user:__secret}
    AOUTHO = LightLakeAutholizer(__your_login_data)


@app.get('/login')
def get_dlt_login(request:Request, params : SampleLoginQueryParameter = Depends(read_login_user_secret)
                       ):
    """ユーザー名とパスワードのログイン認証の例
    """

    #本番なら　asyncioにしてlogger仕掛ける
    print(f'{request.client.host}:{request.client.port}')

    try:
        # /////////////////認証は別で自分で作ってね///////////////////////////
        jwt = SampleAuthoraizer.AOUTHO.login(params.user, params.secret)
        # /////////////////認証は別で自分で作ってね///////////////////////////
    except LightAuthorizeError:
        raise HTTPException(status_code=401)
    except Exception:
        print_exc()
        raise HTTPException(status_code=500)

    return JSONResponse(
        status_code=200,
        headers=None,
        media_type=None,
        content= {
            JsonResponseKeyName.ver.name: "自分で定義してね",
            JsonResponseKeyName.jwt.name: jwt,
            }

    )


class FastApiHeaderAuthorizationJsonWebTokenReader:
    """ヘッダーよりAuthorization情報を読み取り認証する。
    - 基本的にはログイン情報は各アプリ依存なのでこのクラスをコピペして改造して使う
    - Authorazarは自分で別途設計して用意する
    - fastapi.Dependsをつかって依存性を注入することで、ルーティング後のメイン処理に入る前に認証を行える

    """
    AUTHORIZATION_KEY_NAME = FastApiHeaderAuthorizationName.Authorization.name
    __header_key = APIKeyHeader(name=AUTHORIZATION_KEY_NAME, auto_error=False)

    @staticmethod
    def authoraize_jwt(authorization: str = Security(__header_key)) -> str:
        """ヘッダーよりjwtを取り出す
        - このstaticメンバーを依存性を注入する

        Args:
            authorization (str, optional): _description_. Defaults to Security(__api_key_header).

        Returns:
            str: _description_
        """
        if not authorization:
            print('Authorizationヘッダーがない。')
            raise HTTPException(status_code=400 , detail="Authorizationヘッダーが必要です。")

        parts = authorization.split()
        if len(parts) == 1:
            jwt = parts[0]
        elif len(parts) == 2 and parts[0].lower() == "bearer":
            jwt = parts[1]
        else:
            raise HTTPException(status_code=401)

        # /////////////////認証部分は別で自分で作ってね///////////////////////////
        new_jwt = SampleAuthoraizer.AOUTHO.login_from_jwt(jwt)
        return new_jwt
        # /////////////////認証は別で自分で作ってね///////////////////////////


@app.get('/login/jwt')
def get_login_jwt(request:Request, new_jwt : str = Depends(FastApiHeaderAuthorizationJsonWebTokenReader.authoraize_jwt)
                       ) -> JSONResponse:
    """jwtによるユーザー認証の例
    - こいつをベース(コピペ)にしていろいろなエンドポイントを複製すればOK

    Args:
        request (Request): リクエスト
        jwt (str, optional): 新しいjwt. Defaults to Depends(UploaderApiKeyHeaderReader.authoraize_jwt).

    Returns:
        JSONResponse: レスポンス
    """

    #本番なら　asyncioにしてlogger仕掛ける
    print(f'{request.client.host}:{request.client.port}')

    # // 本番ならここに処理を書く
    #
    #
    #
    #
    # // 本番ならここに処理を書く

    return JSONResponse(
        status_code=200,
        headers=None,
        media_type=None,
        content= {
            JsonResponseKeyName.ver.name: "自分で定義してね",
            JsonResponseKeyName.jwt.name: new_jwt,
            }

    )
