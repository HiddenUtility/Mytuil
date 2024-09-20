from pathlib import Path
from time import sleep
from traceback import format_exc
from pyutil.jsonutil.SecureDictionaryJsonSerializer import SecureDictionaryJsonSerializer
from pyutil.pathuil.directory_creator import DirectoryCreator
from pyutil.jsonutil.json_serializer import JsonSerializer
from pyutil.myerror.DetaTamperingDetectedError import DetaTamperingDetectedError


def test_SecureDictionaryJsonSerializer():
    """暗号化付きjsonシリアライザーのテスト"""

    dest = Path("../dest/test.pyutil/SecureDictionaryJsonSerializer")
    DirectoryCreator(dest,clear=True)

    serializer = SecureDictionaryJsonSerializer()

    name = 'hoge'
    body = {'hoge' : 'hoge'}

    serializer = serializer.set_body(name, body)
    assert serializer.name == name
    assert serializer.body == body

    sleep(1)


    filepath = dest / 'hoge.json'

    serializer.dump(filepath)

    sleep(1)

    new = serializer.load(filepath)
    assert new.name == name
    assert new.body == body

    # 改ざん検知
    data = JsonSerializer().read_json(filepath)
    data['body']['bad'] = 'detected'
    detected_path = dest / 'bad_data.json'
    JsonSerializer().to_json(detected_path,data)
    try:
        serializer.load(detected_path)
    except Exception as e:
        assert isinstance(e, DetaTamperingDetectedError), format_exc()
