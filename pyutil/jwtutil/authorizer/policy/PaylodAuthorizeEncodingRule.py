from pyutil.jwtutil.authorizer.policy.IPaylodAuthorizeRule import IPaylodAuthorizeRule
from pyutil.jwtutil.authorizer.PayloadCreator import PayloadCreator
from pyutil.jwtutil.authorizer.RequiredPayloadDictionaryKeyName import RequiredPayloadDictionaryKeyName


class PaylodAuthorizeEncodingRule(IPaylodAuthorizeRule):
    """エンコードに問題ないか
    """
    ENCODE = PayloadCreator.ENCODE
    __is_ok : bool

    def __init__(self,
                client_payload : dict[str, str],
                ) -> None:

        unicode = str(client_payload[RequiredPayloadDictionaryKeyName.typ.name])
        self.__is_ok = self.ENCODE == unicode

    def is_ok(self) -> bool:
        """typeあっている"""
        return self.__is_ok