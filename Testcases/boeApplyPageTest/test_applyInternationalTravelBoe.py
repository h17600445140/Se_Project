# -*- coding:utf-8 -*-
from time import sleep

import allure
import pytest

from PageClass.boeApplyPageClass.applyInternationalTravelBoePage import ApplyInternationalTravelBoePage
from Testcases.common.boeBusinessApprove import BusinessApprove
from Testcases.common.boeSharingCenterApprove import SharingCenterApprove
from Testcases.common.loginDepend import LoginDepend


from Util import logger
from Util.util import getNowTime, getPicturePath


@allure.feature("差旅申请单（国际）流程")
class TestApplyInternationalTravelBoe(object):

    boeNum = globals()

    def setup_class(self):
        self.login = LoginDepend('easHost', 'user')
        self.applyInternationalTravelBoePage = ApplyInternationalTravelBoePage(self.login.driver)

    def teardown_class(self):
        self.applyInternationalTravelBoePage.driver.quit()


    @allure.story("差旅申请单（国际）费用报销界面单据提交")
    @allure.step("差旅申请单（国际）费用报销界面单据提交步骤")
    @allure.severity("blocker")
    @pytest.mark.dependency(name='submit')
    def test_applyInternationalTravel(self, applyInternationalTravelBoe_testdata):
        try:
            logger.info(" ----- 单据流程开始 ----- ")
            with allure.step("打开事项申请单据选择页面"):
                sleep(3)
                self.applyInternationalTravelBoePage.open_boeApply()
            with allure.step("打开的单据类型为：{} ,选择的单据业务类型为: {}".format('差旅申请单（国际）', applyInternationalTravelBoe_testdata['operationType'])):
                try:
                    self.applyInternationalTravelBoePage.open_boe('差旅申请单（国际）', applyInternationalTravelBoe_testdata['operationType'])
                except:
                    sleep(3)
                    logger.error(" Don't find Boe, Try again")
                    self.applyInternationalTravelBoePage.open_boe('差旅申请单（国际）', applyInternationalTravelBoe_testdata['operationType'])

            global boeNum
            boeNum = self.applyInternationalTravelBoePage.getBoeNum()

            with allure.step("输入业务类型"):
                self.applyInternationalTravelBoePage.input_operationType(applyInternationalTravelBoe_testdata['operationType'])
            with allure.step("输入备注"):
                self.applyInternationalTravelBoePage.input_boeAbstract(applyInternationalTravelBoe_testdata['boeAbstract'])
            with allure.step("输入金额"):
                self.applyInternationalTravelBoePage.input_applyAmount(applyInternationalTravelBoe_testdata['applyAmount'])

            with allure.step("输入开始时间：{}".format(applyInternationalTravelBoe_testdata['beginDateStr'])):
                self.applyInternationalTravelBoePage.input_beginDateStr(applyInternationalTravelBoe_testdata['beginDateStr'])
            with allure.step("输入结束时间：{}".format(applyInternationalTravelBoe_testdata['endDateStr'])):
                self.applyInternationalTravelBoePage.input_endDateStr(applyInternationalTravelBoe_testdata['endDateStr'])
            with allure.step("输入出发城市"):
                self.applyInternationalTravelBoePage.input_fromCity(applyInternationalTravelBoe_testdata['fromCity'])
            with allure.step("输入到达城市"):
                self.applyInternationalTravelBoePage.input_toCity(applyInternationalTravelBoe_testdata['toCity'])
            with allure.step("输入交通工具"):
                self.applyInternationalTravelBoePage.select_transportation(applyInternationalTravelBoe_testdata['transportation'])
            with allure.step("输入出差任务"):
                self.applyInternationalTravelBoePage.select_travelTask(applyInternationalTravelBoe_testdata['travelTask'])
            with allure.step("输入项目"):
                self.applyInternationalTravelBoePage.input_projectId(applyInternationalTravelBoe_testdata['projectName'])

            with allure.step("点击单据提交"):
                self.applyInternationalTravelBoePage.click_boeSubmitButton()
            with allure.step("点击单据关闭按钮"):
                self.applyInternationalTravelBoePage.click_close()

            with allure.step("进行单据生成校验"):
                self.applyInternationalTravelBoePage.click_myBoeList()
                self.applyInternationalTravelBoePage.click_moreButton()
                self.applyInternationalTravelBoePage.input_boeNo(boeNum)
                self.applyInternationalTravelBoePage.click_boeNoSelectButton()
                status = self.applyInternationalTravelBoePage.selectResultIsOrNot(boeNum)

            logger.info(" ----- 单据提交流程结束 ----- ")
            assert status == True

        except Exception as e:
            logger.error("出现异常，异常信息为：{}".format(type(e)))
            code = 'wrong'
            timeNow = getNowTime()
            self.applyInternationalTravelBoePage.screenshot(code, timeNow)
            allure.attach.file(getPicturePath(code, timeNow), name=timeNow + code + "screenshot",
                               attachment_type=allure.attachment_type.PNG)
            self.applyInternationalTravelBoePage.driver.quit()
            assert 1 == 0

        else:
            logger.info("测试用例执行成功")
            code = 'success'
            timeNow = getNowTime()
            self.applyInternationalTravelBoePage.screenshot(code, timeNow)
            allure.attach.file(getPicturePath(code, timeNow), name=timeNow + code + "screenshot",
                               attachment_type=allure.attachment_type.PNG)
            assert 1 == 1


    @allure.story("差旅申请单（国际）费用报销界面业务审批")
    @allure.step("差旅申请单（国际）费用报销界面业务审批步骤")
    @pytest.mark.dependency(depends=["submit"] )
    def test_businessApprove(self):
        logger.info(" ----- 单据业务审批开始 ----- ")
        global boeNum
        self.businessApprove = BusinessApprove(boeNum)
        content = self.businessApprove.boeBusinessApprove()
        logger.info(" ----- 单据业务审批开始 ----- ")
        assert content == '审批成功'


    @allure.story("差旅申请单（国际）共享中心界面财务审批")
    @allure.step("差旅申请单（国际）共享中心界面财务审批步骤")
    @pytest.mark.dependency(depends=["submit"])
    def test_sharingCenterApprove(self):
        logger.info(" ----- 单据财务审批开始 ----- ")
        global boeNum
        self.sharingCenterApprove = SharingCenterApprove(boeNum)
        self.sharingCenterApprove.sharingCenterApproveChuShen()
        self.sharingCenterApprove.sharingCenterApproveFuShen()
        logger.info(" ----- 单据财务审批结束 ----- ")





