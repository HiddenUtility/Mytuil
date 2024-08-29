from enum import Enum, auto


class RequiredPayloadDictionaryKeyName(Enum):
    """必ず含めいたい情報"""
    exp = auto()
    typ = auto()