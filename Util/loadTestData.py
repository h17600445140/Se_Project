# -*- coding:utf-8 -*-
"""

author      :   huangchao
fileName    :   loadTestData.py

"""

import json
import os

import yaml

from Util import config


class LoadTestData():

    def __init__(self):
        pass

    # ---------- 一层目录 ----------

    # 获取 data_path
    def get_datapath(self, path : str) -> str:
        a = path.split('Testcases')
        b = a[1].split('Test')
        data_path = a[0] + 'Data' + b[0] + 'Data' + b[0] + 'Data.json'
        return data_path

    def get_ymldatapath(self, path : str) -> str:
        a = path.split('Testcases')
        b = a[1].split('Test')
        data_path = a[0] + 'Data' + b[0] + 'Data' + b[0] + 'Data.yml'
        return data_path

    # ---------- 加载通用数据目录 ----------

    def getDataOath(self, path, dataType):
        a = path.split('Testcases')
        data_path1 = config.testDataPath()
        data_path2 = os.path.join(a[1].replace('Test', 'Data'))
        data_path3 = (a[1].split(os.sep)[len(a[1].split(os.sep)) - 1]).replace('Test', 'Data.{}'.format(dataType))
        return os.path.join((data_path1 + data_path2), data_path3)

    # 加载 Data 目录下json数据
    def get_jsontestdata(self, path, suitename) -> (dict, list):
        with open(path, encoding='UTF-8') as f:
            data = json.load(f)
            casename = [data[suitename][i]["casename"] for i in range(len(data[suitename]))]
        return data[suitename], casename

    # 加载 Data 目录下yaml数据
    def get_ymltestdata(self, path, suitename) -> (dict, list):
        with open(path, 'r', encoding='utf-8') as f:
            cfg = f.read()
        data = yaml.load(cfg, Loader=yaml.FullLoader)
        casename = [data[suitename][i]["casename"] for i in range(len(data[suitename]))]
        return data[suitename], casename


loadTestData = LoadTestData()

if __name__ == '__main__':
    print(loadTestData.get_datapath("D:/se/Se_Project/Testcases/loginPageTest"))