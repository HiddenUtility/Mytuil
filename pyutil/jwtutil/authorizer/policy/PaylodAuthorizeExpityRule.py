from pyutil.jwtutil.authorizer.policy.IPaylodAuthorizeRule import IPaylodAuthorizeRule
from pyutil.jwtutil.authorizer.PayloadCreator import PayloadCreator
from pyutil.jwtutil.authorizer.RequiredPayloadDictionaryKeyName import RequiredPayloadDictionaryKeyName


import pytz


from datetime import datetime


class PaylodAuthorizeExpityRule(IPaylodAuthorizeRule):
    """有効期限は問題ないか
    """
    ENCODE = PayloadCreator.ENCODE

    __is_ok : bool

    def __init__(self,
                client_payload : dict[str, str],
                timezone: str = 'Asia/Tokyo',
                ) -> None:

        now = datetime.now(pytz.timezone(timezone)).timestamp()
        timestamp = int(client_payload[RequiredPayloadDictionaryKeyName.exp.name])
        self.__is_ok = now < timestamp

    def is_ok(self) -> bool:
        """期限過ぎていない"""
        return self.__is_ok