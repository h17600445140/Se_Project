from Util import loadTestData

import pytest
import os

suitename = {
    "test_newDailyExpenseBoe": 'newDailyExpenseBoe',
    "test_newDomesticTravelBoe": 'newDomesticTravelBoe',
    "test_newMultiDomesticTravelBoe": 'newMultiDomesticTravelBoe'
}

newDailyExpenseBoe_data,newDailyExpenseBoe_casename = loadTestData.get_ymltestdata(
    loadTestData.get_ymldatapath(os.path.dirname(__file__)),suitename["test_newDailyExpenseBoe"])
@pytest.fixture(params=newDailyExpenseBoe_data,ids=newDailyExpenseBoe_casename,scope="class")
def newDailyExpenseBoe_testdata(request) ->dict:
    # 返回数据
    return request.param

newDomesticTravelBoe_data,newDomesticTravelBoe_casename = loadTestData.get_ymltestdata(
    loadTestData.get_ymldatapath(os.path.dirname(__file__)),suitename["test_newDomesticTravelBoe"])
@pytest.fixture(params=newDomesticTravelBoe_data,ids=newDomesticTravelBoe_casename,scope="class")
def newDomesticTravelBoe_testdata(request) ->dict:
    # 返回数据
    return request.param

newMultiDomesticTravelBoe_data,newMultiDomesticTravelBoe_casename = loadTestData.get_ymltestdata(
    loadTestData.get_ymldatapath(os.path.dirname(__file__)),suitename["test_newMultiDomesticTravelBoe"])
@pytest.fixture(params=newMultiDomesticTravelBoe_data,ids=newMultiDomesticTravelBoe_casename,scope="class")
def newMultiDomesticTravelBoe_testdata(request) ->dict:
    # 返回数据
    return request.param

if __name__ == '__main__':
    # newDomesticTravelBoe_testdata['boeAbstract']
    print('---------------------')
    print(newDomesticTravelBoe_data)
