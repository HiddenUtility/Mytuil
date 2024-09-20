
from __future__ import annotations

import jwt
from jwt.exceptions import InvalidSignatureError

from pyutil.jwtutil.authorizer.policy.PaylodAuthorizePolicy import PaylodAuthorizePolicy
from pyutil.jwtutil.authorizer.PayloadCreator import PayloadCreator
from pyutil.textutil.random.RandomStringGenerator import RandomStringGenerator
from pyutil.jwtutil.HeaderDictionary import HeaderDictionary
from pyutil.jwtutil.PayLoadDictionary import PayLoadDictionary



class MyJwtAuthorizer:
    """jwtの生成や確認を行う
    - 内部的に秘密鍵もっているため,利用者はこのオブジェクトをstaticにする
    
    """
    ALGORITHMS = 'HS256'
    __secret : str
    __header: HeaderDictionary
    __days : int
    __timezone : str
    __init_payload : dict[str, str]

    def __init__(self,
                 init_payload : dict[str, str] = {},
                 days: int = 365,
                 timezone: str = 'Asia/Tokyo',
                 secret: str = 'hoge',
                 ) -> None:
        
        """jwtの生成や確認を行う
        - 内部的に秘密鍵もっているため,利用者はこのオブジェクトをstaticにする

        Args:
            init_payload (dict[str, str], optional): ペイロードに必ず含めるデータ。有効期限とタイプは自動入力するので不要。. Defaults to {}.
            days (int, optional): 有効期限. Defaults to 365.
            timezone (str, optional): タイムゾーン. Defaults to 'Asia/Tokyo'.
            secret (str, optional): 秘密鍵. Defaults to 'hoge'.
        """
        
        self.__header = {
            "alg": self.ALGORITHMS,
            "typ": "JWT"
        }
        self.__secret = secret
        self.__init_payload = init_payload
        self.__days = days
        self.__timezone = timezone
        
    
    def set_random_secret(self) -> MyJwtAuthorizer:
        """ランダムで秘密鍵をセットする。
        セキュリティ的には推奨。
        このオブジェクト自身をメモリ保持することで改ざんを防ぐ。
        Returns:
            MyJwtAuthorizer: ランダムで暗号鍵をセットする
        """

        return MyJwtAuthorizer(
            init_payload=self.__init_payload,
            days=self.__days,
            timezone=self.__timezone,
            secret=RandomStringGenerator.to_str(),            
            )
    
    def __get_current_payload(self, add_data: dict) -> dict:
        """初期と可変データを足す"""
        current = {}
        for i, v in self.__init_payload.items():
            current[i] = v
        for i, v in add_data.items():
            current[i] = v
        return current
    

    def __calcate_jwt(self, payload: dict) -> str:
        return jwt.encode(payload, self.__secret, headers=self.__header, algorithm=self.ALGORITHMS)




    def read_jwt(self, token: str) -> dict:
        """Payloadの中身を得る"""
        return jwt.decode(token, self.__secret, algorithms=self.ALGORITHMS)
    
    
    def __create_paylaod(self,
                        add_data : dict[str, str] = {},
                       ) -> dict:
        """paylaodのみ得る
        Args:
            add_data (dict[str, str], optional): ユーザーIDなど可変的な情報をPlayloadに加えたいとき. Defaults to {}.

        Returns:
            dict: payload
        """
        current_payload = self.__get_current_payload(add_data)
        return PayloadCreator(current_payload, self.__days, self.__timezone).to_dict()

    def get_jwt(self,
                 add_data : dict[str, str] = {},
                 ) -> str:
        """jwtを得る

        Args:
            add_data (dict[str, str], optional): ユーザーIDなど可変的な情報をPlayloadに加えたいとき. Defaults to {}.

        Returns:
            str: jwt_tokenを返す
        """
        return self.__calcate_jwt(self.__create_paylaod(add_data))
    
    def is_ok(self,
               token: str,
               add_data : dict[str, str] = {},
               ) -> bool:
        """認証OKかどうか

        Args:
            token (str): jwt_token
            add_data (dict[str, str], optional): ユーザーIDなど可変的な情報をPlayloadに加えたいとき. Defaults to {}.

        Returns:
            bool
        """
        try:
            client_payload: dict = self.read_jwt(token)
        except InvalidSignatureError:
            # 偽のtoken           
            return False
        except Exception as e:
            raise e

        master_payload = self.__get_current_payload(add_data)
        policy = PaylodAuthorizePolicy(client_payload, master_payload, timezone=self.__timezone)
        if not policy.is_ok():
            return False
        # 投稿されたpayloadをもとに再計算し改ざんを疑う
        return token == self.__calcate_jwt(client_payload)
