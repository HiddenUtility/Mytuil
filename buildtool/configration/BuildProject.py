from buildtool.configration.enum.MainElemetName import MainElemetName
from buildtool.configration.enum.ProjectTagElemetName import ProjectTagElemetName
from buildtool.configration.enum.ValueTagElemetName import ValueTagElemetName

from pyutil import DirectoryCreator
from pathlib import Path
from xml.etree.ElementTree import Element
from buildtool.configration.error.XmlSettingFileError import XmlSettingFileError


class BuildProject:
    """ビルドするための情報"""
    __root_element : Element
    __project_element: Element
    __pakage_name: str

    __dest_path : Path
    __log_path : Path
    __temp_path : Path
    __dirpaths : list[Path]
    __filepaths : list[Path]

    __ignore_dirnames : list[str]
    __ignore_filenames : list[str]


    def __init__(self,
                 root : Element,
                 project_element : Element,
                 ) -> None:
        
        self.__dirpaths = []
        self.__filepaths = []
        self.__ignore_dirnames = []
        self.__ignore_filenames = []

        self.__root_element = root
        self.__project_element = project_element

        self.__dest_path = Path(self.__root_element.find(MainElemetName.DestinationDirectory.name).text)

        self.__log_path = Path(self.__root_element.find(MainElemetName.LogOutPath.name).text)
        DirectoryCreator(self.log_path)

        self.__temp_path = Path(self.__root_element.find(MainElemetName.TemporaryOutPath.name).text)
        DirectoryCreator(self.temp_path)

        self.__set_project_info()


    def __set_project_info(self):
        if (pakage_name_element := self.__project_element.find(ProjectTagElemetName.PackageName.name)) is not None:
            self.__pakage_name = pakage_name_element.text
        else:
            raise XmlSettingFileError('プロジェクトのパッケージ名は必須です。')
        

        if (required_dirs_element := self.__project_element.find(ProjectTagElemetName.RequiredDirecotryPaths.name)) is not None:
            self.__dirpaths = [Path(e.text) for e in required_dirs_element.findall(ValueTagElemetName.Value.name)]
            for p in self.__dirpaths:
                if not p.is_dir():
                    raise NotADirectoryError(f'{self.__pakage_name} {p}というディレクトリは存在しません。')

        if (required_files_element := self.__project_element.find(ProjectTagElemetName.RequiredFilePaths.name)) is not None:
            self.__filepaths = [Path(e.text) for e in required_files_element.findall(ValueTagElemetName.Value.name)]
            for p in self.__filepaths:
                if not p.is_file(): 
                    raise FileNotFoundError(f'{self.__pakage_name} {p}というファイルは存在しません。')

        if (ignore_dir_element := self.__project_element.find(ProjectTagElemetName.IgnoreDirectoryName.name)) is not None:
            self.__ignore_dirnames = [e.text for e in ignore_dir_element.findall(ValueTagElemetName.Value.name)]

        if (ignore_file_element := self.__project_element.find(ProjectTagElemetName.IgnoreFileName.name)) is not None:
            self.__ignore_filenames = [e.text for e in ignore_file_element.findall(ValueTagElemetName.Value.name)]



    def __str__(self) -> str:
        deco = f'*********************ProjectName is {self.pakage_name}*************************'
        return f"""{deco}
dest : {self.dest_path}
log : {self.log_path}
temp : {self.temp_path}
dirpaths : {''.join([f'\n|---> {v}' for v in self.dirpaths])}
filepaths : {''.join([f'\n|---> {v}'for v in self.filepaths])}
ignore_dirname : {''.join([f'\n|---> {v}' for v in self.ignore_dirname])}
ignore_filename : {''.join([f'\n|---> {v}'for v in self.ignore_filename])}

{deco}"""


    @property
    def dest_path(self) -> Path:
        return self.__dest_path / self.pakage_name
    
    @property
    def log_path(self) -> Path:
        return self.__log_path

    @property
    def temp_path(self) -> Path:
        return self.__temp_path

    @property
    def pakage_name(self) -> str:
        return self.__pakage_name

    @property
    def dirpaths(self) -> list[Path]:
        return self.__dirpaths

    @property
    def filepaths(self) -> list[Path]:
        return self.__filepaths
    
    @property
    def ignore_dirname(self) -> list[str]:
        return self.__ignore_dirnames
    
    @property
    def ignore_filename(self) -> list[str]:
        return self.__ignore_filenames
    