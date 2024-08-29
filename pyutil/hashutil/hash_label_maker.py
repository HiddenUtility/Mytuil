from __future__ import annotations

from pathlib import Path
import hashlib



class HashLableMaker:
    """文字列まはたバイト配列、ファイルからhash値のstringを得る"""
    @staticmethod
    def __try_parse(data:bytes | str) -> bytes:
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
        return hashlib.md5(cls.__try_parse(data)).hexdigest()
    

    @classmethod
    def get_sha256(cls, data:bytes | str) -> str:

        """sha256の文字配列を得る

        Returns:
            str: 64桁のSHA256のハッシュ
        """
        return hashlib.sha256(cls.__try_parse(data)).hexdigest()
    

    @classmethod
    def get_security(cls, name : str, password : str) -> str:
        """認証用のハッシュを発生させる

        Returns:
            str: 64桁のSHA256のハッシュ
        """
        data = f'{name}:{password}'
        return hashlib.sha256(cls.__try_parse(data)).hexdigest()
    
    @classmethod
    def get_file_hash(cls, filepath: str | Path) -> str:
        """ファイルのハッシュ値を得る

        Args:
            filepath (str | Path): ファイルパス

        Raises:
            FileNotFoundError: 存在しない

        Returns:
            str: SHA256のハッシュ
        """
        filepath = Path(filepath)
        if not filepath.exists():
            raise FileNotFoundError(f"{filepath}は存在しません。")
        with open(filepath, "rb") as data:
            return cls.get_sha256(data.read())
    

