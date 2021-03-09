# -*- coding:utf-8 -*-
import os
from time import sleep

import allure
import pytest

from PageClass.boeBorrowPageClass.employeeLoansBoePage import EmployeeLoansBoePage
from Testcases.common.boeBusinessApprove import BusinessApprove
from Testcases.common.boeSharingCenterApprove import SharingCenterApprove
from Testcases.common.loginDepend import LoginDepend
from Util import logger
from Util.util import getNowTime, getPicturePath, writeBoeNum


@allure.feature("员工借款单流程")
class TestEmployeeLoadBoe(object):

    boeNum = globals()

    def setup_class(self):

        self.login = LoginDepend('easHost', 'user')
        self.employeeLoansBoePage = EmployeeLoansBoePage(self.login.driver)

    def teardown_class(self):
        self.employeeLoansBoePage.driver.quit()

    @allure.story("员工借款单费用报销界面单据提交")
    @allure.step("员工借款单费用报销界面单据提交步骤")
    @allure.severity("blocker")
    @pytest.mark.dependency(name='submit')
    def test_employeeLoad(self, employeeLoadBoe_testdata):
        try:
            logger.info(" ----- 单据流程开始 ----- ")
            with allure.step("打开借款还款单据选择页面"):
                sleep(3)
                self.employeeLoansBoePage.open_boeBorrow()
            with allure.step("打开的单据类型为：{} ,选择的单据业务类型为: {}".format('员工借款单', employeeLoadBoe_testdata['operationType'])):
                try:
                    self.employeeLoansBoePage.open_boe('员工借款单', employeeLoadBoe_testdata['operationType'])
                except:
                    sleep(3)
                    logger.error(" Don't find Boe, Try again")
                    self.employeeLoansBoePage.open_boe('员工借款单', employeeLoadBoe_testdata['operationType'])

            global boeNum
            boeNum = self.employeeLoansBoePage.getBoeNum()

            with allure.step("输入业务类型"):
                self.employeeLoansBoePage.input_operationType(employeeLoadBoe_testdata['operationType'])
            with allure.step("输入备注"):
                self.employeeLoansBoePage.input_boeAbstract(employeeLoadBoe_testdata['boeAbstract'])

            with allure.step("输入业务类型"):
                self.employeeLoansBoePage.input_operationSubTypeId(employeeLoadBoe_testdata['operationSubTypeId'])
            with allure.step("输入总金额"):
                self.employeeLoansBoePage.input_expenseAmount(employeeLoadBoe_testdata['expenseAmount'])
            with allure.step("输入项目"):
                self.employeeLoansBoePage.input_projectId(employeeLoadBoe_testdata['projectName'])

            with allure.step("点击单据提交"):
                self.employeeLoansBoePage.click_boeSubmitButton()
            with allure.step("点击单据关闭按钮"):
                self.employeeLoansBoePage.click_close()

            with allure.step("进行单据生成校验"):
                self.employeeLoansBoePage.click_myBoeList()
                self.employeeLoansBoePage.click_moreButton()
                self.employeeLoansBoePage.input_boeNo(boeNum)
                self.employeeLoansBoePage.click_boeNoSelectButton()
                status = self.employeeLoansBoePage.selectResultIsOrNot(boeNum)

            logger.info(" ----- 单据提交流程结束 ----- ")
            assert status == True
        except Exception as e:
            logger.error("出现异常，异常信息为：{}".format(type(e)))
            code = 'wrong'
            timeNow = getNowTime()
            self.employeeLoansBoePage.screenshot(code, timeNow)
            allure.attach.file(getPicturePath(code, timeNow), name=timeNow + code + "screenshot",
                               attachment_type=allure.attachment_type.PNG)
            self.employeeLoansBoePage.driver.quit()
            assert 1 == 0

        else:
            logger.info("测试用例执行成功")
            code = 'success'
            timeNow = getNowTime()
            self.employeeLoansBoePage.screenshot(code, timeNow)
            allure.attach.file(getPicturePath(code, timeNow), name=timeNow + code + "screenshot",
                               attachment_type=allure.attachment_type.PNG)

            boeNumPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'boeNum.json')
            writeBoeNum(boeNumPath, boeNum)

            assert 1 == 1


    @allure.story("员工借款单费用报销界面业务审批")
    @allure.step("员工借款单费用报销界面业务审批步骤")
    @pytest.mark.dependency(depends=["submit"] )
    def test_businessApprove(self):
        logger.info(" ----- 单据业务审批开始 ----- ")
        global boeNum
        self.businessApprove = BusinessApprove(boeNum)
        content = self.businessApprove.boeBusinessApprove()
        logger.info(" ----- 单据业务审批结束 ----- ")
        assert content == '审批成功'


    @allure.story("员工借款单共享中心界面财务审批")
    @allure.step("员工借款单共享中心界面财务审批步骤")
    @pytest.mark.dependency(depends=["submit"])
    def test_sharingCenterApprove(self):
        logger.info(" ----- 单据财务审批开始 ----- ")
        global boeNum
        self.sharingCenterApprove = SharingCenterApprove(boeNum)
        self.sharingCenterApprove.sharingCenterApproveChuShen()
        self.sharingCenterApprove.sharingCenterApproveFuShen()
        logger.info(" ----- 单据财务审批结束 ----- ")


if __name__ == '__main__':
    print(os.path.dirname(os.path.realpath(__file__)))
