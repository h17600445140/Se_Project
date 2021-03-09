# -*- coding:utf-8 -*-
from time import sleep

import allure
import pytest
from PageClass.boeApplyPageClass.comFeeApplyBoePage import ComFeeApplyBoePage
from Testcases.common.boeBusinessApprove import BusinessApprove
from Testcases.common.boeSharingCenterApprove import SharingCenterApprove
from Testcases.common.loginDepend import LoginDepend
from Util import logger
from Util.util import getNowTime, getPicturePath



@allure.feature("通用费用申请单流程")
class TestComFeeApplyBoe(object):

    boeNum = globals()

    def setup_class(self):
        self.login = LoginDepend('easHost', 'user')
        self.comFeeApplyBoePage = ComFeeApplyBoePage(self.login.driver)

    def teardown_class(self):
        self.comFeeApplyBoePage.driver.quit()


    @allure.story("通用费用申请单费用报销界面单据提交")
    @allure.step("通用费用申请单费用报销界面单据提交步骤")
    @allure.severity("blocker")
    @pytest.mark.dependency(name='submit')
    def test_comFeeApply(self, comFeeApplyBoe_testdata):
        try:
            logger.info(" ----- 单据流程开始 ----- ")
            with allure.step("打开事项申请选择页面"):
                sleep(3)
                self.comFeeApplyBoePage.open_boeApply()
            with allure.step("打开的单据类型为：{} ,选择的单据业务类型为: {}".format('通用费用申请单', comFeeApplyBoe_testdata['operationType'])):
                try:
                    self.comFeeApplyBoePage.open_boe('通用费用申请单', comFeeApplyBoe_testdata['operationType'])
                except:
                    sleep(3)
                    logger.error(" Don't find Boe, Try again")
                    self.comFeeApplyBoePage.open_boe('通用费用申请单', comFeeApplyBoe_testdata['operationType'])

            global boeNum
            boeNum = self.comFeeApplyBoePage.getBoeNum()

            with allure.step("输入业务类型:"):
                self.comFeeApplyBoePage.input_operationType(comFeeApplyBoe_testdata['operationType'])
            with allure.step("输入备注"):
                self.comFeeApplyBoePage.input_boeAbstract(comFeeApplyBoe_testdata['boeAbstract'])

            with allure.step("选择申请类型"):
                self.comFeeApplyBoePage.input_operationSubTypeId(comFeeApplyBoe_testdata['operationSubTypeId'])
            with allure.step("输入申请金额"):
                self.comFeeApplyBoePage.input_expenseAmount(comFeeApplyBoe_testdata['expenseAmount'])
            with allure.step("输入申请说明"):
                self.comFeeApplyBoePage.input_remark(comFeeApplyBoe_testdata['remark'])

            with allure.step("点击单据提交"):
                self.comFeeApplyBoePage.click_boeSubmitButton()
            with allure.step("点击单据关闭按钮"):
                self.comFeeApplyBoePage.click_close()

            with allure.step("进行单据生成校验"):
                self.comFeeApplyBoePage.click_myBoeList()
                self.comFeeApplyBoePage.click_moreButton()
                self.comFeeApplyBoePage.input_boeNo(boeNum)
                self.comFeeApplyBoePage.click_boeNoSelectButton()
                status = self.comFeeApplyBoePage.selectResultIsOrNot(boeNum)

            logger.info(" ----- 单据提交流程结束 ----- ")
            assert status == True

        except Exception as e:
            logger.error("出现异常，异常信息为：{}".format(type(e)))
            code = 'wrong'
            timeNow = getNowTime()
            self.comFeeApplyBoePage.screenshot(code, timeNow)
            allure.attach.file(getPicturePath(code, timeNow), name=timeNow + code + "screenshot",
                               attachment_type=allure.attachment_type.PNG)
            self.comFeeApplyBoePage.driver.quit()
            assert 1 == 0

        else:
            logger.info("测试用例执行成功")
            code = 'success'
            timeNow = getNowTime()
            self.comFeeApplyBoePage.screenshot(code, timeNow)
            allure.attach.file(getPicturePath(code, timeNow), name=timeNow + code + "screenshot",
                               attachment_type=allure.attachment_type.PNG)
            assert 1 == 1


    @allure.story("通用费用申请费用报销界面业务审批")
    @allure.step("通用费用申请费用报销界面业务审批步骤")
    @pytest.mark.dependency(depends=["submit"] )
    def test_businessApprove(self, comFeeApplyBoe_testdata):
        logger.info(" ----- 单据业务审批开始 ----- ")
        global boeNum
        self.businessApprove = BusinessApprove(boeNum)
        content = self.businessApprove.boeBusinessApprove()
        logger.info(" ----- 单据业务审批结束 ----- ")
        assert content == '审批成功'


    @allure.story("通用费用申请共享中心界面财务审批")
    @allure.step("通用费用申请共享中心界面财务审批步骤")
    @pytest.mark.dependency(depends=["submit"])
    def test_sharingCenterApprove(self, comFeeApplyBoe_testdata):
        logger.info(" ----- 单据财务审批开始 ----- ")
        global boeNum
        self.sharingCenterApprove = SharingCenterApprove(boeNum)
        self.sharingCenterApprove.sharingCenterApproveChuShen()
        self.sharingCenterApprove.sharingCenterApproveFuShen()
        logger.info(" ----- 单据财务审批结束 ----- ")
