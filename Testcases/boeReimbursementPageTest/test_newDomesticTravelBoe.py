# -*- coding:utf-8 -*-
from time import sleep

from PageClass.BoeReimbursementPageClass.newDomesticTravelBoePage import NewDomesticTravelBoePage
from PageClass.easIndexPageClass.easMyInvoicePage import EasMyInvoiceIndexPage
from Testcases.common import invoiceFactory
from Testcases.common.boeBusinessApprove import BusinessApprove
from Testcases.common.boeSharingCenterApprove import SharingCenterApprove
from Testcases.common.loginDepend import LoginDepend
from Util import logger



class TestNewDomesticTravelBoe():

    boeNum = globals()

    def setup_class(self):
        self.login = LoginDepend('easHost', 'user')
        self.newDomesticTravelBoePage = NewDomesticTravelBoePage(self.login.driver)

    def teardown_class(self):
        # self.newDomesticTravelBoePage.driver.quit()
        pass

    def test_newDomesticTravel(self):

        self.newDomesticTravelBoePage.open_boeReimburse()
        sleep(1)
        self.newDomesticTravelBoePage.open_boe('差旅报账单', '差旅')

        sleep(1)
        # 切换窗口
        logger.info("当前窗口为：{}".format(self.newDomesticTravelBoePage.getCurrentWindowHandle()))
        logger.info("所有窗口为：{}".format(self.newDomesticTravelBoePage.getWindowHandles()))
        windowsList = self.newDomesticTravelBoePage.getWindowHandles()
        self.newDomesticTravelBoePage.switchToWin(windowsList[1])
        logger.info("当前窗口为：{}".format(self.newDomesticTravelBoePage.getCurrentWindowHandle()))

        sleep(1)
        global boeNum
        boeNum = self.newDomesticTravelBoePage.getBoeNum()
        logger.info("当前提单单据号为：{}".format(boeNum))

        self.newDomesticTravelBoePage.input_operationType('差旅')
        self.newDomesticTravelBoePage.input_boeAbstract('测试差旅报账单')

        self.newDomesticTravelBoePage.click_addInvoiceButton()

        self.newDomesticTravelBoePage.click_invoiceType()

        # 差旅火车票新增
        invoiceFactory.get_invoice(self.login.driver, '火车票', 'boeInvoicePage').getTickets(
            '2021-1-13', '内部人员', '1hc', '长沙', '西安', '二等座（高铁/动车）', '500.00', '否')

        self.newDomesticTravelBoePage.selectDepartment('BD', 'B部门')
        self.newDomesticTravelBoePage.input_projectId('hc项目1')


        self.newDomesticTravelBoePage.click_boeSubmitButton()
        self.newDomesticTravelBoePage.click_close()

        logger.info("单据流程结束")
        windowsList = self.newDomesticTravelBoePage.getWindowHandles()
        self.newDomesticTravelBoePage.switchToWin(windowsList[0])

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











