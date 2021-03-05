# -*- coding:utf-8 -*-
import allure
import pytest

from PageClass.basIndexPageClass.fundbillEasPageClass.newBillAllocationBoePage import NewBillAllocationBoePage
from Testcases.common.boeBusinessApprove import BusinessApprove
from Testcases.common.boeSharingCenterApprove import SharingCenterApprove
from Testcases.common.loginDepend import LoginDepend
from Util import logger, record


@allure.feature("票据调拨单（新）流程")
class TestNewBillAllocationBoe():


    boeNum = globals()

    def setup_class(self):
        self.login = LoginDepend('basHost', 'user')
        self.newBillAllocationBoePage = NewBillAllocationBoePage(self.login.driver)

    def teardown_class(self):
        self.newBillAllocationBoePage.driver.quit()

    @allure.story("票据调拨单（新）业务报账界面单据提交")
    @allure.step("票据调拨单（新）业务报账界面单据提交步骤")
    @allure.severity("blocker")
    @pytest.mark.dependency(name='submit')
    def test_newBillAllocationBoe(self):

        logger.info(" ----- 单据提交流程开始 ----- ")

        with allure.step("点击选择资金票据页面"):
            self.newBillAllocationBoePage.selectTabType('资金票据')
        with allure.step("进入票据调拨报账单（新）单据提交页面"):
            self.newBillAllocationBoePage.boeRntry('票据调拨报账单（新）')

        global boeNum
        boeNum = self.newBillAllocationBoePage.getBoeNum()

        with allure.step("选择业务类型"):
            self.newBillAllocationBoePage.input_operationType('UI通用')
        with allure.step("输入备注"):
            self.newBillAllocationBoePage.input_boeAbstract('测试票据调拨单（新）')

        with allure.step("选择收票方"):
            self.newBillAllocationBoePage.selectReceiveVendor('UI供应商1')

        postalOrder = record.readDataFromRecord(type='postalOrderData')['postalOrder1']

        with allure.step("关联票据"):
            self.newBillAllocationBoePage.associateBill(postalOrder)

        with allure.step("点击单据提交"):
            self.newBillAllocationBoePage.click_boeSubmitButton()
        with allure.step("点击单据关闭按钮"):
            self.newBillAllocationBoePage.click_close()

        with allure.step("进行单据生成校验"):
            self.newBillAllocationBoePage.click_more()
            self.newBillAllocationBoePage.input_boeNumQuery(boeNum)
            self.newBillAllocationBoePage.click_queryButton()

        with allure.step("断言结果：{}".format(self.newBillAllocationBoePage.checkBoeNumExistIsOrNot(boeNum))):
            assert self.newBillAllocationBoePage.checkBoeNumExistIsOrNot(boeNum) == True


    @allure.story("票据调拨单（新）费用报销界面业务审批")
    @allure.step("票据调拨单（新）费用报销界面业务审批步骤")
    @pytest.mark.dependency(depends=["submit"] )
    def test_businessApprove(self):
        logger.info(" ----- 单据业务审批开始 ----- ")
        global boeNum
        self.businessApprove = BusinessApprove(boeNum)
        content = self.businessApprove.boeBusinessApprove()
        logger.info(" ----- 单据业务审批开始 ----- ")
        assert content == '审批成功'


    @allure.story("票据调拨单（新）共享中心界面财务审批")
    @allure.step("票据调拨单（新）共享中心界面财务审批步骤")
    @pytest.mark.dependency(depends=["submit"])
    def test_sharingCenterApprove(self):
        logger.info(" ----- 单据财务审批开始 ----- ")
        global boeNum
        self.sharingCenterApprove = SharingCenterApprove(boeNum)
        self.sharingCenterApprove.sharingCenterApproveChuShen()
        self.sharingCenterApprove.sharingCenterApproveFuShen()
        logger.info(" ----- 单据财务审批结束 ----- ")