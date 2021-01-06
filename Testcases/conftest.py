# -*- coding:utf-8 -*-
import pytest
from Util import config

def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item._nodeid.encode("utf-8").decode("unicode_escape")

def pytest_addoption(parser):
    group = parser.getgroup("test url")
    group.addoption("--test", default="testdata", help="使用 tsetdata")

@pytest.fixture(scope="session")
def cmdopt(request):
    return request.config.getoption("--test")

@pytest.fixture(scope="class")
def env(request) -> dict:
    request.config.base_data = config.getUrlDict()
    return request.config.base_data


