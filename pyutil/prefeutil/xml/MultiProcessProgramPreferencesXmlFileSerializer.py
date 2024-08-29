from pathlib import Path
from typing import TypedDict
from xml.etree import ElementTree
from xml.etree.ElementTree import Element

from pyutil.prefeutil.interface.PreferencesXmlFileSerializer import PreferencesXmlFileSerializer
from pyutil.xmlutil import XmlUtility

from enum import Enum, auto


class MultiProcessProgramPreferencesXmlElemetName(Enum):
    LogOutPath = auto()
    TemporaryOutPath = auto()
    Process = auto()
    
class MultiProcessProgramPreferencesXmlProcessSubElemetName(Enum):
    TaskName = auto()
    MultiNumber = auto()

class ProcessDict(TypedDict):
    TaskName : str
    MultiNumber: int

class MultiProcessProgramPreferencesXmlFileSerializer(PreferencesXmlFileSerializer):
    """マルチプロセスを有するプログラムの設定ファイル
    
    下記構造を想定

    <?xml version="1.0" encoding="utf-8"?>
    <root>
    <LogOutPath>../log</LogOutPath>
    <TemporaryOutPath>../log</TemporaryOutPath>
    <Process>
        <TaskName>hoge0</TaskName>
        <MultiNumber>4</MultiNumber>
    </Process>
    <Process>
        <TaskName>hoge2</TaskName>
        <MultiNumber>4</MultiNumber>
    </Process>
    </root>
        
    """

    __root_element : Element
    def __init__(self, path : str | Path, exixts_error=False) -> None:

        self.__src = Path(path)
        if not self.__src.exists():
            if exixts_error:
                raise FileNotFoundError(f'{self.__src}がありません。')
            else:
                self.__dump(self.__src)
        self.__root_element = ElementTree.parse(self.__src).getroot()

    def __dump(self, dest: Path):
        xu = XmlUtility().load_dict(
            {
                MultiProcessProgramPreferencesXmlElemetName.LogOutPath.name : '../log',
                MultiProcessProgramPreferencesXmlElemetName.TemporaryOutPath.name : '../log',
                MultiProcessProgramPreferencesXmlElemetName.Process.name : {
                    MultiProcessProgramPreferencesXmlProcessSubElemetName.TaskName.name : 'hoge0',
                    MultiProcessProgramPreferencesXmlProcessSubElemetName.MultiNumber.name : '4',
                    }
            }
        )
        xu.dump(dest)

    @property
    def log_path(self) -> Path:
        path = self.__root_element.find(MultiProcessProgramPreferencesXmlElemetName.LogOutPath.name).text
        return Path(path)
    
    @property
    def temp_path(self) -> Path:
        path = self.__root_element.find(MultiProcessProgramPreferencesXmlElemetName.TemporaryOutPath.name).text
        return Path(path)
    
    @property
    def process_infos(self) -> list[ProcessDict]:
        infos : list[ProcessDict] = []
        for element in self.__root_element.iter(MultiProcessProgramPreferencesXmlElemetName.Process.name):
            task_name = element.find(MultiProcessProgramPreferencesXmlProcessSubElemetName.TaskName.name).text
            multi = element.find(MultiProcessProgramPreferencesXmlProcessSubElemetName.MultiNumber.name).text

            infos.append(
                {
                    MultiProcessProgramPreferencesXmlProcessSubElemetName.TaskName.name : task_name,
                    MultiProcessProgramPreferencesXmlProcessSubElemetName.MultiNumber.name : int(multi),
                }
            )
        return infos
    
    def get_multi_num(self, process_name: str) -> int:
        """プロセスの並列数の設定値を得る

        Args:
            process_name (str): TaskNameタグで定義した名前

        Raises:
            KeyError: xmlに存在しないtask名

        Returns:
            int: 値をそのまま返す
        """
        for element in self.__root_element.iter(MultiProcessProgramPreferencesXmlElemetName.Process.name):
            task_name = element.find(MultiProcessProgramPreferencesXmlProcessSubElemetName.TaskName.name).text
            multi = element.find(MultiProcessProgramPreferencesXmlProcessSubElemetName.MultiNumber.name).text
            if process_name == task_name:
                return int(multi)
        raise KeyError(f'{process_name}は存在しません。')
        



        



