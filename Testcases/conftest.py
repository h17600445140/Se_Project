# 公共conftest.py文件
import pytest
from Util.util import get_urldict


def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item._nodeid.encode("utf-8").decode("unicode_escape")

def pytest_addoption(parser):
    parser.addoption("--test", default="testdata", help="使用 tsetdata")

@pytest.fixture(scope="session")
def cmdopt(request):
    return request.config.getoption("--test")

@pytest.fixture(scope="session")
def env(request, cmdopt):
    request.config.base_data = get_urldict()
    return request.config.base_data
