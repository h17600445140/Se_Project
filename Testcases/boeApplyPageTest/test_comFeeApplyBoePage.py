# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageClass.boeApplyPageClass.comFeeApplyBoePage import ComFeeApplyBoePage
from Testcases.common.boeBusinessApprove import BusinessApprove
from Testcases.common.loginDepend import LoginDepend
from Util import logger


class TestComFeeApplyBoePage(object):

    boeNum = None

    def setup_class(self):
        self.login = LoginDepend('easHost', 'user')
        self.comFeeApplyBoePage = ComFeeApplyBoePage(self.login.driver)

    def teardown_class(self):
        # self.comFeeApplyBoePage.driver.quit()
        pass

    def test_comFeeApply(self):

        sleep(1)
        self.comFeeApplyBoePage.open_boeApply()

        self.comFeeApplyBoePage.open_comFeeApplyBoe()

        sleep(1)
        logger.info("当前窗口为：{}".format(self.comFeeApplyBoePage.getCurrentWindowHandle()))
        logger.info("所有窗口为：{}".format(self.comFeeApplyBoePage.getWindowHandles()))

        # 切换窗口
        windowsList = self.comFeeApplyBoePage.getWindowHandles()
        self.comFeeApplyBoePage.switchToWin(windowsList[1])

        logger.info("当前窗口为：{}".format(self.comFeeApplyBoePage.getCurrentWindowHandle()))

        sleep(1)
        global boeNum
        boeNum = self.comFeeApplyBoePage.getBoeNum()
        logger.info("当前提单单据号为：{}".format(boeNum))

        sleep(1)
        self.comFeeApplyBoePage.input_operationType('通用费用申请')

        sleep(1)
        self.comFeeApplyBoePage.input_boeAbstract('测试')

        sleep(1)
        self.comFeeApplyBoePage.input_operationSubTypeId('通用业务1')

        sleep(1)
        self.comFeeApplyBoePage.input_expenseAmount('100.11')

        sleep(1)
        self.comFeeApplyBoePage.input_remark('测试')

        sleep(1)
        self.comFeeApplyBoePage.click_boeSubmitButton()

        sleep(3)
        self.comFeeApplyBoePage.click_close()

        sleep(1)
        logger.info("单据流程结束")

        sleep(1)

        windowsList = self.comFeeApplyBoePage.getWindowHandles()
        self.comFeeApplyBoePage.switchToWin(windowsList[0])

        logger.info("当前窗口为：{}".format(self.comFeeApplyBoePage.getCurrentWindowHandle()))
        logger.info("所有窗口为：{}".format(self.comFeeApplyBoePage.getWindowHandles()))

    def test_businessApprove(self):
        global boeNum
        self.businessApprove = BusinessApprove(boeNum)
        content = self.businessApprove.boeBusinessApprove()

        assert content == '审批成功'
