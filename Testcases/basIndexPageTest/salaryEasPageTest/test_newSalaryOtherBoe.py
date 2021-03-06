# -*- coding:utf-8 -*-
from time import sleep

import allure
import pytest

from PageClass.basIndexPageClass.salaryEasPageClass.newSalaryOtherBoePage import NewSalaryOtherBoePage
from Testcases.common.boeBusinessApprove import BusinessApprove
from Testcases.common.boeSharingCenterApprove import SharingCenterApprove
from Testcases.common.loginDepend import LoginDepend
from Util import logger


@allure.feature("五险一金报账单（新）流程")
class TestNewSalaryOtherBoe():

    boeNum = globals()

    def setup_class(self):
        self.publicLogin = LoginDepend('basHost', 'user')
        self.newSalaryOtherBoePage = NewSalaryOtherBoePage(self.publicLogin.driver)

    def teardown_class(self):
        self.newSalaryOtherBoePage.driver.quit()

    @allure.story("五险一金报账单（新）业务报账界面单据提交")
    @allure.step("五险一金报账单（新）业务报账界面单据提交步骤")
    @allure.severity("blocker")
    @pytest.mark.dependency(name='submit')
    def test_newSalaryOtherBoe(self):

        logger.info(" ----- 单据提交流程开始 ----- ")

        with allure.step("点击选择收入收款页面"):
            self.newSalaryOtherBoePage.selectTabType('薪酬报账')
        with allure.step("进入收入报账单单据提交页面"):
            self.newSalaryOtherBoePage.boeRntry('五险一金报账单（新）')

        global boeNum
        boeNum = self.newSalaryOtherBoePage.getBoeNum()

        with allure.step("选择业务类型"):
            self.newSalaryOtherBoePage.input_operationType('UI工资发放')
        with allure.step("输入备注"):
            self.newSalaryOtherBoePage.input_boeAbstract('测试五险一金报账单（新）')

        with allure.step("选择关联薪资"):
            self.newSalaryOtherBoePage.select_salary()

        sleep(1)

        with allure.step("选择收款账户"):
            self.newSalaryOtherBoePage.selectVendorAccount('1109123456789001', accountName='UI供应商')
        with allure.step("输入支付金额"):
            self.newSalaryOtherBoePage.input_paymentAmount('200.20')

        with allure.step("点击单据提交"):
            self.newSalaryOtherBoePage.click_boeSubmitButton()
        with allure.step("点击单据关闭按钮"):
            self.newSalaryOtherBoePage.click_close()

        with allure.step("进行单据生成校验"):
            self.newSalaryOtherBoePage.click_more()
            self.newSalaryOtherBoePage.input_boeNumQuery(boeNum)
            self.newSalaryOtherBoePage.click_queryButton()

        with allure.step("断言结果：{}".format(self.newSalaryOtherBoePage.checkBoeNumExistIsOrNot(boeNum))):
            assert self.newSalaryOtherBoePage.checkBoeNumExistIsOrNot(boeNum) == True

        logger.info(" ----- 单据提交流程结束 ----- ")


    @allure.story("五险一金报账单（新）费用报销界面业务审批")
    @allure.step("五险一金报账单（新）费用报销界面业务审批步骤")
    @pytest.mark.dependency(depends=["submit"])
    def test_businessApprove(self):
        logger.info(" ----- 单据业务审批开始 ----- ")
        global boeNum
        self.businessApprove = BusinessApprove(boeNum)
        content = self.businessApprove.boeBusinessApprove()
        logger.info(" ----- 单据业务审批开始 ----- ")
        assert content == '审批成功'


    @allure.story("五险一金报账单（新）共享中心界面财务审批")
    @allure.step("五险一金报账单（新）共享中心界面财务审批步骤")
    @pytest.mark.dependency(depends=["submit"])
    def test_sharingCenterApprove(self):
        logger.info(" ----- 单据财务审批开始 ----- ")
        global boeNum
        self.sharingCenterApprove = SharingCenterApprove(boeNum)
        self.sharingCenterApprove.sharingCenterApproveChuShen()
        self.sharingCenterApprove.sharingCenterApproveFuShen()
        logger.info(" ----- 单据财务审批结束 ----- ")