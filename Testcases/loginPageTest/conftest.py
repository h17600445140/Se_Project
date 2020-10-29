from Util.util import get_jsontestdata, get_datapath
import os
import pytest


data,casename =get_jsontestdata(get_datapath(os.path.dirname(__file__)))

@pytest.fixture(params=data,ids=casename,scope="class")
def json_testdata(request) ->list:
    # 返回数据
    return request.param


# {
#
#     员工信息: {
#         {
#             员工组：1，
# 员工组名称：2
# },
# {
#     员工组：1，
# 员工组名称：2
# }
# }
#
# }
#
# {
#     登陆界面: {
#         {
#             账户：
# 密码：
# }
# {
#     账户：
# 密码：
# }
# }
# }