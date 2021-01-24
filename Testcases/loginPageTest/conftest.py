# -*- coding:utf-8 -*-
from Util import loadTestData
import os
import pytest

suitename = {"test_publciLoginPage":"publicLoginPage"}


data,casename = loadTestData.get_jsontestdata(loadTestData.get_datapath(os.path.dirname(__file__)),suitename["test_publciLoginPage"])

@pytest.fixture(params=data,ids=casename,scope="class")
def publciLoginPage_testdata(request) -> dict:
    # 返回数据
    return request.param

if __name__ == '__main__':
    print(data)
    print(casename)
    print(loadTestData.get_datapath(os.path.dirname(__file__)))
    print(os.path.dirname(__file__))

