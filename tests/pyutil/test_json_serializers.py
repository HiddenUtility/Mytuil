from pathlib import Path

from pyutil.prefeutil.json.db.DataBasePreferencesJsonFileSerializer import DataBasePreferencesJsonFileSerializer
from pyutil.prefeutil.xml.FileControllePreferencesXmlFileSerializer import FileControllerPreferencesXmlFileSerializer
from pyutil.prefeutil.xml.MultiProcessProgramPreferencesXmlFileSerializer import MultiProcessProgramPreferencesXmlFileSerializer


def test_json_serializers():
    """各jsonシリアライザーをチェックする"""
    dest = Path("../dest/test.pyutil/prefeutil")
    json_path = dest / 'test.json'
    j_serializer = DataBasePreferencesJsonFileSerializer(json_path)
    print(j_serializer.host)
    print(j_serializer.port)
    print(j_serializer.db_name)
    print(j_serializer.user_name)
    print(j_serializer.password)

    xml_path = dest / 'test_proces.xml'
    xlm_serializer = MultiProcessProgramPreferencesXmlFileSerializer(xml_path)

    print(xlm_serializer.log_path)
    print(xlm_serializer.temp_path)
    print(xlm_serializer.process_infos)
    print(xlm_serializer.get_multi_num('hoge0'))

    xml_path = dest / 'test_file.xml'
    xlm_serializer = FileControllerPreferencesXmlFileSerializer(xml_path)

    print(xlm_serializer.log_path)
    print(xlm_serializer.temp_path)
    print(xlm_serializer.process_infos)