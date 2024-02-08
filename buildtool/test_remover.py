from buildtool.build_process import BuildProcess


from pathlib import Path
from shutil import rmtree


class TestRemover(BuildProcess):
    __dst : Path
    def __init__(self,dst=Path()):
        self.__dst = dst

    def run(self):
        targets = [d for d in self.__dst.glob("**/test") if d.is_dir()]
        list(map(rmtree, targets))
        targets = [f for f in self.__dst.glob("*.py") if "_test" in f.name.lower()]
        [f.unlink() for f in targets]