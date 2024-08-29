


from pathlib import Path
from shutil import rmtree


class PycacheRemover:
    """指定したディレクトリ内の__pycache__をすべて消す"""
    __target_dir_path : Path
    def __init__(self,target=Path()):
        self.__target_dir_path = target

    def run(self):
        targets = [d for d in self.__target_dir_path.glob("**/__pycache__") if d.is_dir()]
        list(map(rmtree, targets))

