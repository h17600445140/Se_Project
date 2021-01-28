# -*- coding:utf-8 -*-
from Util import loadTestData

import pytest
import os

suitename = {
    "test_newIncomeStatementBoe": 'newIncomeStatementBoe'
}


newIncomeStatementBoe_data,newIncomeStatementBoe_casename = loadTestData.get_ymltestdata(
    loadTestData.getDataOath(os.path.dirname(os.path.realpath(__file__)), 'yml'),suitename["test_newIncomeStatementBoe"])
@pytest.fixture(params=newIncomeStatementBoe_data,ids=newIncomeStatementBoe_casename,scope="class")
def newIncomeStatementBoe_testdata(request) ->dict:
    # 返回数据
    return request.param