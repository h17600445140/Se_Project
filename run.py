# -*- coding:utf-8 -*-
from Util import testSuite
import pytest

testcases = testSuite.readTestCase()

if __name__ == '__main__':
    pytest.main([*testcases,'-v','-s','--strict','--alluredir','./Report/allure-results','--clean-alluredir'])



