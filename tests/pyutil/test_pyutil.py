

from pathlib import Path
from time import sleep

from pyutil.jsonutil.ProcessNumberJsonLogger import ProcessNumberJsonLogger



def test_json_logger():
    dest = Path("../dest/test.pyutil/json_logger")

    dest.unlink(missing_ok=True)


    for i in range(10):
        logger = ProcessNumberJsonLogger(dest, 'hoge')
        logger.add(i)
        print(f'{i}回目')

        sleep(1)
    
    logger = ProcessNumberJsonLogger(dest, 'hoge')
    
    assert logger.get_all_process_number() == 10



