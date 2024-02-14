from pyutil import *
from socketutil import *
from streamutil import *


from pyutil.filepathstream.test._test_filepathstream import TestFilepathListStream
from pyutil.hashutil.test._test_hashutil import TestHashUtil
from pyutil.mylogger.test._test_mylogger import TestMyLogger

import asyncio

class Main:
    def __init__(self) -> None:
        pass
    def run(self):
        TestFilepathListStream().run()
        TestHashUtil().run()
        asyncio.run(TestMyLogger().run())



if __name__ == "__main__":
    Main().run()

    


