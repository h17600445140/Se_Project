# -*- coding:utf-8 -*-
import allure
import pytest

from PageClass.basIndexPageClass.fundbillEasPageClass.newFundAllocationBoePage import NewFundAllocationBoePage
from Testcases.common.boeBusinessApprove import BusinessApprove
from Testcases.common.boeSharingCenterApprove import SharingCenterApprove
from Testcases.common.loginDepend import LoginDepend
from Util import logger


@allure.feature("资金调拨报账单(新)流程")
class TestNewFundAllocationBoe():

    boeNum = globals()

    def setup_class(self):
        self.login = LoginDepend('basHost', 'user')
        self.newFundAllocationBoePage = NewFundAllocationBoePage(self.login.driver)

    def teardown_class(self):
        # self.newFundAllocationBoePage.driver.quit()
        pass

    @allure.story("资金调拨报账单（新）业务报账界面单据提交")
    @allure.step("资金调拨报账单（新）业务报账界面单据提交步骤")
    @allure.severity("blocker")
    @pytest.mark.dependency(name='submit')
    def test_newFundAllocationBoe(self):

        logger.info(" ----- 单据提交流程开始 ----- ")

        with allure.step("点击选择资金票据页面"):
            self.newFundAllocationBoePage.selectTabType('资金票据')
        with allure.step("进入资金调拨报账单（新）单据提交页面"):
            self.newFundAllocationBoePage.boeRntry('资金调拨报账单(新)')

        global boeNum
        boeNum = self.newFundAllocationBoePage.getBoeNum()

        with allure.step("选择业务类型"):
            self.newFundAllocationBoePage.input_operationType('UI通用')
        with allure.step("输入备注"):
            self.newFundAllocationBoePage.input_boeAbstract('测试票据调拨单（新）')

        with allure.step("选择付款账户"):
            self.newFundAllocationBoePage.selectReceiveVendor('UI账户')

        with allure.step("添加账户"):
            self.newFundAllocationBoePage.addAccount('UI供应商1')

        with allure.step("输入调拨金额"):
            self.newFundAllocationBoePage.input_transferAmount('100.00')

        with allure.step("点击单据提交"):
            self.newFundAllocationBoePage.click_boeSubmitButton()
        with allure.step("点击单据关闭按钮"):
            self.newFundAllocationBoePage.click_close()

        with allure.step("进行单据生成校验"):
            self.newFundAllocationBoePage.click_more()
            self.newFundAllocationBoePage.input_boeNumQuery(boeNum)
            self.newFundAllocationBoePage.click_queryButton()

        with allure.step("断言结果：{}".format(self.newFundAllocationBoePage.checkBoeNumExistIsOrNot(boeNum))):
            assert self.newFundAllocationBoePage.checkBoeNumExistIsOrNot(boeNum) == True


    @allure.story("资金调拨报账单（新）费用报销界面业务审批")
    @allure.step("资金调拨报账单（新）费用报销界面业务审批步骤")
    @pytest.mark.dependency(depends=["submit"] )
    def test_businessApprove(self):
        logger.info(" ----- 单据业务审批开始 ----- ")
        global boeNum
        self.businessApprove = BusinessApprove(boeNum)
        content = self.businessApprove.boeBusinessApprove()
        logger.info(" ----- 单据业务审批开始 ----- ")
        assert content == '审批成功'


    @allure.story("资金调拨报账单（新）共享中心界面财务审批")
    @allure.step("资金调拨报账单（新）共享中心界面财务审批步骤")
    @pytest.mark.dependency(depends=["submit"])
    def test_sharingCenterApprove(self):
        logger.info(" ----- 单据财务审批开始 ----- ")
        global boeNum
        self.sharingCenterApprove = SharingCenterApprove(boeNum)
        self.sharingCenterApprove.sharingCenterApproveChuShen()
        self.sharingCenterApprove.sharingCenterApproveFuShen()
        logger.info(" ----- 单据财务审批结束 ----- ")
