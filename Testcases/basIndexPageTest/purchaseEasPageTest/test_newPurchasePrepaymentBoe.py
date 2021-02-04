# -*- coding:utf-8 -*-
import allure
import pytest

from PageClass.basIndexPageClass.purchaseEasPageClass.newPurchasePrepaymentBoePage import NewPurchasePrepaymentBoePage
from Testcases.common.boeBusinessApprove import BusinessApprove
from Testcases.common.boeSharingCenterApprove import SharingCenterApprove
from Testcases.common.loginDepend import LoginDepend
from Util import logger


@allure.feature("采购预付单流程")
class TestNewPurchasePrepaymentBoe():

    boeNum = globals()

    def setup_class(self):
        self.login = LoginDepend('basHost', 'user')
        self.newPurchasePrepaymentBoePage = NewPurchasePrepaymentBoePage(self.login.driver)

    def teardown_class(self):
        # self.newPurchasePrepaymentBoePage.driver.quit()
        pass

    @allure.story("采购预付单业务报账界面单据提交")
    @allure.step("采购预付单业务报账界面单据提交步骤")
    @allure.severity("blocker")
    @pytest.mark.dependency(name='submit')
    def test_newPurchasePrepaymentBoe(self):

        logger.info(" ----- 单据提交流程开始 ----- ")

        with allure.step("点击选择采购付款页面"):
            self.newPurchasePrepaymentBoePage.selectTabType('采购付款')
        with allure.step("进入采购预付单单据提交页面"):
            self.newPurchasePrepaymentBoePage.boeRntry('采购预付')

        global boeNum
        boeNum = self.newPurchasePrepaymentBoePage.getBoeNum()

        with allure.step("选择业务类型"):
            self.newPurchasePrepaymentBoePage.input_operationType('预付')
        with allure.step("输入备注"):
            self.newPurchasePrepaymentBoePage.input_boeAbstract('测试采购预付单')

        with allure.step("选择供应商"):
            self.newPurchasePrepaymentBoePage.selectVendor('hcGYS1', vendorName='hc供应商1')
        with allure.step("选择关联合同"):
            self.newPurchasePrepaymentBoePage.selectContract('hc00000022')

        with allure.step("输入采购订单"):
            self.newPurchasePrepaymentBoePage.input_loanOrderNumber('hcOrder001')
        with allure.step("选择预付类型"):
            self.newPurchasePrepaymentBoePage.input_loanOperationSubType('预付小类1')
        with allure.step("输入预付金额"):
            self.newPurchasePrepaymentBoePage.input_loanExpenseAmount('200.10')

        with allure.step("选择支付方式"):
            self.newPurchasePrepaymentBoePage.selectPaymentMethod('hc挂账-不支付')

        with allure.step("点击单据提交"):
            self.newPurchasePrepaymentBoePage.click_boeSubmitButton()
        with allure.step("点击单据关闭按钮"):
            self.newPurchasePrepaymentBoePage.click_close()

        with allure.step("进行单据生成校验"):
            self.newPurchasePrepaymentBoePage.click_more()
            self.newPurchasePrepaymentBoePage.input_boeNumQuery(boeNum)
            self.newPurchasePrepaymentBoePage.click_queryButton()

        with allure.step("断言结果：{}".format(self.newPurchasePrepaymentBoePage.checkBoeNumExistIsOrNot(boeNum))):
            assert self.newPurchasePrepaymentBoePage.checkBoeNumExistIsOrNot(boeNum) == True


    @allure.story("采购预付单费用报销界面业务审批")
    @allure.step("采购预付单费用报销界面业务审批步骤")
    @pytest.mark.dependency(depends=["submit"] )
    def test_businessApprove(self):
        logger.info(" ----- 单据业务审批开始 ----- ")
        global boeNum
        self.businessApprove = BusinessApprove(boeNum)
        content = self.businessApprove.boeBusinessApprove()
        logger.info(" ----- 单据业务审批开始 ----- ")
        assert content == '审批成功'


    @allure.story("采购预付单共享中心界面财务审批")
    @allure.step("采购预付单共享中心界面财务审批步骤")
    @pytest.mark.dependency(depends=["submit"])
    def test_sharingCenterApprove(self):
        logger.info(" ----- 单据财务审批开始 ----- ")
        global boeNum
        self.sharingCenterApprove = SharingCenterApprove(boeNum)
        self.sharingCenterApprove.sharingCenterApproveChuShen()
        self.sharingCenterApprove.sharingCenterApproveFuShen()
        logger.info(" ----- 单据财务审批结束 ----- ")






