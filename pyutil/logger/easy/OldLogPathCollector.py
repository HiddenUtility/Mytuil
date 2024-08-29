from pathlib import Path


class OldLogPathCollector:
    """ログファイルを調べる"""
    __target: Path
    __name : str
    def __init__(self,
                    target: Path,
                    base_name,
                    ) -> None:
        """ログファイルを調べる

        Args:
            target (Path): ログが出力されているところ
            base_name (_type_): ベース名
        """
        self.__target = target
        self.__name = base_name

    def exists(self) -> bool:
        """過去あるかどうか"""
        fs = self.get_log_paths()
        if fs: return True
        return False

    def get_log_paths(self) -> list[Path]:
        return [f for f in self.__target.glob('*.log') if f.is_file() and self.__name in f.stem]

    def get_final_log_path(self) -> Path:
        fs = self.get_log_paths()
        if not fs:
            raise FileNotFoundError('先にexistsで調べましょう')
        return fs[-1]