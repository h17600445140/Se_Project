from Util.util import get_jsontestdata, get_datapath

import os
import pytest


@pytest.fixture()
def json_testdata() ->list:
    print(os.path.dirname(__file__))
    data_path = get_datapath(os.path.dirname(__file__))
    return get_jsontestdata(data_path)