from filepathstream import *
from hashutil import *
from matplotutil import *
from mylogger import *
from myutil import *
from settingutil import *
from socketutil import *
from streamutil import *
from subprocessutil import *
from ziputil import *

from filepathstream.test._test_filepathstream import TestFilepathListStream
from hashutil.test._test_hashutil import TestHashUtil
from mylogger.test._test_mylogger import TestMyLogger

import asyncio

if __name__ == "__main__":
    TestFilepathListStream().run()
    TestHashUtil().run()
    asyncio.run(TestMyLogger().run())


