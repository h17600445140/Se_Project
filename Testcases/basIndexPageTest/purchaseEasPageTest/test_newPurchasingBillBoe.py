# -*- coding:utf-8 -*-
import allure
import pytest

from PageClass.basIndexPageClass.purchaseEasPageClass.newPurchasingBillBoePage import NewPurchasingBillBoePage
from Testcases.common.boeBusinessApprove import BusinessApprove
from Testcases.common.boeSharingCenterApprove import SharingCenterApprove
from Testcases.common.loginDepend import LoginDepend
from Util import logger


@allure.feature("采购报账单流程")
class TestCostEstimateBoe():

    boeNum = globals()

    def setup_class(self):
        self.login = LoginDepend('basHost', 'user')
        self.newPurchasingBillBoePage = NewPurchasingBillBoePage(self.login.driver)

    def teardown_class(self):
        # self.newPurchasingBillBoePage.driver.quit()
        pass


    @allure.story("采购报账单业务报账界面单据提交")
    @allure.step("采购报账单业务报账界面单据提交步骤")
    @allure.severity("blocker")
    @pytest.mark.dependency(name='submit')
    def test_newPurchasingBillBoe(self):

        logger.info(" ----- 单据提交流程开始 ----- ")

        with allure.step("点击选择采购付款页面"):
            self.newPurchasingBillBoePage.selectTabType('采购付款')
        with allure.step("进入采购报账单单据提交页面"):
            self.newPurchasingBillBoePage.boeRntry('采购报账')

        global boeNum
        boeNum = self.newPurchasingBillBoePage.getBoeNum()

        with allure.step("选择业务类型"):
            self.newPurchasingBillBoePage.input_operationType('报账')
        with allure.step("输入备注"):
            self.newPurchasingBillBoePage.input_boeAbstract('测试采购报账单')

        with allure.step("选择供应商"):
            self.newPurchasingBillBoePage.selectVendor('hcGYS1', vendorName='hc供应商1')
        with allure.step("选择关联合同"):
            self.newPurchasingBillBoePage.selectContract('hc00000022')
        with allure.step("输入项目"):
            self.newPurchasingBillBoePage.input_project('hc项目1')
        with allure.step("选择成本中心"):
            self.newPurchasingBillBoePage.selectExpenseDept('AD', deptName='A部门')


        # with allure.step("建立关联"):
        #     self.newPurchasingBillBoePage.click_makeRelated()
        #     self.newPurchasingBillBoePage.relateAcceptancesheetAndInvoice('ysd005', '88800001')


        with allure.step("关联付款计划"):
            self.newPurchasingBillBoePage.selectAccountReceivable('质保金付款')

        with allure.step("点击单据提交"):
            self.newPurchasingBillBoePage.click_boeSubmitButton()
        with allure.step("点击单据关闭按钮"):
            self.newPurchasingBillBoePage.click_close()

        with allure.step("进行单据生成校验"):
            self.newPurchasingBillBoePage.click_more()
            self.newPurchasingBillBoePage.input_boeNumQuery(boeNum)
            self.newPurchasingBillBoePage.click_queryButton()

        with allure.step("断言结果：{}".format(self.newPurchasingBillBoePage.checkBoeNumExistIsOrNot(boeNum))):
            assert self.newPurchasingBillBoePage.checkBoeNumExistIsOrNot(boeNum) == True


    @allure.story("采购报账单费用报销界面业务审批")
    @allure.step("采购报账单费用报销界面业务审批步骤")
    @pytest.mark.dependency(depends=["submit"] )
    def test_businessApprove(self):
        logger.info(" ----- 单据业务审批开始 ----- ")
        global boeNum
        self.businessApprove = BusinessApprove(boeNum)
        content = self.businessApprove.boeBusinessApprove()
        logger.info(" ----- 单据业务审批开始 ----- ")
        assert content == '审批成功'


    @allure.story("采购报账单共享中心界面财务审批")
    @allure.step("采购报账单共享中心界面财务审批步骤")
    @pytest.mark.dependency(depends=["submit"])
    def test_sharingCenterApprove(self):
        logger.info(" ----- 单据财务审批开始 ----- ")
        global boeNum
        self.sharingCenterApprove = SharingCenterApprove(boeNum)
        self.sharingCenterApprove.sharingCenterApproveChuShen()
        self.sharingCenterApprove.sharingCenterApproveFuShen()
        logger.info(" ----- 单据财务审批结束 ----- ")



