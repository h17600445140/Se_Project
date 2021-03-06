# -*- coding:utf-8 -*-
import datetime
from time import sleep

import allure
import pytest

from PageClass.basIndexPageClass.accountEasPageClass.newWithholdingAmortizationPage import \
    NewWithholdingAmortizationPage
from Testcases.common.boeBusinessApprove import BusinessApprove
from Testcases.common.boeSharingCenterApprove import SharingCenterApprove
from Testcases.common.loginDepend import LoginDepend
from Util import logger


@allure.feature("预提申请单（新）流程")
class TestNewWithholdingAmortization():

    boeNum = globals()

    def setup_class(self):
        self.login = LoginDepend('basHost', 'user')
        self.newWithholdingAmortizationPage = NewWithholdingAmortizationPage(self.login.driver)

    def teardown_class(self):
        self.newWithholdingAmortizationPage.driver.quit()

    @allure.story("预提申请单（新）业务报账界面单据提交")
    @allure.step("预提申请单（新）业务报账界面单据提交步骤")
    @allure.severity("blocker")
    @pytest.mark.dependency(name='submit')
    def test_newWithholdingAmortization(self):

        logger.info(" ----- 单据提交流程开始 ----- ")

        with allure.step("点击选择财务记账页面"):
            self.newWithholdingAmortizationPage.selectTabType('财务记账')
        with allure.step("进入预提申请单（新）单据提交页面"):
            self.newWithholdingAmortizationPage.boeRntry('预提申请单(新)')

        global boeNum
        boeNum = self.newWithholdingAmortizationPage.getBoeNum()

        with allure.step("选择业务类型"):
            self.newWithholdingAmortizationPage.input_operationType('UI通用')
        with allure.step("输入备注"):
            self.newWithholdingAmortizationPage.input_boeAbstract('测试预提申请单(新)')

        with allure.step("选择客商"):
            self.newWithholdingAmortizationPage.input_vendor('UI供应商1')
        with allure.step("选择预提规则"):
            self.newWithholdingAmortizationPage.selectYuTiRule('按月平均计算')
        # with allure.step("选择合同"):
        #     self.newWithholdingAmortizationPage.selectContract('hc00000022')

        with allure.step("输入预提类型"):
            self.newWithholdingAmortizationPage.input_costOperationSubType('UI通用01')
        with allure.step("选择责任部门"):
            self.newWithholdingAmortizationPage.selectCostExpenseDept('UIDP', deptName='UI部门')
        with allure.step("输入项目"):
            self.newWithholdingAmortizationPage.input_costProject('UI项目')
        with allure.step("输入金额"):
            self.newWithholdingAmortizationPage.input_costExpenseAmount('100.00')
        with allure.step("选择开始时间"):
            self.newWithholdingAmortizationPage.select_costBeginDateStr(datetime.datetime.now().strftime("%Y-%m-%d"))
        with allure.step("输入期限（月）"):
            self.newWithholdingAmortizationPage.input_costTheTerm('3')
        with allure.step("选择贷方科目"):
            self.newWithholdingAmortizationPage.input_voucherAccount('UI科目1')

        with allure.step("自动计算"):
            self.newWithholdingAmortizationPage.click_autoCalculation()

        with allure.step("点击单据提交"):
            self.newWithholdingAmortizationPage.click_boeSubmitButton()
        with allure.step("点击单据关闭按钮"):
            self.newWithholdingAmortizationPage.click_close()

        with allure.step("进行单据生成校验"):
            self.newWithholdingAmortizationPage.click_more()
            self.newWithholdingAmortizationPage.input_boeNumQuery(boeNum)
            self.newWithholdingAmortizationPage.click_queryButton()

        with allure.step("断言结果：{}".format(self.newWithholdingAmortizationPage.checkBoeNumExistIsOrNot(boeNum))):
            assert self.newWithholdingAmortizationPage.checkBoeNumExistIsOrNot(boeNum) == True


    @allure.story("预提申请单（新）费用报销界面业务审批")
    @allure.step("预提申请单（新）费用报销界面业务审批步骤")
    @pytest.mark.dependency(depends=["submit"] )
    def test_businessApprove(self):
        logger.info(" ----- 单据业务审批开始 ----- ")
        global boeNum
        self.businessApprove = BusinessApprove(boeNum)
        content = self.businessApprove.boeBusinessApprove()
        logger.info(" ----- 单据业务审批开始 ----- ")
        assert content == '审批成功'


    @allure.story("预提申请单（新）共享中心界面财务审批")
    @allure.step("预提申请单（新）共享中心界面财务审批步骤")
    @pytest.mark.dependency(depends=["submit"])
    def test_sharingCenterApprove(self):
        logger.info(" ----- 单据财务审批开始 ----- ")
        global boeNum
        self.sharingCenterApprove = SharingCenterApprove(boeNum)
        self.sharingCenterApprove.sharingCenterApproveChuShen()
        self.sharingCenterApprove.sharingCenterApproveFuShen()
        logger.info(" ----- 单据财务审批结束 ----- ")
