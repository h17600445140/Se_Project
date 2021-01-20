# -*- coding:utf-8 -*-
from time import sleep

from PageClass.BoeReimbursementPageClass.newDailyExpenseBoePage import NewDailyExpenseBoePage
from Testcases.common.boeBusinessApprove import BusinessApprove
from Testcases.common.boeSharingCenterApprove import SharingCenterApprove
from Testcases.common.loginDepend import LoginDepend
from Util import logger



class TestNewDailyExpenseBoe():

    boeNum = globals()

    def setup_class(self):
        self.login = LoginDepend('easHost', 'user')
        self.newDailyExpenseBoePage = NewDailyExpenseBoePage(self.login.driver)

    def teardown_class(self):
        # self.newDailyExpenseBoePage.driver.quit()
        pass

    def test_newDailyExpense(self):

        sleep(1)
        self.newDailyExpenseBoePage.open_boeReimburse()
        sleep(1)
        self.newDailyExpenseBoePage.open_newDailyExpenseBoe()

        sleep(1)
        # 切换窗口
        windowsList = self.newDailyExpenseBoePage.getWindowHandles()
        self.newDailyExpenseBoePage.switchToWin(windowsList[1])

        global boeNum
        boeNum = self.newDailyExpenseBoePage.getBoeNum()
        logger.info("当前提单单据号为：{}".format(boeNum))

        self.newDailyExpenseBoePage.input_operationType('通用费用申请')

        sleep(1)
        self.newDailyExpenseBoePage.input_boeAbstract('测试')

        sleep(1)
        self.newDailyExpenseBoePage.selectRelatedInvoice('80000010')

        sleep(1)
        self.newDailyExpenseBoePage.selectOperationSubType('通用业务1')

        sleep(1)
        self.newDailyExpenseBoePage.selectDepartment('BD', 'B部门')

        sleep(1)
        self.newDailyExpenseBoePage.input_projectId('hc项目1')

        # sleep(1)
        # self.newDailyExpenseBoePage.input_expenseAmount('100.10')

        sleep(1)
        self.newDailyExpenseBoePage.click_boeSubmitButton()

        sleep(3)
        self.newDailyExpenseBoePage.click_close()

        sleep(1)
        logger.info("单据流程结束")

        sleep(1)

        windowsList = self.newDailyExpenseBoePage.getWindowHandles()
        self.newDailyExpenseBoePage.switchToWin(windowsList[0])

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