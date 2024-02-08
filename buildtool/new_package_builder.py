from buildtool.build_process import BuildProcess


from pathlib import Path
from shutil import copy2, copytree, make_archive, rmtree


class NewPackageBuilder(BuildProcess):
    __src:Path
    __dst:Path
    __build_name :str
    __ignore_files: list[str]
    __ignore_direcotry: list[str]
    IGUNORE_DIRECTORYS =  [
        ".git",
        ".venv",
        "__pycache__",
    ]
  
    IGUNORE_FILENAMES = [
        ".gitignore",
    ]

    def __init__(self,
                 src: Path,
                 dst : Path,
                 ignore_files: list[str] = [],
                 ignore_direcotry: list[str] = [],
                 ):
        self.__src = src
        self.__dst = dst
        self.__igunore_files = ignore_files + self.IGUNORE_FILENAMES
        self.__igunore_directory = ignore_direcotry + self.IGUNORE_DIRECTORYS

    def run(self):
        if self.__dst.is_dir():
            rmtree(self.__dst)
        self.__dst.mkdir()

        paths = [p for p in self.__src.glob("*")]
        dirpaths = [d for d in paths if d.is_dir()]
        filepaths = [d for d in paths if d.is_file()]

        for path in dirpaths:
            if path.name in self.__igunore_directory: 
                continue
            copytree(path, self.__dst)

        for path in filepaths:
            if path.name in self.__igunore_files: 
                continue
            copy2(path, self.__dst / path.name)

        