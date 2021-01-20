# -*- coding:utf-8 -*-
from time import sleep

from PageClass.boeApplyPageClass.applyInternationalTravelBoePage import ApplyInternationalTravelBoePage
from Testcases.common.boeBusinessApprove import BusinessApprove
from Testcases.common.boeSharingCenterApprove import SharingCenterApprove
from Testcases.common.loginDepend import LoginDepend


from Util import logger



# 测试用例 - 差旅申请单（国际）
class TestApplyInternationalTravelBoe(object):

    boeNum = globals()

    def setup_class(self):
        self.login = LoginDepend('easHost', 'user')
        self.applyInternationalTravelBoePage = ApplyInternationalTravelBoePage(self.login.driver)

    def teardown_class(self):
        # self.applyInternationalTravelBoePage.driver.quit()
        pass

    def test_applyInternationalTravel(self):

        sleep(1)
        self.applyInternationalTravelBoePage.open_boeApply()
        sleep(1)
        self.applyInternationalTravelBoePage.open_boe('差旅申请单（国际）', '差旅')

        sleep(1)
        # 切换窗口
        logger.info("当前窗口为：{}".format(self.applyInternationalTravelBoePage.getCurrentWindowHandle()))
        logger.info("所有窗口为：{}".format(self.applyInternationalTravelBoePage.getWindowHandles()))
        windowsList = self.applyInternationalTravelBoePage.getWindowHandles()
        self.applyInternationalTravelBoePage.switchToWin(windowsList[1])
        logger.info("当前窗口为：{}".format(self.applyInternationalTravelBoePage.getCurrentWindowHandle()))

        sleep(1)
        global boeNum
        boeNum = self.applyInternationalTravelBoePage.getBoeNum()
        logger.info("当前提单单据号为：{}".format(boeNum))

        self.applyInternationalTravelBoePage.input_operationType('差旅')
        self.applyInternationalTravelBoePage.input_boeAbstract('测试差旅申请单（国际）')
        self.applyInternationalTravelBoePage.input_applyAmount('100.10')

        sleep(1)
        self.applyInternationalTravelBoePage.input_beginDateStr('14')
        self.applyInternationalTravelBoePage.input_endDateStr('20')

        sleep(1)
        self.applyInternationalTravelBoePage.input_fromCity('长沙')
        sleep(1)
        self.applyInternationalTravelBoePage.input_toCity('北京')

        sleep(1)
        self.applyInternationalTravelBoePage.select_transportation('动卧')
        sleep(1)
        self.applyInternationalTravelBoePage.select_travelTask('会议出差')

        self.applyInternationalTravelBoePage.input_projectId('hc项目1')

        self.applyInternationalTravelBoePage.click_boeSubmitButton()

        sleep(3)
        self.applyInternationalTravelBoePage.click_close()

        sleep(1)
        logger.info("单据流程结束")

        # 切换窗口
        windowsList = self.applyInternationalTravelBoePage.getWindowHandles()
        self.applyInternationalTravelBoePage.switchToWin(windowsList[0])
        logger.info("当前窗口为：{}".format(self.applyInternationalTravelBoePage.getCurrentWindowHandle()))
        logger.info("所有窗口为：{}".format(self.applyInternationalTravelBoePage.getWindowHandles()))

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





