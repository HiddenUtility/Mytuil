# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 17:18:38 2023

@author: nanik
"""

from mylogger import MyLogger
import time

if __name__ == '__main__':
    
    logger = MyLogger()
    logger.start()
    
    loggers = {}
    for i in range(3):
        loggers[i] = MyLogger()
        

    for i in range(3):
        
        time.sleep(1)
        loggers[0].write(0,debug=True)
        time.sleep(1)
        loggers[1].write(1,debug=True)
        time.sleep(1)
        loggers[2].write(2,debug=True)
    

    for i in range(3):
        logger += loggers[i]
    logger.end()
    
    from _init import main
    main()
    