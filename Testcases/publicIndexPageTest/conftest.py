from Util import loadTestData

import pytest
import os

suitename = {
    "test_groupManagementPage":{"TestManagementPageClass":"managementPageClass"},
    "test_sharingCenterPage":{},
    "test_systemDefinitionPage":{},
    "test_timedTasksPage":{}
}

managementPageClass_data,managementPageClass_casename = loadTestData.get_ymltestdata(
    loadTestData.get_ymldatapath(os.path.dirname(__file__)),suitename["test_groupManagementPage"]["TestManagementPageClass"])

@pytest.fixture(params=managementPageClass_data,ids=managementPageClass_casename,scope="class")
def managementPageClass_testdata(request) ->dict:
    # 返回数据
    return request.param
