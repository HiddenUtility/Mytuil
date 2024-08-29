from pyutil.jwtutil.PayLoadDictionary import PayLoadDictionary


import pytz


from datetime import datetime, timedelta


from pyutil.jwtutil.authorizer.RequiredPayloadDictionaryKeyName import RequiredPayloadDictionaryKeyName


class PayloadCreator:
    """ペイロードを作成する"""
    __exp: datetime
    __data : dict[str, str]
    ENCODE = 'utf-8'


    def __init__(self,
                 data : dict[str, str] = {},
                 days: int = 365,
                 timezone: str = 'Asia/Tokyo',
                 ) -> None:
        """ペイロードを作成する

        Args:
            data (dict[str, str]): ユーザーIDとかパスワードとかペイロードに含めたいデータ。有効期限とタイプは自動入力するので不要。
            days (int, optional): 有効期限. Defaults to 365.
            timezone (str, optional): タイムゾーン. Defaults to 'Asia/Tokyo'.
        """
        self.__exp = datetime.now(pytz.timezone(timezone)) + timedelta(days=days)
        self.__data = data


    def to_dict(self) -> PayLoadDictionary:

        payload :PayLoadDictionary = {
            RequiredPayloadDictionaryKeyName.exp.name : int(self.__exp.timestamp()),
            RequiredPayloadDictionaryKeyName.typ.name : self.ENCODE,
        }
        for k,v in self.__data.items():
            payload[k] = v
        return payload
    
