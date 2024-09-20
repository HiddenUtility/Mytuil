from __future__ import annotations
from typing import override, TypedDict, Required
import asyncio
from datetime import datetime, timedelta
from pathlib import Path
from threading import Thread
from multiprocessing import Pool
from multiprocessing import Process
from traceback import print_exc, format_exc
from pandas import DataFrame
from xml.etree import ElementTree
from xml.etree.ElementTree import Element



from pyutil.logger.ProcessNumberJsonLogger import ProcessNumberJsonLogger
from pyutil.logger import *

from pyutil.prefeutil import *



from tests.pyutil.test_DirectoryTreeRemover import test_DirectoryTreeRemover
from tests.pyutil.test_SecureDictionaryJsonSerializer import test_SecureDictionaryJsonSerializer
from tests.pyutil.test_json_serializers import test_json_serializers
from tests.pyutil.test_easy_logger import test_easy_logger
from tests.pyutil.test_pyutil import test_json_logger




if __name__ == '__main__':



    # test_json_logger()
    # test_easy_logger()
    # test_json_serializers()

    # test_SecureDictionaryJsonSerializer()

    test_DirectoryTreeRemover()














    ...






