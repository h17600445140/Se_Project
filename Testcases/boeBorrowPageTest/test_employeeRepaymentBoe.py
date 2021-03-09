# -*- coding:utf-8 -*-
import datetime
import os
from time import sleep

import allure
import pytest

from PageClass.boeBorrowPageClass.employeeRepaymentBoePage import EmployeeRepaymentBoePage
from Testcases.common.boeBusinessApprove import BusinessApprove
from Testcases.common.boeSharingCenterApprove import SharingCenterApprove
from Testcases.common.loginDepend import LoginDepend
from Util import logger
from Util.util import getNowTime, getPicturePath, readBoeNum


@allure.feature("员工还款单流程")
class TestEmployeeRepaymentBoe(object):

    boeNum = globals()

    def setup_class(self):
        boeNumPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'boeNum.json')
        self.login = LoginDepend('easHost', 'user')
        self.employeeRepaymentBoePage = EmployeeRepaymentBoePage(self.login.driver)
        self.loadBoeNum = readBoeNum(boeNumPath)

    def teardown_class(self):
        self.employeeRepaymentBoePage.driver.quit()


    @allure.story("员工还款单费用报销界面单据提交")
    @allure.step("员工还款单费用报销界面单据提交步骤")
    @allure.severity("blocker")
    @pytest.mark.dependency(name='submit')
    def test_employeeRepayment(self, employeeRepaymentBoe_testdata):
        try:
            logger.info(" ----- 单据流程开始 ----- ")
            with allure.step("打开借款还款单据选择页面"):
                sleep(3)
                self.employeeRepaymentBoePage.open_boeBorrow()
            with allure.step("打开的单据类型为：{} ,选择的单据业务类型为: {}".format('员工还款单', employeeRepaymentBoe_testdata['operationType'])):
                try:
                    self.employeeRepaymentBoePage.open_boe('员工还款单', employeeRepaymentBoe_testdata['operationType'])
                except:
                    sleep(3)
                    logger.error(" Don't find Boe, Try again")
                    self.employeeRepaymentBoePage.open_boe('员工还款单', employeeRepaymentBoe_testdata['operationType'])

            global boeNum
            boeNum = self.employeeRepaymentBoePage.getBoeNum()

            self.boeFee = self.employeeRepaymentBoePage.selectWriteOffBoe(self.loadBoeNum)

            with allure.step("输入业务类型"):
                self.employeeRepaymentBoePage.input_operationType(employeeRepaymentBoe_testdata['operationType'])
            with allure.step("输入备注"):
                self.employeeRepaymentBoePage.input_boeAbstract(employeeRepaymentBoe_testdata['boeAbstract'])

            with allure.step("输入还款方式"):
                self.employeeRepaymentBoePage.selectReplaymentType(employeeRepaymentBoe_testdata['operationSubType'])
            with allure.step("输入还款金额"):
                # self.employeeRepaymentBoePage.input_expenseAmount(self.boeFee)
                self.employeeRepaymentBoePage.input_expenseAmount('100..00')
            with allure.step("输入收款账户"):
                self.employeeRepaymentBoePage.selectCollectionAccount(employeeRepaymentBoe_testdata['favoriteId'])
            with allure.step("输入还款日期"):
                self.employeeRepaymentBoePage.selectLoanRepaymentDate(
                    datetime.datetime.now().strftime("%Y-%m-%d"))
            with allure.step("输入还困说明"):
                self.employeeRepaymentBoePage.input_remark(employeeRepaymentBoe_testdata['remark'])

            with allure.step("点击单据提交"):
                self.employeeRepaymentBoePage.click_boeSubmitButton()
            with allure.step("点击单据关闭按钮"):
                self.employeeRepaymentBoePage.click_close()

            with allure.step("进行单据生成校验"):
                self.employeeRepaymentBoePage.click_myBoeList()
                self.employeeRepaymentBoePage.click_moreButton()
                self.employeeRepaymentBoePage.input_boeNo(boeNum)
                self.employeeRepaymentBoePage.click_boeNoSelectButton()
                status = self.employeeRepaymentBoePage.selectResultIsOrNot(boeNum)

            logger.info(" ----- 单据提交流程结束 ----- ")
            assert status == True
        except Exception as e:
            logger.error("出现异常，异常信息为：{}".format(type(e)))
            code = 'wrong'
            timeNow = getNowTime()
            self.employeeRepaymentBoePage.screenshot(code, timeNow)
            allure.attach.file(getPicturePath(code, timeNow), name=timeNow + code + "screenshot",
                               attachment_type=allure.attachment_type.PNG)
            self.employeeRepaymentBoePage.driver.quit()
            assert 1 == 0

        else:
            logger.info("测试用例执行成功")
            code = 'success'
            timeNow = getNowTime()
            self.employeeRepaymentBoePage.screenshot(code, timeNow)
            allure.attach.file(getPicturePath(code, timeNow), name=timeNow + code + "screenshot",
                               attachment_type=allure.attachment_type.PNG)
            assert 1 == 1


    @allure.story("员工还款单费用报销界面业务审批")
    @allure.step("员工还款单费用报销界面业务审批步骤")
    @pytest.mark.dependency(depends=["submit"] )
    def test_businessApprove(self):
        logger.info(" ----- 单据业务审批开始 ----- ")
        global boeNum
        self.businessApprove = BusinessApprove(boeNum)
        content = self.businessApprove.boeBusinessApprove()
        logger.info(" ----- 单据业务审批开始 ----- ")
        assert content == '审批成功'


    @allure.story("员工还款单共享中心界面财务审批")
    @allure.step("员工还款单共享中心界面财务审批步骤")
    @pytest.mark.dependency(depends=["submit"])
    def test_sharingCenterApprove(self):
        logger.info(" ----- 单据财务审批开始 ----- ")
        global boeNum
        self.sharingCenterApprove = SharingCenterApprove(boeNum)
        self.sharingCenterApprove.sharingCenterApproveChuShen()
        self.sharingCenterApprove.sharingCenterApproveFuShen()
        logger.info(" ----- 单据财务审批结束 ----- ")

