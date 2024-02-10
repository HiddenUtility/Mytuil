from pyutil import *
from socketutil import *
from streamutil import *


from pyutil.filepathstream.test._test_filepathstream import TestFilepathListStream
from pyutil.hashutil.test._test_hashutil import TestHashUtil
from pyutil.mylogger.test._test_mylogger import TestMyLogger

import asyncio

if __name__ == "__main__":
    TestFilepathListStream().run()
    TestHashUtil().run()
    asyncio.run(TestMyLogger().run())


