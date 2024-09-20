import json
from pathlib import Path


class JsonDataSaver:
    """json保存中は拡張子をユニークにすることができるセーバー
    保存途中やすでにファイルがある場合は削除する。
    """
    __dummy_path : Path
    __filepath : Path
    __data : dict
    XXX = ".jsonsaving"

    def __init__(self,filepath: Path, dictionary: dict) -> None:
        self.__filepath = filepath
        self.__data = dictionary
        self.__dummy_path = filepath.with_suffix(self.XXX)

    def run(self) -> None:
        self.__dummy_path.unlink(missing_ok=True)
        self.__filepath.unlink(missing_ok=True)

        with open(self.__dummy_path, "w") as f:
            json.dump(self.__data, f)

        self.__dummy_path.rename(self.__filepath)