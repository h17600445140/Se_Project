# -*- coding:utf-8 -*-
import datetime
import random
import string
from time import sleep

import allure
import pytest

from PageClass.boeReimbursementPageClass.newDailyExpenseBoePage import NewDailyExpenseBoePage
from Testcases.common.boeBusinessApprove import BusinessApprove
from Testcases.common.boeSharingCenterApprove import SharingCenterApprove
from Testcases.common.loginDepend import LoginDepend
from Util import logger
from Util.util import getPicturePath, getNowTime
from Testcases.common import invoiceFactory



@allure.feature("日常费用报账单流程")
class TestNewDailyExpenseBoe():

    boeNum = globals()

    def setup_class(self):
        self.login = LoginDepend('easHost', 'user')
        self.newDailyExpenseBoePage = NewDailyExpenseBoePage(self.login.driver)

    def teardown_class(self):
        self.newDailyExpenseBoePage.driver.quit()


    @allure.story("日常费用报账单费用报销界面单据提交")
    @allure.step("日常费用报账单费用报销界面单据提交步骤")
    @allure.severity("blocker")
    @pytest.mark.dependency(name='submit')
    def test_newDailyExpense(self, newDailyExpenseBoe_testdata):
        try:
            logger.info(" ----- 单据流程开始 ----- ")
            with allure.step("打开费用报销单据选择页面"):
                sleep(3)
                self.newDailyExpenseBoePage.open_boeReimburse()
            with allure.step("打开的单据类型为：{} ,选择的单据业务类型为: {}".format('日常费用报账单', newDailyExpenseBoe_testdata['operationType'])):
                try:
                    self.newDailyExpenseBoePage.open_boe('日常费用报账单', newDailyExpenseBoe_testdata['operationType'])
                except:
                    sleep(3)
                    logger.error(" Don't find Boe, Try again")
                    self.newDailyExpenseBoePage.open_boe('日常费用报账单', newDailyExpenseBoe_testdata['operationType'])

            global boeNum
            boeNum = self.newDailyExpenseBoePage.getBoeNum()

            with allure.step("输入业务类型"):
                self.newDailyExpenseBoePage.input_operationType(newDailyExpenseBoe_testdata['operationType'])
            with allure.step("输入备注"):
                self.newDailyExpenseBoePage.input_boeAbstract(newDailyExpenseBoe_testdata['boeAbstract'])

            # with allure.step("选择关联发票"):
            #     self.newDailyExpenseBoePage.selectRelatedInvoice(newDailyExpenseBoe_testdata['relatedInvoice'])


            with allure.step("点击新增发票"):
                self.newDailyExpenseBoePage.click_addInvoiceButton()
                self.newDailyExpenseBoePage.click_invoiceType()
                invoiceFactory.get_invoice(self.login.driver, '增值税普通发票', 'boeInvoicePage').getTickets(
                    date = datetime.datetime.now().strftime('%Y-%m-%d'),
                    invoiceNo = ''.join(random.choice(string.digits) for _ in range(12)),
                    invoiceCode = ''.join(random.choice(string.digits) for _ in range(8)),
                    feeTotal = '100.00',
                    tax = '0.00',
                    checkCode = '123456')
            with allure.step("输入业务类型"):
                try:
                    self.newDailyExpenseBoePage.selectOperationSubType(newDailyExpenseBoe_testdata['operationSubType'])
                except:
                    sleep(1)
                    self.newDailyExpenseBoePage.selectOperationSubType(newDailyExpenseBoe_testdata['operationSubType'])

            with allure.step("选择部门"):
                self.newDailyExpenseBoePage.selectDepartment(newDailyExpenseBoe_testdata['deptCode'], newDailyExpenseBoe_testdata['deptName'])
            with allure.step("输入项目"):
                self.newDailyExpenseBoePage.input_projectId(newDailyExpenseBoe_testdata['projectName'])

            with allure.step("点击单据提交"):
                self.newDailyExpenseBoePage.click_boeSubmitButton()
            with allure.step("点击单据关闭按钮"):
                self.newDailyExpenseBoePage.click_close()

            with allure.step("进行单据生成校验"):
                self.newDailyExpenseBoePage.click_myBoeList()
                self.newDailyExpenseBoePage.click_moreButton()
                self.newDailyExpenseBoePage.input_boeNo(boeNum)
                self.newDailyExpenseBoePage.click_boeNoSelectButton()
                status = self.newDailyExpenseBoePage.selectResultIsOrNot(boeNum)

            logger.info(" ----- 单据提交流程结束 ----- ")
            assert status == True

        except Exception as e:
            logger.error("出现异常，异常信息为：{}".format(type(e)))
            code = 'wrong'
            timeNow = getNowTime()
            self.newDailyExpenseBoePage.screenshot(code, timeNow)
            allure.attach.file(getPicturePath(code, timeNow), name=timeNow + code + "screenshot",
                               attachment_type=allure.attachment_type.PNG)
            self.newDailyExpenseBoePage.driver.quit()
            assert 1 == 0

        else:
            logger.info("测试用例执行成功")
            code = 'success'
            timeNow = getNowTime()
            self.newDailyExpenseBoePage.screenshot(code, timeNow)
            allure.attach.file(getPicturePath(code, timeNow), name=timeNow + code + "screenshot",
                               attachment_type=allure.attachment_type.PNG)
            assert 1 == 1


    @allure.story("日常费用报账单费用报销界面业务审批")
    @allure.step("日常费用报账单费用报销界面业务审批步骤")
    @pytest.mark.dependency(depends=["submit"] )
    def test_businessApprove(self):
        logger.info(" ----- 单据业务审批开始 ----- ")
        global boeNum
        self.businessApprove = BusinessApprove(boeNum)
        content = self.businessApprove.boeBusinessApprove()
        logger.info(" ----- 单据业务审批开始 ----- ")
        assert content == '审批成功'


    @allure.story("日常费用报账单共享中心界面财务审批")
    @allure.step("日常费用报账单共享中心界面财务审批步骤")
    @pytest.mark.dependency(depends=["submit"])
    def test_sharingCenterApprove(self):
        logger.info(" ----- 单据财务审批开始 ----- ")
        global boeNum
        self.sharingCenterApprove = SharingCenterApprove(boeNum)
        self.sharingCenterApprove.sharingCenterApproveChuShen()
        self.sharingCenterApprove.sharingCenterApproveFuShen()
        logger.info(" ----- 单据财务审批结束 ----- ")