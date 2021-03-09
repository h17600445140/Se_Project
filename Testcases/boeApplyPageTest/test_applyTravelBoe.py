# -*- coding:utf-8 -*-
from time import sleep

import allure
import pytest

from PageClass.boeApplyPageClass.applyTravelBoePage import ApplyTravelBoePage
from Testcases.common.boeBusinessApprove import BusinessApprove
from Testcases.common.boeSharingCenterApprove import SharingCenterApprove
from Testcases.common.loginDepend import LoginDepend
from Util import logger
from Util.util import getNowTime, getPicturePath



@allure.feature("差旅申请单流程")
class TestApplyTravelBoe(object):

    boeNum = globals()

    def setup_class(self):
        self.login = LoginDepend('easHost', 'user')
        self.applyTravelBoePage = ApplyTravelBoePage(self.login.driver)

    def teardown_class(self):
        self.applyTravelBoePage.driver.quit()


    @allure.story("差旅申请单费用报销界面单据提交")
    @allure.step("差旅申请单费用报销界面单据提交步骤")
    @allure.severity("blocker")
    @pytest.mark.dependency(name='submit')
    def test_applyTravel(self, applyTravelBoe_testdata):
        try:
            logger.info(" ----- 单据流程开始 ----- ")
            with allure.step("打开事项申请单据选择页面"):
                sleep(3)
                self.applyTravelBoePage.open_boeApply()
            with allure.step("打开的单据类型为：{} ,选择的单据业务类型为: {}".format('差旅申请单', applyTravelBoe_testdata['operationType'])):
                try:
                    self.applyTravelBoePage.open_boe('差旅申请单', applyTravelBoe_testdata['operationType'])
                except:
                    logger.error(" Don't find Boe, Try again")
                    sleep(3)
                    self.comFeeApplyBoePage.open_boe('通用费用申请单', applyTravelBoe_testdata['operationType'])

            global boeNum
            boeNum = self.applyTravelBoePage.getBoeNum()

            with allure.step("输入业务类型"):
                self.applyTravelBoePage.input_operationType(applyTravelBoe_testdata['operationType'])
            with allure.step("输入备注"):
                self.applyTravelBoePage.input_boeAbstract(applyTravelBoe_testdata['boeAbstract'])
            with allure.step("输入金额"):
                self.applyTravelBoePage.input_applyAmount(applyTravelBoe_testdata['applyAmount'])

            with allure.step("输入开始时间：{}".format(applyTravelBoe_testdata['beginDateStr'])):
                self.applyTravelBoePage.input_beginDateStr(applyTravelBoe_testdata['beginDateStr'])
            with allure.step("输入结束时间：{}".format(applyTravelBoe_testdata['endDateStr'])):
                self.applyTravelBoePage.input_endDateStr(applyTravelBoe_testdata['endDateStr'])
            with allure.step("输入出差任务"):
                self.applyTravelBoePage.select_travelTask(applyTravelBoe_testdata['travelTask'])
            with allure.step("输入出发城市"):
                self.applyTravelBoePage.input_fromCity(applyTravelBoe_testdata['fromCity'])
            with allure.step("输入到达城市"):
                self.applyTravelBoePage.input_toCity(applyTravelBoe_testdata['toCity'])
            with allure.step("输入交通工具"):
                self.applyTravelBoePage.select_transportation(applyTravelBoe_testdata['transportation'])


            with allure.step("点击单据提交"):
                self.applyTravelBoePage.click_boeSubmitButton()
            with allure.step("点击单据关闭按钮"):
                self.applyTravelBoePage.click_close()

            with allure.step("进行单据生成校验"):
                self.applyTravelBoePage.click_myBoeList()
                self.applyTravelBoePage.click_moreButton()
                self.applyTravelBoePage.input_boeNo(boeNum)
                self.applyTravelBoePage.click_boeNoSelectButton()
                status = self.applyTravelBoePage.selectResultIsOrNot(boeNum)

            logger.info(" ----- 单据提交流程结束 ----- ")
            assert status == True

        except Exception as e:
            logger.error("出现异常，异常信息为：{}".format(type(e)))
            code = 'wrong'
            timeNow = getNowTime()
            self.applyTravelBoePage.screenshot(code, timeNow)
            allure.attach.file(getPicturePath(code, timeNow), name=timeNow + code + "screenshot",
                               attachment_type=allure.attachment_type.PNG)
            self.applyTravelBoePage.driver.quit()
            assert 1 == 0

        else:
            logger.info("测试用例执行成功")
            code = 'success'
            timeNow = getNowTime()
            self.applyTravelBoePage.screenshot(code, timeNow)
            allure.attach.file(getPicturePath(code, timeNow), name=timeNow + code + "screenshot",
                               attachment_type=allure.attachment_type.PNG)
            assert 1 == 1


    @allure.story("差旅申请单费用报销界面业务审批")
    @allure.step("差旅申请单费用报销界面业务审批步骤")
    @pytest.mark.dependency(depends=["submit"] )
    def test_businessApprove(self):
        logger.info(" ----- 单据业务审批开始 ----- ")
        global boeNum
        self.businessApprove = BusinessApprove(boeNum)
        content = self.businessApprove.boeBusinessApprove()
        logger.info(" ----- 单据业务审批开始 ----- ")
        assert content == '审批成功'


    @allure.story("差旅申请单共享中心界面财务审批")
    @allure.step("差旅申请单共享中心界面财务审批步骤")
    @pytest.mark.dependency(depends=["submit"])
    def test_sharingCenterApprove(self):
        logger.info(" ----- 单据财务审批开始 ----- ")
        global boeNum
        self.sharingCenterApprove = SharingCenterApprove(boeNum)
        self.sharingCenterApprove.sharingCenterApproveChuShen()
        self.sharingCenterApprove.sharingCenterApproveFuShen()
        logger.info(" ----- 单据财务审批结束 ----- ")