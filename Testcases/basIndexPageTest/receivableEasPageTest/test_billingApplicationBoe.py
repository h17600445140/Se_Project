# -*- coding:utf-8 -*-
import allure
import pytest

from PageClass.basIndexPageClass.receivableEasPageClass.billingApplicationBoePage import BillingApplicationBoePage
from Testcases.common.boeBusinessApprove import BusinessApprove
from Testcases.common.boeSharingCenterApprove import SharingCenterApprove
from Testcases.common.loginDepend import LoginDepend
from Util import logger


@allure.feature("开票申请单流程")
class TestBillingApplicationBoe():

    boeNum = globals()

    def setup_class(self):
        self.publicLogin = LoginDepend('basHost', 'user')
        self.billingApplicationBoePage = BillingApplicationBoePage(self.publicLogin.driver)

    def teardown_class(self):
        # self.billingApplicationBoePage.driver.quit()
        pass

    @allure.story("开票申请单业务报账界面单据提交")
    @allure.step("开票申请单业务报账界面单据提交步骤")
    @allure.severity("blocker")
    @pytest.mark.dependency(name='submit')
    def test_billingApplicationBoe(self):

        logger.info(" ----- 单据提交流程开始 ----- ")

        with allure.step("点击选择收入收款页面"):
            self.billingApplicationBoePage.selectTabType('收入收款')
        with allure.step("进入收入报账单单据提交页面"):
            self.billingApplicationBoePage.boeRntry('开票申请单')

        global boeNum
        boeNum = self.billingApplicationBoePage.getBoeNum()

        self.billingApplicationBoePage.selectBuyer('hc客户001')

        self.billingApplicationBoePage.selectContract('hcKH000002')

        self.billingApplicationBoePage.input_orderNumber('hcOrder000001')

        self.billingApplicationBoePage.input_project('hc项目1')

        self.billingApplicationBoePage.selectGoods('hcProduct001', goodsName = '商品名称')

        self.billingApplicationBoePage.input_goodsAmount('10')

        self.billingApplicationBoePage.input_goodPrice('100.00')

        self.billingApplicationBoePage.input_goodsExpenseAmount('1000.00')

        self.billingApplicationBoePage.input_goodsTaxRate('5')

        self.billingApplicationBoePage.selectSaler('hc法人')

        with allure.step("点击单据提交"):
            self.billingApplicationBoePage.click_boeSubmitButton()
        with allure.step("点击单据关闭按钮"):
            self.billingApplicationBoePage.click_close()

        with allure.step("进行单据生成校验"):
            self.billingApplicationBoePage.click_more()
            self.billingApplicationBoePage.input_boeNumQuery(boeNum)
            self.billingApplicationBoePage.click_queryButton()

        with allure.step("断言结果：{}".format(self.billingApplicationBoePage.checkBoeNumExistIsOrNot(boeNum))):
            assert self.billingApplicationBoePage.checkBoeNumExistIsOrNot(boeNum) == True

        logger.info(" ----- 单据提交流程结束 ----- ")

    @allure.story("开票申请单费用报销界面业务审批")
    @allure.step("开票申请单费用报销界面业务审批步骤")
    @pytest.mark.dependency(depends=["submit"])
    def test_businessApprove(self):
        logger.info(" ----- 单据业务审批开始 ----- ")
        global boeNum
        self.businessApprove = BusinessApprove(boeNum)
        content = self.businessApprove.boeBusinessApprove()
        logger.info(" ----- 单据业务审批开始 ----- ")
        assert content == '审批成功'

    @allure.story("收入报账单共享中心界面财务审批")
    @allure.step("收入报账单共享中心界面财务审批步骤")
    @pytest.mark.dependency(depends=["submit"])
    def test_sharingCenterApprove(self):
        logger.info(" ----- 单据财务审批开始 ----- ")
        global boeNum
        self.sharingCenterApprove = SharingCenterApprove(boeNum)
        invoiceDataDict = {'invoiceNo': '880000000009', 'invoiceCode': '88000009', 'invoiceDate': '2020-1-1',
                'invoiceFee': '1000.00', 'invoiceTax': '47.62', 'invoiceRemark': '测试开票申请单'}
        self.sharingCenterApprove.sharingCenterApproveChuShen(modify=True, **invoiceDataDict)
        self.sharingCenterApprove.sharingCenterApproveFuShen()
        logger.info(" ----- 单据财务审批结束 ----- ")




