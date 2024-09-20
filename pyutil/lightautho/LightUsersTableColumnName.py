from enum import Enum, auto


class LightUsersTableColumnName(Enum):
    """ログイン情報とかのテーブルのカラム名"""
    username = auto()
    password = auto()
    mail_adress = auto()
    authority = auto()
    api_key = auto()
    api_uri = auto()
    api_id = auto()
    api_password = auto()