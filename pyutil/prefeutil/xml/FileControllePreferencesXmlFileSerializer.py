from pathlib import Path
from typing import TypedDict
from xml.etree import ElementTree
from xml.etree.ElementTree import Element

from pyutil.prefeutil.interface.PreferencesXmlFileSerializer import PreferencesXmlFileSerializer
from pyutil.xmlutil import XmlUtility

from enum import Enum, auto


class FileContrllerElemetName(Enum):
    LogOutPath = auto()
    TemporaryOutPath = auto()
    TargetDirecotryPath = auto()

    
class TargetDirecotrySubElemetName(Enum):
    Src = auto()
    Dest = auto()

class TargetDirectoryDict(TypedDict):
    src : Path
    dest : Path

class FileControllerPreferencesXmlFileSerializer(PreferencesXmlFileSerializer):
    """ファイルを取り扱うプログラムの設定ファイル
    
    下記構造を想定

    <?xml version="1.0" encoding="utf-8"?>
        <root>
        <LogOutPath>../log</LogOutPath>
        <TemporaryOutPath>../log</TemporaryOutPath>

        <TargetDirecotryPath>
            <Src>../data/src</Src>
            <Dest>../data/dest</Dest>
        </TargetDirecotryPath>

        <TargetDirecotryPath>
            <Src>../data/src</Src>
            <Dest>../data/dest</Dest>
        </TargetDirecotryPath>

        .
        .
        .
        

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
                FileContrllerElemetName.LogOutPath.name : '../log',
                FileContrllerElemetName.TemporaryOutPath.name : '../temporary',
                FileContrllerElemetName.TargetDirecotryPath.name : {
                    TargetDirecotrySubElemetName.Src.name : '../data/src',
                    TargetDirecotrySubElemetName.Dest.name : '../data/dest',
                    }
            }
        )
        xu.dump(dest)

    @property
    def log_path(self) -> Path:
        path = self.__root_element.find(FileContrllerElemetName.LogOutPath.name).text
        return Path(path)
    
    @property
    def temp_path(self) -> Path:
        path = self.__root_element.find(FileContrllerElemetName.TemporaryOutPath.name).text
        return Path(path)
    
    @property
    def process_infos(self) -> list[TargetDirectoryDict]:
        infos : list[TargetDirectoryDict] = []
        for element in self.__root_element.iter(FileContrllerElemetName.TargetDirecotryPath.name):
            src = element.find(TargetDirecotrySubElemetName.Src.name).text
            dest = element.find(TargetDirecotrySubElemetName.Dest.name).text

            infos.append(
                {
                    TargetDirecotrySubElemetName.Src.name.lower() : Path(src),
                    TargetDirecotrySubElemetName.Dest.name.lower() : Path(dest),
                }
            )
        return infos
    
