# サンプルコード
```py
from pyutil import *
    dest = Path("../dest/test.XmlUtility/test.xml")
    xu =  XmlUtility()

    xu = xu.load_dict(
        {
            'LogOutPath' : '../log',
            'TemporaryOutPath' : '../log',
        }
    )

    xu = xu.load_dict(
        {
            'Process' : {
                'TaskName' : 'hoge0',
                'MultiNumber' : '4',
                
                }
        }
    )

    xu = xu.load_dict(
        {
            'Process' : {
                'TaskName' : 'hoge1',
                'MultiNumber' : '4',
                
                }
        }
    )


    xu.dump(dest)

```

上記を事項すると下記のxmlファイルが得られる

```xml
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
```