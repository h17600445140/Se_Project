# -*- coding:utf-8 -*-
from time import sleep

from PageClass.BoeReimbursementPageClass.newMultiDomesticTravelBoePage import NewMultiDomesticTravelBoePage
from Testcases.common import invoiceFactory
from Testcases.common.boeBusinessApprove import BusinessApprove
from Testcases.common.boeSharingCenterApprove import SharingCenterApprove
from Testcases.common.loginDepend import LoginDepend
from Util import logger



class TestNewMultiDomesticTravelBoe():

    boeNum = globals()

    def setup_class(self):
        self.login = LoginDepend('easHost', 'user')
        self.newMultiDomesticTravelBoePage = NewMultiDomesticTravelBoePage(self.login.driver)

    def teardown_class(self):
        # self.newMultiDomesticTravelBoePage.driver.quit()
        pass

    def test_newMultiDomesticTravel(self):

        self.newMultiDomesticTravelBoePage.open_boeReimburse()
        sleep(1)
        self.newMultiDomesticTravelBoePage.open_boe('多人差旅报账单', '差旅')

        sleep(1)
        # 切换窗口
        logger.info("当前窗口为：{}".format(self.newMultiDomesticTravelBoePage.getCurrentWindowHandle()))
        logger.info("所有窗口为：{}".format(self.newMultiDomesticTravelBoePage.getWindowHandles()))
        windowsList = self.newMultiDomesticTravelBoePage.getWindowHandles()
        self.newMultiDomesticTravelBoePage.switchToWin(windowsList[1])
        logger.info("当前窗口为：{}".format(self.newMultiDomesticTravelBoePage.getCurrentWindowHandle()))

        sleep(1)
        global boeNum
        boeNum = self.newMultiDomesticTravelBoePage.getBoeNum()
        logger.info("当前提单单据号为：{}".format(boeNum))

        self.newMultiDomesticTravelBoePage.input_operationType('差旅')
        self.newMultiDomesticTravelBoePage.input_boeAbstract('测试多人差旅报账单')

        self.newMultiDomesticTravelBoePage.add_travelers('3')

        self.newMultiDomesticTravelBoePage.select_projectId('hc项目1')

        self.newMultiDomesticTravelBoePage.clearPersonCard()

        self.newMultiDomesticTravelBoePage.click_addInvoiceButton()
        self.newMultiDomesticTravelBoePage.click_invoiceType()
        # 差旅火车票新增
        invoiceFactory.get_invoice(self.login.driver, '火车票', 'boeInvoicePage').getTickets(
            '2021-1-27', '内部人员', '1hc', '长沙', '北京', '二等座（高铁/动车）', '500.00', '否')

        self.newMultiDomesticTravelBoePage.click_addInvoiceButton()
        self.newMultiDomesticTravelBoePage.click_invoiceType()
        # 差旅火车票新增
        invoiceFactory.get_invoice(self.login.driver, '火车票', 'boeInvoicePage').getTickets(
            '2021-1-27', '内部人员', 'hr员工3', '长沙', '北京', '二等座（高铁/动车）', '500.00', '否')

        # self.newMultiDomesticTravelBoePage.click_addInvoiceButton()
        # self.newMultiDomesticTravelBoePage.click_invoiceType()
        # invoiceFactory.get_invoice(self.login.driver, '增值税普通发票', 'boeInvoicePage').getTickets(
        #     '2021-1-27', '811000000002', '81100002', '100.10', '0.10', '123456')

        self.newMultiDomesticTravelBoePage.click_boeSubmitButton()
        self.newMultiDomesticTravelBoePage.click_close()

        logger.info("单据流程结束")
        windowsList = self.newMultiDomesticTravelBoePage.getWindowHandles()
        self.newMultiDomesticTravelBoePage.switchToWin(windowsList[0])

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