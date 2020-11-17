import os

from Util.util import get_ymltestdata, get_ymldatapath

suitename = {
    "test_groupManagementPage":{"TestManagementPageClass":"managementPageClass"},
    "test_sharingCenterPage":{},
    "test_systemDefinitionPage":{},
    "test_timedTasksPage":{}
}

managementPageClass_data,managementPageClass_casename = get_ymltestdata(get_ymldatapath(os.path.dirname(__file__)),suitename["test_groupManagementPage"]["TestManagementPageClass"])

print(managementPageClass_data)
print(managementPageClass_casename)
