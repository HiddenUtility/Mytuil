from buildtool.build_process import BuildProcess
from buildtool.config import Configuration
from buildtool.new_package_builder import NewPackageBuilder
from buildtool.py_chash_remover import PycashRemover
from buildtool.system_chash_remover import SystemChashRemover
from buildtool.test_remover import TestRemover

from pathlib import Path
from shutil import make_archive


class BuildTool(BuildProcess):
    RELEASE = Configuration.RELEASE
    __src:Path
    __dst:Path
    __processes:list[type[BuildProcess]]
    __ignore_files: list[str]
    __ignore_direcotry: list[str]
    __initialize_dirnames: list[str]
    __out_zip : bool
    def __init__(self,
                 src: Path = Path().cwd(),
                 dst : Path = Path(RELEASE),
                 build_name = "v1000",
                 ignore_files: list[str] = [],
                 ignore_direcotry: list[str] = [],
                 initialize_dirnames: list[str] = [],
                 out_zip = False,
                 ):
        if not dst.parent.exists(): 
            raise NotADirectoryError()
        dst.mkdir(exist_ok=True)
        self.__src = src
        self.__dst = dst / build_name
        self.__ignore_files = ignore_files
        self.__ignore_direcotry = ignore_direcotry 
        self.__initialize_dirnames = initialize_dirnames
        self.__out_zip = out_zip

        self.__processes:list[type[BuildProcess]] = [
            NewPackageBuilder(
                self.__src,
                self.__dst,
                self.__ignore_files,
                self.__ignore_direcotry
                ),
            PycashRemover(self.__src),
            TestRemover(self.__dst),
            SystemChashRemover(self.__dst, self.__initialize_dirnames),
            ]
        if self.__out_zip:
            make_archive(self.__dst , "zip" , self.__dst)

    def run(self):
        for process in self.__processes:
            process.run()