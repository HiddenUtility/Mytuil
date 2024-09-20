from enum import Enum, auto


class MainElemetName(Enum):
    """1階層目のエレメント"""
    DestinationDirectory = auto()
    LogOutPath = auto()
    TemporaryOutPath = auto()
    Project = auto()