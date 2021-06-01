# -*- coding:utf-8 -*-

"""

author      :   huangchao
fileName    :   config.py

"""


import os
import yaml


class Config():

    def __init__(self):
        pass

    # 获取项目根路径
    @classmethod
    def getRootPath(cls):
        return os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    # 配置文件路径
    @classmethod
    def configPath(cls):
        return os.path.join(Config.getRootPath(),"Config")

    # 测试数据配置路径
    @classmethod
    def testDataPath(cls):
        return os.path.join(Config.getRootPath(),"Data")

    # 图片保存路径
    @classmethod
    def imagePath(cls):
        return os.path.join(Config.getRootPath(), "Image")

    # 图片保存路径
    @classmethod
    def logPath(cls):
        return os.path.join(Config.getRootPath(), "Log")

    # 获取配置Url地址
    @classmethod
    def getUrlDict(cls) -> dict:
        urlDictPath = os.path.join(Config.getRootPath(),"Config", 'test', 'UrlConfig.yml')
        with open(urlDictPath, 'r', encoding='utf-8') as f:
            cfg = f.read()
        urlDict = yaml.load(cfg, Loader=yaml.FullLoader)
        return urlDict


config = Config()


if __name__ == '__main__':
    print(config.imagePath())


