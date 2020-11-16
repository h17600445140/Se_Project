from Util.util import get_jsontestdata, get_datapath
import os
import pytest

suitename = {"test_publciLoginPage":"publicLoginPage"}

data,casename =get_jsontestdata(get_datapath(os.path.dirname(__file__)),suitename["test_publciLoginPage"])

@pytest.fixture(params=data,ids=casename,scope="class")
def publciLoginPage_testdata(request) ->dict:
    # 返回数据
    return request.param
