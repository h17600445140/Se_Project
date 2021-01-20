# -*- coding:utf-8 -*-
from time import sleep

from PageClass.boeApplyPageClass.applyTravelBoePage import ApplyTravelBoePage
from Testcases.common.boeBusinessApprove import BusinessApprove
from Testcases.common.boeSharingCenterApprove import SharingCenterApprove
from Testcases.common.loginDepend import LoginDepend
from Util import logger



# 测试用例 - 差旅申请单（国际）
class TestApplyTravelBoe(object):

    boeNum = globals()

    def setup_class(self):
        self.login = LoginDepend('easHost', 'user')
        self.applyTravelBoePage = ApplyTravelBoePage(self.login.driver)

    def teardown_class(self):
        # self.applyTravelBoePage.driver.quit()
        pass

    def test_applyTravel(self):
        sleep(1)
        self.applyTravelBoePage.open_boeApply()
        sleep(1)
        self.applyTravelBoePage.open_boe('差旅申请单', '差旅')

        sleep(1)
        # 切换窗口
        logger.info("当前窗口为：{}".format(self.applyTravelBoePage.getCurrentWindowHandle()))
        logger.info("所有窗口为：{}".format(self.applyTravelBoePage.getWindowHandles()))
        windowsList = self.applyTravelBoePage.getWindowHandles()
        self.applyTravelBoePage.switchToWin(windowsList[1])
        logger.info("当前窗口为：{}".format(self.applyTravelBoePage.getCurrentWindowHandle()))

        sleep(1)
        global boeNum
        boeNum = self.applyTravelBoePage.getBoeNum()
        logger.info("当前提单单据号为：{}".format(boeNum))

        self.applyTravelBoePage.input_operationType('差旅')
        self.applyTravelBoePage.input_boeAbstract('测试差旅申请单')
        self.applyTravelBoePage.input_applyAmount('100.10')

        sleep(1)
        self.applyTravelBoePage.input_beginDateStr('14')
        self.applyTravelBoePage.input_endDateStr('20')

        sleep(1)
        self.applyTravelBoePage.select_travelTask('会议出差')
        sleep(1)
        self.applyTravelBoePage.input_fromCity('长沙')
        sleep(1)
        self.applyTravelBoePage.input_toCity('北京')
        sleep(1)
        self.applyTravelBoePage.select_transportation('动卧')

        self.applyTravelBoePage.click_boeSubmitButton()

        sleep(3)
        self.applyTravelBoePage.click_close()

        sleep(1)
        logger.info("单据流程结束")

        # 切换窗口
        windowsList = self.applyTravelBoePage.getWindowHandles()
        self.applyTravelBoePage.switchToWin(windowsList[0])
        logger.info("当前窗口为：{}".format(self.applyTravelBoePage.getCurrentWindowHandle()))
        logger.info("所有窗口为：{}".format(self.applyTravelBoePage.getWindowHandles()))

    def test_businessApprove(self):
        global boeNum
        self.businessApprove = BusinessApprove(boeNum)
        content = self.businessApprove.boeBusinessApprove()

        assert content == '审批成功'

    def test_sharingCenterApprove(self):
        global boeNum
        self.sharingCenterApprove = SharingCenterApprove(boeNum)
        self.sharingCenterApprove.sharingCenterApproveChuShen()
        self.sharingCenterApprove.sharingCenterApproveFuShen()