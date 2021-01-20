# -*- coding:utf-8 -*-
from time import sleep

from PageClass.boeBorrowPageClass.employeeRepaymentBoePage import EmployeeRepaymentBoePage
from Testcases.common.boeBusinessApprove import BusinessApprove
from Testcases.common.boeSharingCenterApprove import SharingCenterApprove
from Testcases.common.loginDepend import LoginDepend
from Util import logger



class TestEmployeeRepaymentBoe(object):

    boeNum = globals()

    def setup_class(self):
        self.login = LoginDepend('easHost', 'user')
        self.employeeRepaymentBoePage = EmployeeRepaymentBoePage(self.login.driver)

    def teardown_class(self):
        # self.employeeRepaymentBoePage.driver.quit()
        pass

    def test_employeeRepayment(self):

        sleep(1)
        self.employeeRepaymentBoePage.open_boeBorrow()
        sleep(1)
        self.employeeRepaymentBoePage.open_employeeRepaymentBoe()

        sleep(1)
        # 切换窗口
        windowsList = self.employeeRepaymentBoePage.getWindowHandles()
        self.employeeRepaymentBoePage.switchToWin(windowsList[1])

        sleep(1)
        global boeNum
        boeNum = self.employeeRepaymentBoePage.getBoeNum()
        logger.info("当前提单单据号为：{}".format(boeNum))

        sleep(1)
        self.boeFee = self.employeeRepaymentBoePage.selectWriteOffBoe('hcGroup-BX210119105')

        self.employeeRepaymentBoePage.selectReplaymentType('还款002')

        self.employeeRepaymentBoePage.input_expenseAmount(self.boeFee)

        self.employeeRepaymentBoePage.selectCollectionAccount('hc账户1')

        self.employeeRepaymentBoePage.selectLoanRepaymentDate()

        self.employeeRepaymentBoePage.input_remark('测试')

        self.employeeRepaymentBoePage.click_boeSubmitButton()

        sleep(3)
        self.employeeRepaymentBoePage.click_close()

        sleep(1)
        logger.info("单据流程结束")

        sleep(1)

        windowsList = self.employeeRepaymentBoePage.getWindowHandles()
        self.employeeRepaymentBoePage.switchToWin(windowsList[0])

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

