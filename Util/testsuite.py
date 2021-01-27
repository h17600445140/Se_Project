# -*- coding:utf-8 -*-
"""

author      :   huangchao
fileName    :   testsuite.py

"""

import os
from Util import config
import pandas as pd



class TestSuite():

    def __init__(self):
        self._testfiles = []
        self._testsuites = []
        self._testPlanPath = os.path.join(config.configPath(), "testPlan.xlsx")

    # 读取测试计划
    def readTestPlan(self) -> list:

        df = pd.read_excel(io=self._testPlanPath, sheet_name=0)
        row = df.shape[0]

        for i in range(row):
            if df.at[i, "是否执行"] == "Y":
                filename = df.at[i, "文件名"]
                self._testfiles.append(filename)
        return self._testfiles

    # 读取测试用例
    def readTestCase(self) -> list:

        for testfile in self.readTestPlan():
            testcasePath = os.path.join(config.configPath(), testfile)
            df = pd.read_excel(io=testcasePath, sheet_name=0)
            row = df.shape[0]
            for i in range(row):
                if df.at[i, "是否执行"] == "N":
                    continue
                if df.at[i, "配置方式"] == "1-按方法运行":
                    self._testsuites.append(
                        os.path.join(df.at[i, "路径"], df.at[i, "文件名"]) + "::" + df.at[i, "类名"] + "::" + df.at[i, "方法名"])
                elif df.at[i, "配置方式"] == "2-按类名运行":
                    self._testsuites.append(os.path.join(df.at[i, "路径"], df.at[i, "文件名"]) + "::" + df.at[i, "类名"])
                elif df.at[i, "配置方式"] == "3-按文件名运行":
                    self._testsuites.append(os.path.join(df.at[i, "路径"], df.at[i, "文件名"]))

        return self._testsuites

testSuite = TestSuite()


if __name__ == '__main__':
    testSuite.readTestPlan()



