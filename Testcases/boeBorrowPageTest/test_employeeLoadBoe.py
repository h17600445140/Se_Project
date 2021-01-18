# -*- coding:utf-8 -*-
from time import sleep

from PageClass.boeBorrowPageClass.employeeLoansBoePage import EmployeeLoansBoePage
from Testcases.common.boeBusinessApprove import BusinessApprove
from Testcases.common.boeSharingCenterApprove import SharingCenterApprove
from Testcases.common.loginDepend import LoginDepend
from Util import logger



class TestEmployeeLoadBoe(object):

    boeNum = globals()

    def setup_class(self):

        self.login = LoginDepend('easHost', 'user')
        self.employeeLoansBoePage = EmployeeLoansBoePage(self.login.driver)

    def teardown_class(self):
        # self.employeeLoansBoePage.driver.quit()
        pass

    def test_employeeLoad(self):

        sleep(1)
        self.employeeLoansBoePage.open_boeBorrow()

        self.employeeLoansBoePage.open_employeeLoansBoe()

        sleep(1)
        # 切换窗口
        windowsList = self.employeeLoansBoePage.getWindowHandles()
        self.employeeLoansBoePage.switchToWin(windowsList[1])

        sleep(1)
        global boeNum
        boeNum = self.employeeLoansBoePage.getBoeNum()
        logger.info("当前提单单据号为：{}".format(boeNum))

        sleep(1)
        self.employeeLoansBoePage.input_operationType('借款业务')

        sleep(1)
        self.employeeLoansBoePage.input_boeAbstract('测试')

        sleep(1)
        self.employeeLoansBoePage.input_operationSubTypeId('借款业务1')

        sleep(1)
        self.employeeLoansBoePage.input_expenseAmount('100.11')

        sleep(1)
        self.employeeLoansBoePage.input_projectId('hc项目1')

        sleep(1)
        self.employeeLoansBoePage.click_boeSubmitButton()

        sleep(3)
        self.employeeLoansBoePage.click_close()

        sleep(1)
        logger.info("单据流程结束")

        sleep(1)

        windowsList = self.employeeLoansBoePage.getWindowHandles()
        self.employeeLoansBoePage.switchToWin(windowsList[0])

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




