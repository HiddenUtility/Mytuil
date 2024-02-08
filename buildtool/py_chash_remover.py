from buildtool.build_process import BuildProcess


from pathlib import Path
from shutil import rmtree


class PycashRemover(BuildProcess):
    __dst : Path
    def __init__(self,dst=Path()):
        self.__dst = dst

    def run(self):
        targets = [d for d in self.__dst.glob("**/__pycache__") if d.is_dir()]
        list(map(rmtree, targets))

