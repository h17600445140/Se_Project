# -*- coding:utf-8 -*-
import allure
import pytest

from PageClass.basIndexPageClass.salaryEasPageClass.newSalaryWageBoePage import NewSalaryWageBoePage
from Testcases.common.boeBusinessApprove import BusinessApprove
from Testcases.common.boeSharingCenterApprove import SharingCenterApprove
from Testcases.common.loginDepend import LoginDepend
from Util import logger


@allure.feature("工资报账单（新）流程")
class TestNewSalaryWageBoe():

    boeNum = globals()

    def setup_class(self):
        self.publicLogin = LoginDepend('basHost', 'user')
        self.newSalaryWageBoePage = NewSalaryWageBoePage(self.publicLogin.driver)

    def teardown_class(self):
        self.newSalaryWageBoePage.driver.quit()

    @allure.story("工资报账单（新）业务报账界面单据提交")
    @allure.step("工资报账单（新）业务报账界面单据提交步骤")
    @allure.severity("blocker")
    @pytest.mark.dependency(name='submit')
    def test_newSalaryWageBoe(self):

        logger.info(" ----- 单据提交流程开始 ----- ")

        with allure.step("点击选择收入收款页面"):
            self.newSalaryWageBoePage.selectTabType('薪酬报账')
        with allure.step("进入收入报账单单据提交页面"):
            self.newSalaryWageBoePage.boeRntry('工资报账单（新）')

        global boeNum
        boeNum = self.newSalaryWageBoePage.getBoeNum()

        with allure.step("选择业务类型"):
            self.newSalaryWageBoePage.input_operationType('UI工资发放')
        with allure.step("输入备注"):
            self.newSalaryWageBoePage.input_boeAbstract('测试工资报账单（新）')

        with allure.step("选择关联薪资"):
            self.newSalaryWageBoePage.select_salary()

        with allure.step("点击单据提交"):
            self.newSalaryWageBoePage.click_boeSubmitButton()
        with allure.step("点击单据关闭按钮"):
            self.newSalaryWageBoePage.click_close()

        with allure.step("进行单据生成校验"):
            self.newSalaryWageBoePage.click_more()
            self.newSalaryWageBoePage.input_boeNumQuery(boeNum)
            self.newSalaryWageBoePage.click_queryButton()

        with allure.step("断言结果：{}".format(self.newSalaryWageBoePage.checkBoeNumExistIsOrNot(boeNum))):
            assert self.newSalaryWageBoePage.checkBoeNumExistIsOrNot(boeNum) == True

        logger.info(" ----- 单据提交流程结束 ----- ")


    @allure.story("工资报账单（新）费用报销界面业务审批")
    @allure.step("工资报账单（新）费用报销界面业务审批步骤")
    @pytest.mark.dependency(depends=["submit"] )
    def test_businessApprove(self):
        logger.info(" ----- 单据业务审批开始 ----- ")
        global boeNum
        self.businessApprove = BusinessApprove(boeNum)
        content = self.businessApprove.boeBusinessApprove()
        logger.info(" ----- 单据业务审批开始 ----- ")
        assert content == '审批成功'


    @allure.story("工资报账单（新）共享中心界面财务审批")
    @allure.step("工资报账单（新）共享中心界面财务审批步骤")
    @pytest.mark.dependency(depends=["submit"])
    def test_sharingCenterApprove(self):
        logger.info(" ----- 单据财务审批开始 ----- ")
        global boeNum
        self.sharingCenterApprove = SharingCenterApprove(boeNum)
        self.sharingCenterApprove.sharingCenterApproveChuShen()
        self.sharingCenterApprove.sharingCenterApproveFuShen()
        logger.info(" ----- 单据财务审批结束 ----- ")









