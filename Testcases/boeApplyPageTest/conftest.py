# -*- coding:utf-8 -*-
from Util import loadTestData

import pytest
import os

suitename = {
    "test_comFeeApplyBoe": 'comFeeApplyBoe',
    "test_applyTravelBoe": 'applyTravelBoe',
    "test_applyInternationalTravelBoe": 'applyInternationalTravelBoe'
}


comFeeApplyBoe_data,comFeeApplyBoe_casename = loadTestData.get_ymltestdata(
    loadTestData.getDataOath(os.path.dirname(os.path.realpath(__file__)), 'yml'),suitename["test_comFeeApplyBoe"])
@pytest.fixture(params=comFeeApplyBoe_data,ids=comFeeApplyBoe_casename,scope="class")
def comFeeApplyBoe_testdata(request) ->dict:
    # 返回数据
    return request.param


applyTravelBoe_data,applyTravelBoe_casename = loadTestData.get_ymltestdata(
    loadTestData.get_ymldatapath(os.path.dirname(__file__)),suitename["test_applyTravelBoe"])
@pytest.fixture(params=applyTravelBoe_data,ids=applyTravelBoe_casename,scope="class")
def applyTravelBoe_testdata(request) ->dict:
    # 返回数据
    return request.param


applyInternationalTravelBoe_data,applyInternationalTravelBoe_casename = loadTestData.get_ymltestdata(
    loadTestData.get_ymldatapath(os.path.dirname(__file__)),suitename["test_applyInternationalTravelBoe"])
@pytest.fixture(params=applyInternationalTravelBoe_data,ids=applyInternationalTravelBoe_casename,scope="class")
def applyInternationalTravelBoe_testdata(request) ->dict:
    # 返回数据
    return request.param



if __name__ == '__main__':
    # print(loadTestData.get_ymldatapath(os.path.dirname(__file__)))
    print(loadTestData.getDataOath(os.path.dirname(os.path.realpath(__file__)), 'yml'))
    print(os.path.dirname(__file__))
    pass
