# -*- coding:utf-8 -*-
import allure
import pytest

from PageClass.basIndexPageClass.accountEasPageClass.newBusinessLedgerBoePage import NewBusinessLedgerBoePage
from Testcases.common.boeBusinessApprove import BusinessApprove
from Testcases.common.boeSharingCenterApprove import SharingCenterApprove
from Testcases.common.loginDepend import LoginDepend
from Util import logger


@allure.feature("业务记账单（新）流程")
class TestNewBusinessLedgerBoe():

    boeNum = globals()

    def setup_class(self):
        self.login = LoginDepend('basHost', 'user')
        self.newBusinessLedgerBoePage = NewBusinessLedgerBoePage(self.login.driver)

    def teardown_class(self):
        self.newBusinessLedgerBoePage.driver.quit()

    @allure.story("业务记账单（新）业务报账界面单据提交")
    @allure.step("业务记账单（新）业务报账界面单据提交步骤")
    @allure.severity("blocker")
    @pytest.mark.dependency(name='submit')
    def test_newBusinessLedgerBoe(self):

        logger.info(" ----- 单据提交流程开始 ----- ")

        with allure.step("点击选择财务记账页面"):
            self.newBusinessLedgerBoePage.selectTabType('财务记账')
        with allure.step("进入业务记账单（新）单据提交页面"):
            self.newBusinessLedgerBoePage.boeRntry('业务记账(新)')

        global boeNum
        boeNum = self.newBusinessLedgerBoePage.getBoeNum()

        with allure.step("选择业务类型"):
            self.newBusinessLedgerBoePage.input_operationType('UI通用')
        with allure.step("输入备注"):
            self.newBusinessLedgerBoePage.input_boeAbstract('测试业务记账单（新）,测试业务记账单（新）,测试业务记账单（新）')

        with allure.step("输入项目"):
            self.newBusinessLedgerBoePage.input_costProject('UI项目')
        with allure.step("输入总金额"):
            self.newBusinessLedgerBoePage.input_costExpenseAmount('100.00')
        with allure.step("输入业务类型"):
            self.newBusinessLedgerBoePage.input_costOperationSubType('UI通用01')
        with allure.step("选择成本中心"):
            self.newBusinessLedgerBoePage.selectCostExpenseDept('UIDP', 'UI部门')

        with allure.step("点击新增明细信息按钮"):
            self.newBusinessLedgerBoePage.click_addDetailButton()

        with allure.step("输入项目"):
            self.newBusinessLedgerBoePage.input_costProject('UI项目', count='1')
        with allure.step("输入总金额"):
            self.newBusinessLedgerBoePage.input_costExpenseAmount('100.00', count='1')
        with allure.step("输入业务类型"):
            self.newBusinessLedgerBoePage.input_costOperationSubType('UI通用02', count='1')
        with allure.step("选择成本中心"):
            self.newBusinessLedgerBoePage.selectCostExpenseDept('UIDP', 'UI部门', count='1')

        with allure.step("点击单据提交"):
            self.newBusinessLedgerBoePage.click_boeSubmitButton()
        with allure.step("点击单据关闭按钮"):
            self.newBusinessLedgerBoePage.click_close()

        with allure.step("进行单据生成校验"):
            self.newBusinessLedgerBoePage.click_more()
            self.newBusinessLedgerBoePage.input_boeNumQuery(boeNum)
            self.newBusinessLedgerBoePage.click_queryButton()

        with allure.step("断言结果：{}".format(self.newBusinessLedgerBoePage.checkBoeNumExistIsOrNot(boeNum))):
            assert self.newBusinessLedgerBoePage.checkBoeNumExistIsOrNot(boeNum) == True

    @allure.story("业务记账单（新）费用报销界面业务审批")
    @allure.step("业务记账单（新）费用报销界面业务审批步骤")
    @pytest.mark.dependency(depends=["submit"] )
    def test_businessApprove(self):
        logger.info(" ----- 单据业务审批开始 ----- ")
        global boeNum
        self.businessApprove = BusinessApprove(boeNum)
        content = self.businessApprove.boeBusinessApprove()
        logger.info(" ----- 单据业务审批开始 ----- ")
        assert content == '审批成功'


    @allure.story("业务记账单（新）共享中心界面财务审批")
    @allure.step("业务记账单（新）共享中心界面财务审批步骤")
    @pytest.mark.dependency(depends=["submit"])
    def test_sharingCenterApprove(self):
        logger.info(" ----- 单据财务审批开始 ----- ")
        global boeNum
        self.sharingCenterApprove = SharingCenterApprove(boeNum)
        self.sharingCenterApprove.sharingCenterApproveChuShen()
        self.sharingCenterApprove.sharingCenterApproveFuShen()
        logger.info(" ----- 单据财务审批结束 ----- ")
