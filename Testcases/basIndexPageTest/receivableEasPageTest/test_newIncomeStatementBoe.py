# -*- coding:utf-8 -*-
import allure
import pytest

from PageClass.basIndexPageClass.receivableEasPageClass.newIncomeStatementBoePage import NewIncomeStatementBoePage
from Testcases.common.boeBusinessApprove import BusinessApprove
from Testcases.common.boeSharingCenterApprove import SharingCenterApprove
from Testcases.common.loginDepend import LoginDepend
from Util import logger
from Util.util import getNowTime, getPicturePath



@allure.feature("收入报账单流程")
class TestNewIncomeStatementBoe():

    boeNum = globals()

    def setup_class(self):
        self.publicLogin = LoginDepend('basHost', 'user')
        self.newIncomeStatementBoePage = NewIncomeStatementBoePage(self.publicLogin.driver)

    def teardown_class(self):
        self.newIncomeStatementBoePage.driver.quit()

    @allure.story("收入报账单业务报账界面单据提交")
    @allure.step("差旅申请单业务报账界面单据提交步骤")
    @allure.severity("blocker")
    @pytest.mark.dependency(name='submit')
    def test_newIncomeStatementBoe(self, newIncomeStatementBoe_testdata):
        try:

            logger.info(" ----- 单据提交流程开始 ----- ")

            with allure.step("点击选择收入收款页面"):
                self.newIncomeStatementBoePage.selectTabType('收入收款')
            with allure.step("进入收入报账单单据提交页面"):
                self.newIncomeStatementBoePage.boeRntry('收入报账')

            global boeNum
            boeNum = self.newIncomeStatementBoePage.getBoeNum()

            with allure.step("选择业务类型"):
                self.newIncomeStatementBoePage.input_operationType(newIncomeStatementBoe_testdata['operationType'])
            with allure.step("输入备注"):
                self.newIncomeStatementBoePage.input_boeAbstract(newIncomeStatementBoe_testdata['boeAbstract'])

            with allure.step("选择客户"):
                self.newIncomeStatementBoePage.selectVendor(newIncomeStatementBoe_testdata['vendor']['vendorCode'], vendorName=newIncomeStatementBoe_testdata['vendor']['vendorName'])
            # with allure.step("选择关联合同"):
            #     self.newIncomeStatementBoePage.selectContract(newIncomeStatementBoe_testdata['contract'])
            with allure.step("输入订单编号"):
                self.newIncomeStatementBoePage.input_orderNumber(newIncomeStatementBoe_testdata['orderNumber'])
            with allure.step("选择业务类型"):
                self.newIncomeStatementBoePage.input_operationSubType(newIncomeStatementBoe_testdata['operationSubType'])
            with allure.step("选择利润中心"):
                self.newIncomeStatementBoePage.selectExpenseDept(newIncomeStatementBoe_testdata['expenseDept']['deptCode'], deptName = newIncomeStatementBoe_testdata['expenseDept']['deptName'])
            with allure.step("输入金额"):
                self.newIncomeStatementBoePage.input_incomeDetailExpenseAmount(newIncomeStatementBoe_testdata['expenseAmount'])
            with allure.step("输入税额"):
                self.newIncomeStatementBoePage.input_incomeDetailTaxAmount(newIncomeStatementBoe_testdata['taxAmount'])

            with allure.step("点击单据提交"):
                self.newIncomeStatementBoePage.click_boeSubmitButton()
            with allure.step("点击单据关闭按钮"):
                self.newIncomeStatementBoePage.click_close()

            with allure.step("进行单据生成校验"):
                self.newIncomeStatementBoePage.click_more()
                self.newIncomeStatementBoePage.input_boeNumQuery(boeNum)
                self.newIncomeStatementBoePage.click_queryButton()

            with allure.step("断言结果：{}".format(self.newIncomeStatementBoePage.checkBoeNumExistIsOrNot(boeNum))):
                assert self.newIncomeStatementBoePage.checkBoeNumExistIsOrNot(boeNum) == True

            logger.info(" ----- 单据提交流程结束 ----- ")

        except Exception as e:

            logger.error("出现异常，异常信息为：{}".format(type(e)))
            code = 'wrong'
            timeNow = getNowTime()
            self.newIncomeStatementBoePage.screenshot(code, timeNow)
            allure.attach.file(getPicturePath(code, timeNow), name=timeNow + code + "screenshot",
                               attachment_type=allure.attachment_type.PNG)
            self.newIncomeStatementBoePage.driver.quit()
            assert 1 == 0

        else:
            logger.info("测试用例执行成功")
            code = 'success'
            timeNow = getNowTime()
            self.newIncomeStatementBoePage.screenshot(code, timeNow)
            allure.attach.file(getPicturePath(code, timeNow), name=timeNow + code + "screenshot",
                               attachment_type=allure.attachment_type.PNG)
            assert 1 == 1

    @allure.story("收入报账单费用报销界面业务审批")
    @allure.step("收入报账单费用报销界面业务审批步骤")
    @pytest.mark.dependency(depends=["submit"] )
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
        self.sharingCenterApprove.sharingCenterApproveChuShen()
        self.sharingCenterApprove.sharingCenterApproveFuShen()
        logger.info(" ----- 单据财务审批结束 ----- ")