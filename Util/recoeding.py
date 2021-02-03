# -*- coding:utf-8 -*-
"""

author      :   huangchao
fileName    :   recoeding.py

"""

import json
import os

from Util import config, logger


class Recording(object):

    def __init__(self):
        pass

    # 获取 record.json 文件目录
    @property
    def _getRecordingPath(self):
        return os.path.join(config.testDataPath(), 'localMemory', 'record.json')

    # 写入记录文件
    def writeDataToRecord(self, dict, type='boeData'):
        with open(self._getRecordingPath, "r", encoding="UTF-8") as f:
            rData = json.load(f)
        logger.info('{} 的值为：{}'.format(type, rData.get(type)))
        if rData.get(type) == None:
            rData.update({type:{}})
        rData[type].update(dict)
        data = rData
        with open(self._getRecordingPath, "w", encoding="UTF-8") as f:
            json.dump(data, f)
        logger.debug('记录文件信息, 文件信息为 -> {} : {}'.format(type, dict))

    # 读取记录文件
    def readDataFromRecord(self, type='boeData'):
        with open(self._getRecordingPath, "r", encoding="UTF-8") as f:
            rData = json.load(f)
        return rData.get(type)


record = Recording()

if __name__ == '__main__':
    print(record.writeDataToRecord())