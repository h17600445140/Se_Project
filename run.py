# -*- coding:utf-8 -*-
from Util import testSuite, logger
import pytest

testcases = testSuite.readTestCase()

if __name__ == '__main__':
    for i in range(len(testcases)):
        logger.info('收集到了测试用例：{}'.format(testcases[i]))
    pytest.main([*testcases,'-v' ,'-s' ,'--alluredir' ,'./Report/allure-results' ,'--clean-alluredir'])





