import hashlib


class HashLableMaker:
    @staticmethod
    def _try_parse(data:bytes | str) -> bytes:
        if isinstance(data, str):
            data = data.encode()
        if not isinstance(data, bytes):raise TypeError()
        return data

    @classmethod
    def get_md5(cls, data:bytes | str) -> str:
        return hashlib.md5(cls._try_parse(data)).hexdigest()

    @classmethod
    def get_sha256(cls, data:bytes | str) -> str:
        return hashlib.sha256(cls._try_parse(data)).hexdigest()