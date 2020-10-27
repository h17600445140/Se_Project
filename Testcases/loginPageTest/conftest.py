from Util.util import get_jsontestdata, get_datapath
import os
import pytest

case = ["账号密码不匹配", "请输入账户名称", "请输入密码", "当前登录用户名或密码错误", "登陆成功"]

@pytest.fixture(params=get_jsontestdata(get_datapath(os.path.dirname(__file__))),ids=case)
def json_testdata(request) ->list:
    # 返回数据
    return request.param

