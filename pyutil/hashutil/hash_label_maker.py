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
        """md5を発生させる。

        Args:
            data (bytes | str): ハッシュにしたい値

        Returns:
            str: 32文字列
        """
        return hashlib.md5(cls._try_parse(data)).hexdigest()
    

    @classmethod
    def get_sha256(cls, data:bytes | str) -> str:

        """sha256の文字配列を得る

        Returns:
            str: 64桁の文字列
        """
        return hashlib.sha256(cls._try_parse(data)).hexdigest()
    

    @classmethod
    def get_security(cls, name : str, password : str) -> str:
        """認証用のハッシュを発生させる

        Returns:
            str: 64桁の文字列
        """
        data = f'{name}:{password}'
        return hashlib.sha256(cls._try_parse(data)).hexdigest()
    
