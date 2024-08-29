# サンプルコード

## DataBasePreferencesJsonFileSerializer

```py
from pyutil import *

if __name__ == '__main__':
    dest = Path("../dest/test.pyutil")
    json_path = dest / 'test.json'
    j_serializer = DataBasePreferencesJsonFileSerializer(json_path)
    print(j_serializer.host)
    print(j_serializer.port)
    print(j_serializer.db_name)
    print(j_serializer.user_name)
    print(j_serializer.password)

  # print結果
  # localhost
  # 5432
  # postgres
  # postgres
  # postgres
```
デフォ出力
```json

{
     "host": "localhost",
     "port": 5432,
     "dbname": "postgres",
     "username": "postgres",
     "password": "postgres"
}

```

## MultiProcessProgramPreferencesXmlFileSerializer

```py
from pyutil import *

if __name__ == '__main__':

    dest = Path("../dest/test.pyutil")
    xml_path = dest / 'test.xml'
    xlm_serializer = MultiProcessProgramPreferencesXmlFileSerializer(xml_path)
    print(xlm_serializer.log_path)
    print(xlm_serializer.temp_path)
    print(xlm_serializer.process_infos)
    print(xlm_serializer.get_multi_num('hoge0'))

    # print結果
    # ..\log
    # ..\log
    # [{'TaskName': 'hoge0', 'MultiNumber': 4}]
    # 4
```
デフォ出力
```xml
<?xml version="1.0" encoding="utf-8"?>
<root>
  <LogOutPath>../log</LogOutPath>
  <TemporaryOutPath>../log</TemporaryOutPath>
  <Process>
    <TaskName>hoge0</TaskName>
    <MultiNumber>4</MultiNumber>
  </Process>
</root>


```


