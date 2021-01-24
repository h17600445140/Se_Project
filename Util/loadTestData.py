# -*- coding:utf-8 -*-
import json
import yaml

class LoadTestData():

    def __init__(self):
        pass

    # 获取 data_path
    def get_datapath(self, path : str) -> str:
        # D: / se / Se_Project / Testcases / loginPageTest
        a = path.split('Testcases')
        b = a[1].split('Test')
        data_path = a[0] + 'Data' + b[0] + 'Data' + b[0] + 'Data.json'
        return data_path

    def get_ymldatapath(self, path : str) -> str:
        a = path.split('Testcases')
        b = a[1].split('Test')
        data_path = a[0] + 'Data' + b[0] + 'Data' + b[0] + 'Data.yml'
        return data_path

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
        print(path)
        print(suitename)
        data = yaml.load(cfg, Loader=yaml.FullLoader)
        print(data)
        casename = [data[suitename][i]["casename"] for i in range(len(data[suitename]))]
        return data[suitename], casename


loadTestData = LoadTestData()

if __name__ == '__main__':
    print(loadTestData.get_datapath("D:/se/Se_Project/Testcases/loginPageTest"))