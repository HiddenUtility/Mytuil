from pathlib import Path


class DirecotryCreator:
    @classmethod
    def mkdir(cls, path: Path):
        try:
            if not path.parent.exists():cls.mkdir(path.parent)
        except:
            raise Exception(f"{path}は作ることはできません。")
        path.mkdir(exist_ok=True)