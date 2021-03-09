# -*- coding:utf-8 -*-
import datetime
from time import sleep

import allure
import pytest

from PageClass.boeReimbursementPageClass.newDomesticTravelBoePage import NewDomesticTravelBoePage
from PageClass.easIndexPageClass.easMyInvoicePage import EasMyInvoiceIndexPage
from Testcases.common import invoiceFactory
from Testcases.common.boeBusinessApprove import BusinessApprove
from Testcases.common.boeSharingCenterApprove import SharingCenterApprove
from Testcases.common.loginDepend import LoginDepend
from Util import logger
from Util.util import getNowTime, getPicturePath


@allure.feature("差旅报账单流程")
class TestNewDomesticTravelBoe():

    boeNum = globals()

    def setup_class(self):
        self.login = LoginDepend('easHost', 'user')
        self.newDomesticTravelBoePage = NewDomesticTravelBoePage(self.login.driver)

    def teardown_class(self):
        self.newDomesticTravelBoePage.driver.quit()


    @allure.story("差旅报账单费用报销界面单据提交")
    @allure.step("差旅报账单费用报销界面单据提交步骤")
    @allure.severity("blocker")
    @pytest.mark.dependency(name='submit')
    def test_newDomesticTravel(self, newDomesticTravelBoe_testdata):
        try:
            logger.info(" ----- 单据流程开始 ----- ")
            with allure.step("打开费用报销单据选择页面"):
                sleep(3)
                self.newDomesticTravelBoePage.open_boeReimburse()
            with allure.step("打开的单据类型为：{} ,选择的单据业务类型为: {}".format('差旅报账单', newDomesticTravelBoe_testdata['operationType'])):
                try:
                    self.newDomesticTravelBoePage.open_boe('差旅报账单', newDomesticTravelBoe_testdata['operationType'])
                except:
                    sleep(3)
                    logger.error(" Don't find Boe, Try again")
                    self.newDomesticTravelBoePage.open_boe('差旅报账单', newDomesticTravelBoe_testdata['operationType'])

            global boeNum
            boeNum = self.newDomesticTravelBoePage.getBoeNum()

            with allure.step("输入业务类型"):
                self.newDomesticTravelBoePage.input_operationType(newDomesticTravelBoe_testdata['operationType'])
            with allure.step("输入备注"):
                self.newDomesticTravelBoePage.input_boeAbstract(newDomesticTravelBoe_testdata['boeAbstract'])

            with allure.step("增加发票"):
                self.newDomesticTravelBoePage.click_addInvoiceButton()
                self.newDomesticTravelBoePage.click_invoiceType()
                # 差旅火车票新增
                invoiceFactory.get_invoice(self.login.driver, '火车票', 'boeInvoicePage').getTickets(
                    # datetime.datetime.now().strftime("%Y-%m-%d")
                    '2021-02-21',
                    newDomesticTravelBoe_testdata['trainInvoice']['invoicePersonType'],
                    newDomesticTravelBoe_testdata['trainInvoice']['invoicePersonName'],
                    newDomesticTravelBoe_testdata['trainInvoice']['invoiceFromCity'],
                    newDomesticTravelBoe_testdata['trainInvoice']['invoiceToCity'],
                    newDomesticTravelBoe_testdata['trainInvoice']['invoiceSiteType'],
                    newDomesticTravelBoe_testdata['trainInvoice']['invoiceTicketFee'],
                    newDomesticTravelBoe_testdata['trainInvoice']['invoiceIsReplace'])

            with allure.step("选择部门"):
                self.newDomesticTravelBoePage.selectDepartment(newDomesticTravelBoe_testdata['deptCode'], newDomesticTravelBoe_testdata['deptName'])
            with allure.step("输入项目"):
                self.newDomesticTravelBoePage.input_projectId(newDomesticTravelBoe_testdata['projectName'])

            with allure.step("点击单据提交"):
                self.newDomesticTravelBoePage.click_boeSubmitButton()
            with allure.step("点击单据关闭按钮"):
                self.newDomesticTravelBoePage.click_close()

            with allure.step("进行单据生成校验"):
                self.newDomesticTravelBoePage.click_myBoeList()
                self.newDomesticTravelBoePage.click_moreButton()
                self.newDomesticTravelBoePage.input_boeNo(boeNum)
                self.newDomesticTravelBoePage.click_boeNoSelectButton()
                status = self.newDomesticTravelBoePage.selectResultIsOrNot(boeNum)

            logger.info(" ----- 单据提交流程结束 ----- ")
            assert status == True

        except Exception as e:
            logger.error("出现异常，异常信息为：{}".format(type(e)))
            code = 'wrong'
            timeNow = getNowTime()
            self.newDomesticTravelBoePage.screenshot(code, timeNow)
            allure.attach.file(getPicturePath(code, timeNow), name=timeNow + code + "screenshot",
                               attachment_type=allure.attachment_type.PNG)
            self.newDomesticTravelBoePage.driver.quit()
            assert 1 == 0

        else:
            logger.info("测试用例执行成功")
            code = 'success'
            timeNow = getNowTime()
            self.newDomesticTravelBoePage.screenshot(code, timeNow)
            allure.attach.file(getPicturePath(code, timeNow), name=timeNow + code + "screenshot",
                               attachment_type=allure.attachment_type.PNG)
            assert 1 == 1


    @allure.story("差旅报账单费用报销界面业务审批")
    @allure.step("差旅报账单费用报销界面业务审批步骤")
    @pytest.mark.dependency(depends=["submit"] )
    def test_businessApprove(self):
        logger.info(" ----- 单据业务审批开始 ----- ")
        global boeNum
        self.businessApprove = BusinessApprove(boeNum)
        content = self.businessApprove.boeBusinessApprove()
        logger.info(" ----- 单据业务审批结束 ----- ")
        assert content == '审批成功'


    @allure.story("差旅报账单共享中心界面财务审批")
    @allure.step("差旅报账单共享中心界面财务审批步骤")
    @pytest.mark.dependency(depends=["submit"])
    def test_sharingCenterApprove(self):
        logger.info(" ----- 单据财务审批开始 ----- ")
        global boeNum
        self.sharingCenterApprove = SharingCenterApprove(boeNum)
        self.sharingCenterApprove.sharingCenterApproveChuShen()
        self.sharingCenterApprove.sharingCenterApproveFuShen()
        logger.info(" ----- 单据财务审批结束 ----- ")











