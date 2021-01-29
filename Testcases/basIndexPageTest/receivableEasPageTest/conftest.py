# -*- coding:utf-8 -*-
from Util import loadTestData

import pytest
import os

suitename = {
    'test_newIncomeStatementBoe': 'newIncomeStatementBoe',
    'test_billingApplicationBoe': 'billingApplicationBoe'
}


newIncomeStatementBoe_data,newIncomeStatementBoe_casename = loadTestData.get_ymltestdata(
    loadTestData.getDataOath(os.path.dirname(os.path.realpath(__file__)), 'yml'),suitename["test_newIncomeStatementBoe"])
@pytest.fixture(params=newIncomeStatementBoe_data,ids=newIncomeStatementBoe_casename,scope="class")
def newIncomeStatementBoe_testdata(request) ->dict:
    # 返回数据
    return request.param


# billingApplicationBoe_data,billingApplicationBoe_casename = loadTestData.get_ymltestdata(
#     loadTestData.getDataOath(os.path.dirname(os.path.realpath(__file__)), 'yml'),suitename["test_billingApplicationBoe"])
# @pytest.fixture(params=billingApplicationBoe_data,ids=billingApplicationBoe_casename,scope="class")
# def billingApplicationBoe_testdata(request) ->dict:
#     # 返回数据
#     return request.param