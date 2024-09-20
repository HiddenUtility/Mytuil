from pyutil.logger import EasyLogger


from pathlib import Path
from time import sleep


def test_easy_logger():
    dest = Path("../dest/test.pyutil/logger")


    for i in range(10):
        logger = EasyLogger(dest=dest, name='EasyLogger')
        logger.start()
        logger.write(f'{i}回目')
        logger.end()

        sleep(1)