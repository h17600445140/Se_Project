# -*- coding:utf-8 -*-
"""

author      :   huangchao
fileName    :   log.py

"""

import logging
import os
import datetime
from logging import handlers
from Util import config
from Util.util import singleton


@singleton
class Logger():

    def __init__(self):
        self.allLogPath = os.path.join(config.logPath(), "allLogs", "all.log")
        self.errorLogPath = os.path.join(config.logPath(), "errorLogs", "error.log")

        self.logger = logging.getLogger('WebUIAuto')
        self.logger.setLevel(logging.DEBUG)

        # 记录所有的日志
        all_handler = handlers.TimedRotatingFileHandler(self.allLogPath, when='midnight', interval=1, backupCount=7,
                                                        atTime=datetime.time(hour=0, minute=0, second=0, microsecond=0),
                                                        encoding="UTF-8")
        all_handler.setFormatter(logging.Formatter("%(levelname)s - %(asctime)s - %(message)s"))

        # 记录错误级别以上的日志
        error_handler = logging.FileHandler(self.errorLogPath, encoding="UTF-8")
        error_handler.setLevel(logging.ERROR)
        error_handler.setFormatter(
            logging.Formatter("%(levelname)s - %(asctime)s - %(pathname)s - %(filename)s[:%(lineno)d] - %(message)s"))

        # 将 handler 添加到 logger 中
        self.logger.addHandler(logging.StreamHandler())
        self.logger.addHandler(all_handler)
        self.logger.addHandler(error_handler)

    def debug(self, msg: str, *args, **kwargs):
        self.logger.debug(msg, *args, **kwargs)

    def info(self, msg: str, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)

    def warning(self, msg: str, *args, **kwargs):
        self.logger.warning(msg, *args, **kwargs)

    def error(self, msg: str, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)

    def critical(self, msg: str, *args, **kwargs):
        self.logger.critical(msg, *args, **kwargs)

logger = Logger()

if __name__ == '__main__':
    # logger1 = Logger()
    # logger.debug("测试debug")
    # logger.info("测试info")
    # logger.warning("测试warning")
    # logger.error("测试error")
    # logger.critical("测试critical")
    pass


