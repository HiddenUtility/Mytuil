from time import sleep
from mylogger.mylogger import MyLogger


class TestMyLogger:
    def __init__(self) -> None:
        pass
    
    def run(self):
        logger = MyLogger()
        logger.start()
        
        loggers = {}
        for i in range(3):
            loggers[i] = MyLogger()
            
        for i in range(3):
            sleep(1)
            loggers[0].write(0,debug=True)
            sleep(1)
            loggers[1].write(1,debug=True)
            sleep(1)
            loggers[2].write(2,debug=True)
        
        for i in range(3):
            logger += loggers[i]
        logger.end()