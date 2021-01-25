from Util import loadTestData

import pytest
import os

suitename = {
    "test_employeeLoadBoe": 'employeeLoadBoe',
    "test_employeeRepaymentBoe": 'employeeRepaymentBoe'
}


employeeLoadBoe_data,employeeLoadBoe_casename = loadTestData.get_ymltestdata(
    loadTestData.get_ymldatapath(os.path.dirname(__file__)),suitename["test_employeeLoadBoe"])
@pytest.fixture(params=employeeLoadBoe_data,ids=employeeLoadBoe_casename,scope="class")
def employeeLoadBoe_testdata(request) ->dict:
    # 返回数据
    return request.param


employeeRepaymentBoe_data,employeeRepaymentBoe_casename = loadTestData.get_ymltestdata(
    loadTestData.get_ymldatapath(os.path.dirname(__file__)),suitename["test_employeeRepaymentBoe"])
@pytest.fixture(params=employeeRepaymentBoe_data,ids=employeeRepaymentBoe_casename,scope="class")
def employeeRepaymentBoe_testdata(request) ->dict:
    # 返回数据
    return request.param