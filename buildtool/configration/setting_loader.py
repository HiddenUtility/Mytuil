from pathlib import Path
from xml.etree import ElementTree
from xml.etree.ElementTree import Element


from pyutil import DirectoryCreator
from buildtool.configration.BuildProject import BuildProject
from buildtool.configration.enum.MainElemetName import MainElemetName
from buildtool.configration.default_xml import default_xml


class SettingLoader:
    """ファイルを取り扱うプログラムの設定ファイル
    """

    __root_element : Element
    __pjts : list[BuildProject]
    def __init__(self,
                  path : str | Path = Path('./buildtool/settings/setting.xml'), 
                  exixts_error=False,
                  ) -> None:

        self.__src = Path(path)
        if not self.__src.exists():
            if exixts_error:
                raise FileNotFoundError(f'{self.__src}がありません。')
            else:
                self.__dump(self.__src)
        self.__root_element = ElementTree.parse(self.__src).getroot()
        self.__pjts  = [
            BuildProject(self.__root_element, e) for e in self.__root_element.iter(MainElemetName.Project.name)
        ]

    def clear_dest(self):
        """出力先を初期化する。"""

        DirectoryCreator(self.dest_path, clear=True)
        DirectoryCreator(self.log_path)
        DirectoryCreator(self.temp_path)



    def __dump(self, dest: Path):
        """ない場合はデフォを作成する"""
        with open(dest, "w", encoding='utf-8') as fs:
            fs.writelines(default_xml)

    def clear_setting_file(self):
        """初期化する。"""
        self.__src.unlink()
        self.__dump()
        
    def to_pjts(self) -> list[BuildProject]:
        return self.__pjts
    

    @property
    def dest_path(self) -> Path:
        path = self.__root_element.find(MainElemetName.DestinationDirectory.name).text
        return Path(path)

    @property
    def log_path(self) -> Path:
        path = self.__root_element.find(MainElemetName.LogOutPath.name).text
        return Path(path)

    @property
    def temp_path(self) -> Path:
        path = self.__root_element.find(MainElemetName.TemporaryOutPath.name).text
        return Path(path)
    
