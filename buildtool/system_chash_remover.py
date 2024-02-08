from buildtool.build_process import BuildProcess


from pathlib import Path
from shutil import rmtree


class SystemChashRemover(BuildProcess):
    __dst : Path
    def __init__(self, 
                 dst: Path,
                 selfinitialize_dirnames: list[str]
                 ):
        self.__dst = dst
        self.__initialize_dirnames = selfinitialize_dirnames

    def run(self):
        for dirname in self.__initialize_dirnames:
            target = self.__dst / dirname
            if target.is_dir():
                rmtree(target)
            target.mkdir()