from Util import loadTestData

import pytest
import os

suitename = {
    "test_groupManagementPage":{"TestManagementPage":"managementPage"},
    "test_sharingCenterPage":{},
    "test_systemDefinitionPage":{},
    "test_timedTasksPage":{}
}

managementPage_data,managementPage_casename = loadTestData.get_ymltestdata(
    loadTestData.get_ymldatapath(os.path.dirname(__file__)),suitename["test_groupManagementPage"]["TestManagementPage"])

@pytest.fixture(params=managementPage_data,ids=managementPage_casename,scope="class")
def managementPage_testdata(request) ->dict:
    # 返回数据
    return request.param

if __name__ == '__main__':
    # print(os.path.dirname(__file__))
    print(suitename["test_groupManagementPage"]["TestManagementPage"])
    print(loadTestData.get_ymldatapath(os.path.dirname(__file__)))
    print(loadTestData.get_ymldatapath(os.path.dirname(__file__)),suitename["test_groupManagementPage"]["TestManagementPage"])
    print(loadTestData.get_ymltestdata(loadTestData.get_ymldatapath(os.path.dirname(__file__)),suitename["test_groupManagementPage"]["TestManagementPage"]))
