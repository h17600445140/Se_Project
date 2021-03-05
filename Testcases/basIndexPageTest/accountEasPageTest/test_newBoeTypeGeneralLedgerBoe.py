# -*- coding:utf-8 -*-
import datetime

import allure
import pytest

from PageClass.basIndexPageClass.accountEasPageClass.newBoeTypeGeneralLedgerBoePage import \
    NewBoeTypeGeneralLedgerBoePage
from Testcases.common.boeBusinessApprove import BusinessApprove
from Testcases.common.boeSharingCenterApprove import SharingCenterApprove
from Testcases.common.loginDepend import LoginDepend
from Util import logger


@allure.feature("总账单流程")
class TestNewBoeTypeGeneralLedgerBoe():

    boeNum = globals()

    def setup_class(self):
        self.login = LoginDepend('basHost', 'user')
        self.newBoeTypeGeneralLedgerBoePage = NewBoeTypeGeneralLedgerBoePage(self.login.driver)

    def teardown_class(self):
        self.newBoeTypeGeneralLedgerBoePage.driver.quit()

    @allure.story("总账单业务报账界面单据提交")
    @allure.step("总账单业务报账界面单据提交步骤")
    @allure.severity("blocker")
    @pytest.mark.dependency(name='submit')
    def test_newBoeTypeGeneralLedgerBoe(self):

        logger.info(" ----- 单据提交流程开始 ----- ")

        with allure.step("点击选择财务记账页面"):
            self.newBoeTypeGeneralLedgerBoePage.selectTabType('财务记账')
        with allure.step("进入总账单单据提交页面"):
            self.newBoeTypeGeneralLedgerBoePage.boeRntry('总账单')

        global boeNum
        boeNum = self.newBoeTypeGeneralLedgerBoePage.getBoeNum()

        with allure.step("选择业务类型"):
            self.newBoeTypeGeneralLedgerBoePage.input_operationType('UI通用')
        with allure.step("选择总账记账日期"):
            self.newBoeTypeGeneralLedgerBoePage.select_glDate(datetime.datetime.now().strftime("%Y-%m-%d"))

        with allure.step("输入摘要"):
            self.newBoeTypeGeneralLedgerBoePage.input_voucherRemark('测试')
        with allure.step("选择会计科目"):
            self.newBoeTypeGeneralLedgerBoePage.input_voucherAccount('UI科目1')
        with allure.step("输入金额"):
            self.newBoeTypeGeneralLedgerBoePage.input_voucherDebitAmount('100.00')

        with allure.step("点击新增凭证分录按钮"):
            self.newBoeTypeGeneralLedgerBoePage.click_addVoucherButton()

        with allure.step("输入摘要"):
            self.newBoeTypeGeneralLedgerBoePage.input_voucherRemark('测试', count='1')
        with allure.step("选择会计科目"):
            self.newBoeTypeGeneralLedgerBoePage.input_voucherAccount('UI科目2', count='1')
        with allure.step("输入金额"):
            self.newBoeTypeGeneralLedgerBoePage.input_voucherCreditAmount('100.00', count='1')

        with allure.step("点击单据提交"):
            self.newBoeTypeGeneralLedgerBoePage.click_boeSubmitButton()
        with allure.step("点击单据关闭按钮"):
            self.newBoeTypeGeneralLedgerBoePage.click_close()

        with allure.step("进行单据生成校验"):
            self.newBoeTypeGeneralLedgerBoePage.click_more()
            self.newBoeTypeGeneralLedgerBoePage.input_boeNumQuery(boeNum)
            self.newBoeTypeGeneralLedgerBoePage.click_queryButton()

        with allure.step("断言结果：{}".format(self.newBoeTypeGeneralLedgerBoePage.checkBoeNumExistIsOrNot(boeNum))):
            assert self.newBoeTypeGeneralLedgerBoePage.checkBoeNumExistIsOrNot(boeNum) == True


    @allure.story("总账单费用报销界面业务审批")
    @allure.step("总账单费用报销界面业务审批步骤")
    @pytest.mark.dependency(depends=["submit"] )
    def test_businessApprove(self):
        logger.info(" ----- 单据业务审批开始 ----- ")
        global boeNum
        self.businessApprove = BusinessApprove(boeNum)
        content = self.businessApprove.boeBusinessApprove()
        logger.info(" ----- 单据业务审批开始 ----- ")
        assert content == '审批成功'


    @allure.story("总账单共享中心界面财务审批")
    @allure.step("总账单共享中心界面财务审批步骤")
    @pytest.mark.dependency(depends=["submit"])
    def test_sharingCenterApprove(self):
        logger.info(" ----- 单据财务审批开始 ----- ")
        global boeNum
        self.sharingCenterApprove = SharingCenterApprove(boeNum)
        self.sharingCenterApprove.sharingCenterApproveChuShen()
        self.sharingCenterApprove.sharingCenterApproveFuShen()
        logger.info(" ----- 单据财务审批结束 ----- ")


