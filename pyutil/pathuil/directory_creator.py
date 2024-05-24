from pathlib import Path


class DirecotryCreator:
    """ディレクトリを作る
    mkdir
    """
    @classmethod
    def mkdir(cls, path: Path):
        """ディレクトリを作る
        親がいなければ再回帰的に作成する。

        Args:
            path (Path): 作成したいディレクトリ

        Raises:
            Exception: 作ることができなかった場合
        """
        try:
            if not path.parent.exists():
                cls.mkdir(path.parent)
        except:
            raise Exception(f"{path}は作ることはできません。")
        path.mkdir(exist_ok=True)