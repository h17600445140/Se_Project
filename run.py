import pytest
import pandas as pd
from Util import Config
import os

# pytest Testcases/loginPageTest/test_publciLoginPage.py

testPlanPath = os.path.join(Config.configPath(),"testPlan.xlsx")
df = pd.read_excel(io=testPlanPath,sheet_name=0)
row = df.shape[0]
testfiles = []

for i in range(row):
    if df.at[i, "是否执行"] == "Y":
        filename = df.at[i, "文件名"]
        testfiles.append(filename)

testsuites = []

for testfile in testfiles:
    testcasePath = os.path.join(Config.configPath(),testfile)
    df = pd.read_excel(io=testcasePath, sheet_name=0)
    row = df.shape[0]
    for i in range(row):
        if df.at[i, "配置方式"] == "1-按方法运行":
            testsuites.append(os.path.join(df.at[i, "路径"], df.at[i, "文件名"])+"::"+df.at[i, "类名"]+"::"+df.at[i, "方法名"])
        elif df.at[i, "配置方式"] == "2-按类名运行":
            testsuites.append(os.path.join(df.at[i, "路径"], df.at[i, "文件名"])+"::"+df.at[i, "类名"])
        elif df.at[i, "配置方式"] == "3-按文件名运行":
            testsuites.append(os.path.join(df.at[i, "路径"], df.at[i, "文件名"]))

for i in testsuites:
    print(i)
if __name__ == '__main__':
    pytest.main([*testsuites,'-v','-s','--strict','--alluredir','./Report/allure-results','--clean-alluredir'])


