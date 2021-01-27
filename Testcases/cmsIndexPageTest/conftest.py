from Util import loadTestData, record

import pytest
import os

suitename = {
    "test_contractEditPage": 'contractEditPage'
}

contractEditPage_data,contractEditPage_casename = loadTestData.get_ymltestdata(
    loadTestData.get_ymldatapath(os.path.dirname(__file__)),suitename["test_contractEditPage"])
@pytest.fixture(params=contractEditPage_data,ids=contractEditPage_casename,scope="class")
def contractEditPage_testdata(request) -> dict:
    # 返回数据
    return request.param


if __name__ == '__main__':
    pass
