import pytest
import os
import yaml

def pytest_addoption(parser):
    parser.addoption("--test", default="testdata", help="使用 tsetdata")

@pytest.fixture(scope="session")
def cmdopt(request):
    return request.config.getoption("--test")

def get_urldict():
    path = os.path.dirname(os.path.dirname(__file__))
    yamlPath = os.sep.join([path, 'Config', 'test', 'testUrl_config.yml'])
    with open(yamlPath, 'r', encoding='utf-8') as f:
        cfg = f.read()
    d = yaml.load(cfg, Loader=yaml.FullLoader)
    # print(d)    # {'url': {'host': 'http://fsscysc.csztessc.com.cn:8085/'}}
    return d

@pytest.fixture(scope="session")
def env(request, cmdopt):
    request.config.base_data = get_urldict()
    return request.config.base_data
