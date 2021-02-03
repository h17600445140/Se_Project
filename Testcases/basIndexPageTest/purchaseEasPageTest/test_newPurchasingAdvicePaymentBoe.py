# -*- coding:utf-8 -*-
import allure
import pytest

from PageClass.basIndexPageClass.purchaseEasPageClass.newPurchasingAdvicePaymentBoePage import \
    NewPurchasingAdvicePaymentBoePage
from Testcases.common.boeBusinessApprove import BusinessApprove
from Testcases.common.boeSharingCenterApprove import SharingCenterApprove
from Testcases.common.loginDepend import LoginDepend
from Util import logger


@allure.feature("采购付款单流程")
class TestNewPurchasingAdvicePaymentBoe():

    boeNum = globals()

    def setup_class(self):
        self.login = LoginDepend('basHost', 'user')
        self.newPurchasingAdvicePaymentBoePage = NewPurchasingAdvicePaymentBoePage(self.login.driver)

    def teardown_class(self):
        # self.newPurchasingAdvicePaymentBoePage.driver.quit()
        pass

    @allure.story("采购付款单业务报账界面单据提交")
    @allure.step("采购付款单业务报账界面单据提交步骤")
    @allure.severity("blocker")
    @pytest.mark.dependency(name='submit')
    def test_newPurchasingAdvicePaymentBoe(self):

        logger.info(" ----- 单据提交流程开始 ----- ")

        with allure.step("点击选择采购付款页面"):
            self.newPurchasingAdvicePaymentBoePage.selectTabType('采购付款')
        with allure.step("进入成本暂估单（旧）单据提交页面"):
            self.newPurchasingAdvicePaymentBoePage.boeRntry('采购付款')

        global boeNum
        boeNum = self.newPurchasingAdvicePaymentBoePage.getBoeNum()

        with allure.step("选择业务类型"):
            self.newPurchasingAdvicePaymentBoePage.input_operationType('付款')
        with allure.step("输入备注"):
            self.newPurchasingAdvicePaymentBoePage.input_boeAbstract('测试采购付款但')

        with allure.step("选择供应商"):
            self.newPurchasingAdvicePaymentBoePage.selectVendor('hcGYS1', vendorName='hc供应商1')
        # with allure.step("选择关联合同"):
        #     self.newPurchasingAdvicePaymentBoePage.selectContract('hc00000021')

        with allure.step("关联挂账款"):
            self.newPurchasingAdvicePaymentBoePage.selectAccountReceivable('hcGroup-BX210203126')

        with allure.step("点击单据提交"):
            self.newPurchasingAdvicePaymentBoePage.click_boeSubmitButton()
        with allure.step("点击单据关闭按钮"):
            self.newPurchasingAdvicePaymentBoePage.click_close()

        with allure.step("进行单据生成校验"):
            self.newPurchasingAdvicePaymentBoePage.click_more()
            self.newPurchasingAdvicePaymentBoePage.input_boeNumQuery(boeNum)
            self.newPurchasingAdvicePaymentBoePage.click_queryButton()

        with allure.step("断言结果：{}".format(self.newPurchasingAdvicePaymentBoePage.checkBoeNumExistIsOrNot(boeNum))):
            assert self.newPurchasingAdvicePaymentBoePage.checkBoeNumExistIsOrNot(boeNum) == True


    @allure.story("采购付款单费用报销界面业务审批")
    @allure.step("采购付款单费用报销界面业务审批步骤")
    @pytest.mark.dependency(depends=["submit"] )
    def test_businessApprove(self):
        logger.info(" ----- 单据业务审批开始 ----- ")
        global boeNum
        self.businessApprove = BusinessApprove(boeNum)
        content = self.businessApprove.boeBusinessApprove()
        logger.info(" ----- 单据业务审批开始 ----- ")
        assert content == '审批成功'


    @allure.story("采购付款单共享中心界面财务审批")
    @allure.step("采购付款单共享中心界面财务审批步骤")
    @pytest.mark.dependency(depends=["submit"])
    def test_sharingCenterApprove(self):
        logger.info(" ----- 单据财务审批开始 ----- ")
        global boeNum
        self.sharingCenterApprove = SharingCenterApprove(boeNum)
        self.sharingCenterApprove.sharingCenterApproveChuShen()
        self.sharingCenterApprove.sharingCenterApproveFuShen()
        logger.info(" ----- 单据财务审批结束 ----- ")
