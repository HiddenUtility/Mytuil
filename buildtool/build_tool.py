from buildtool.build_process import BuildProcess
from buildtool.new_package_builder import NewPackageBuilder
from buildtool.py_chash_remover import PycashRemover
from buildtool.system_chash_remover import SystemChashRemover
from buildtool.test_remover import TestRemover


from pathlib import Path


class BuildTool(BuildProcess):
    __src:Path
    __dst:Path
    __processes:list[type[BuildProcess]]
    def __init__(self,
                 src: Path,
                 dst : Path,
                 build_name = "buildtool1000",
                 ignore_files: list[str] = [],
                 ignore_direcotry: list[str] = [],
                 initialize_dirnames: list[str] = [],
                 ):
        if not dst.exists(): raise NotADirectoryError()
        self.__src = src
        self.__dst = dst
        self.__build_name = build_name
        self.__ignore_files = ignore_files
        self.__ignore_direcotry = ignore_direcotry 
        self.__initialize_dirnames = initialize_dirnames

        self.__processes:list[type[BuildProcess]] = [
            NewPackageBuilder(
                self.__src,
                self.__dst,
                self.__build_name,
                self.__ignore_files,
                self.__ignore_direcotry
                ),
            PycashRemover(self.__dst),
            TestRemover(self.__dst),
            SystemChashRemover(self.__dst, self.__initialize_dirnames),
            ]

    def run(self):
        for process in self.__processes:
            process.run()