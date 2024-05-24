import base64
import hmac
import json
import hashlib


from pyutil.jwtutil.HeaderInformation import HeaderInformation
from pyutil.jwtutil.PayLoad import PayLoad


class MyJsonWebToken:
    __header : HeaderInformation
    __secret : str
    def __init__(self,
                 secret: str = '',
                  
                 ) -> None:
        """JWT生成の勉強用

        Args:
            payload (dict[str, str]): ユーザー情報などが一般的。基本的にデコードされるのでパスワードは含んではいけない
            secret (str): 環境変数などに入れてバックのみの秘密にすると良い
        """
        self.__header = {
            "alg": "HS256",
            "typ": "JWT"
        }
        self.__secret = secret

        
    def __base64_encode(self, data : bytes) -> bytes:
        return base64.urlsafe_b64encode(data).rstrip(b'=')

    def __to_signature(self, base64_header : bytes, base64_paylaod : bytes) -> bytes:
        """秘密鍵でハッシュ化(署名化)し、base64でエンコードする。

        Args:
            base64_header (bytes): _description_
            base64_paylaod (bytes): _description_

        Returns:
            bytes: base64エンコードした署名
        """
        signature : bytes = hmac.new(
            self.__secret.encode(),
            msg=f'{base64_header.decode()}.{base64_paylaod.decode()}'.encode(),
            digestmod=hashlib.sha256
        ).digest()
        signature_base64_encoded : bytes = self.__base64_encode(signature)
        return signature_base64_encoded
    
    def generate(self, paylaod: PayLoad) -> str:
        """トークン生成
        ヘッダを生成
        ペイロードを生成
        署名を生成する
        以上の3つをドット(.)で連結して完成
        Returns:
            str: jwtをリターン
        """
        # ヘッダーとペイロードをbase64でエンコードする。
        header_json : str = json.dumps(self.__header)
        header_encoded : bytes = self.__base64_encode(header_json.encode())
        payload_json : str = json.dumps(paylaod)
        payload_encoded : bytes = self.__base64_encode(payload_json.encode())
        # 秘密鍵でハッシュ化(署名化)し、base64でエンコードする。
        signature_encoded : bytes = self.__to_signature(header_encoded, payload_encoded)
        # jwtの仕様は　{ヘッダー}.{ペイロード}.{ハッシュ値}
        jwt = f'{header_encoded.decode()}.{payload_encoded.decode()}.{signature_encoded.decode()}'
        return jwt
    
    def is_ok(self, client_jwt: str) -> bool:
        """承認のアルゴ。送られてきたヘッダーとpayloadを使って署名を再計算し一致すればOK
        ヘッダを検証する
        署名を検証する
        (ペイロードを検証する) 
        Args:
            jwt (str): クライアントサイドからきたjwt

        Returns:
            bool: 認証成功
        """
        parts = client_jwt.split('.')
        client_header = parts[0]
        client_payload = parts[1]
        client_signature = parts[2]
        # ヘッダーを検証して一致するか。typ,kid, algをチェック。
        ...
        # payloadを検証する。有効期限とかもろもろチェック
        ...
        # 再計算結果と提出された署名が一致するかチェック
        signature_base64_encoded : bytes= self.__to_signature(client_header.encode(), client_payload.encode())
        return  signature_base64_encoded.decode() == client_signature
    

def main():
    secret = 'secret-key'  # 秘密鍵。環境変数等から引いてくるなどpushしないように注意する。

    # ログイン情報が送られてくる。正しければpayloadを生成する。
    payload : PayLoad = {'user_id': 'value'}  # ユーザー情報,アルゴリズムなどが一般的。本番なら普通にクラスで定義する。

    # 秘密鍵を使ってトークンの生成、クライアントサイドへリターンする。
    token = MyJsonWebToken(secret).generate(payload)
    print(token)

    #トークンの検証
    verification = MyJsonWebToken(secret)
    print(verification.is_ok(token))
    

if __name__ == '__main__':
    main()
