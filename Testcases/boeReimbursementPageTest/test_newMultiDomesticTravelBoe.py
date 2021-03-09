# -*- coding:utf-8 -*-
import datetime
from time import sleep

import allure
import pytest

from PageClass.boeReimbursementPageClass.newMultiDomesticTravelBoePage import NewMultiDomesticTravelBoePage
from Testcases.common import invoiceFactory
from Testcases.common.boeBusinessApprove import BusinessApprove
from Testcases.common.boeSharingCenterApprove import SharingCenterApprove
from Testcases.common.loginDepend import LoginDepend
from Util import logger
from Util.util import getNowTime, getPicturePath


@allure.feature("多人差旅报账单流程")
class TestNewMultiDomesticTravelBoe():

    boeNum = globals()

    def setup_class(self):
        self.login = LoginDepend('easHost', 'user')
        self.newMultiDomesticTravelBoePage = NewMultiDomesticTravelBoePage(self.login.driver)

    def teardown_class(self):
        self.newMultiDomesticTravelBoePage.driver.quit()


    @allure.story("多人差旅报账单费用报销界面单据提交")
    @allure.step("多人差旅报账单费用报销界面单据提交步骤")
    @allure.severity("blocker")
    @pytest.mark.dependency(name='submit')
    def test_newMultiDomesticTravel(self, newMultiDomesticTravelBoe_testdata):
        try:
            logger.info(" ----- 单据流程开始 ----- ")
            with allure.step("打开费用报销单据选择页面"):
                sleep(3)
                self.newMultiDomesticTravelBoePage.open_boeReimburse()
            with allure.step("打开的单据类型为：{} ,选择的单据业务类型为: {}".format('多人差旅报账单', newMultiDomesticTravelBoe_testdata['operationType'])):
                try:
                    self.newMultiDomesticTravelBoePage.open_boe('多人差旅报账单', newMultiDomesticTravelBoe_testdata['operationType'])
                except:
                    sleep(3)
                    logger.error(" Don't find Boe, Try again")
                    self.newMultiDomesticTravelBoePage.open_boe('多人差旅报账单', newMultiDomesticTravelBoe_testdata['operationType'])

            global boeNum
            boeNum = self.newMultiDomesticTravelBoePage.getBoeNum()

            with allure.step("输入业务类型"):
                self.newMultiDomesticTravelBoePage.input_operationType(newMultiDomesticTravelBoe_testdata['operationType'])
            with allure.step("输入备注"):
                self.newMultiDomesticTravelBoePage.input_boeAbstract(newMultiDomesticTravelBoe_testdata['boeAbstract'])

            with allure.step("增加出行人员"):
                self.newMultiDomesticTravelBoePage.add_travelers(newMultiDomesticTravelBoe_testdata['travelers'])
            with allure.step("输入项目"):
                self.newMultiDomesticTravelBoePage.select_projectId(newMultiDomesticTravelBoe_testdata['projectName'])

            self.newMultiDomesticTravelBoePage.clearPersonCard()

            with allure.step("新增发票操作"):
                self.newMultiDomesticTravelBoePage.click_addInvoiceButton()
                self.newMultiDomesticTravelBoePage.click_invoiceType()
                # 差旅火车票新增
                invoiceFactory.get_invoice(self.login.driver, '火车票', 'boeInvoicePage').getTickets(
                    # datetime.datetime.now().strftime("%Y-%m-%d")
                    '2021-02-22',
                    '内部人员',
                    'UI01',
                    '长沙',
                    '杭州',
                    '二等座（高铁/动车）',
                    '500.00',
                    '否')

                self.newMultiDomesticTravelBoePage.click_addInvoiceButton()
                self.newMultiDomesticTravelBoePage.click_invoiceType()
                # 差旅火车票新增
                invoiceFactory.get_invoice(self.login.driver, '火车票', 'boeInvoicePage').getTickets(
                    # datetime.datetime.now().strftime("%Y-%m-%d")
                    '2021-02-22',
                    '内部人员',
                    'UI02',
                    '长沙',
                    '杭州',
                    '二等座（高铁/动车）',
                    '500.00',
                    '否')

            # self.newMultiDomesticTravelBoePage.click_addInvoiceButton()
            # self.newMultiDomesticTravelBoePage.click_invoiceType()
            # invoiceFactory.get_invoice(self.login.driver, '增值税普通发票', 'boeInvoicePage').getTickets(
            #     '2021-1-27', '811000000002', '81100002', '100.10', '0.10', '123456')

            with allure.step("点击单据提交"):
                self.newMultiDomesticTravelBoePage.click_boeSubmitButton()
            with allure.step("点击单据关闭按钮"):
                self.newMultiDomesticTravelBoePage.click_close()

            with allure.step("进行单据生成校验"):
                self.newMultiDomesticTravelBoePage.click_myBoeList()
                self.newMultiDomesticTravelBoePage.click_moreButton()
                self.newMultiDomesticTravelBoePage.input_boeNo(boeNum)
                self.newMultiDomesticTravelBoePage.click_boeNoSelectButton()
                status = self.newMultiDomesticTravelBoePage.selectResultIsOrNot(boeNum)

            logger.info(" ----- 单据提交流程结束 ----- ")
            assert status == True

        except Exception as e:
            logger.error("出现异常，异常信息为：{}".format(type(e)))
            code = 'wrong'
            timeNow = getNowTime()
            self.newMultiDomesticTravelBoePage.screenshot(code, timeNow)
            allure.attach.file(getPicturePath(code, timeNow), name=timeNow + code + "screenshot",
                               attachment_type=allure.attachment_type.PNG)
            self.newMultiDomesticTravelBoePage.driver.quit()
            assert 1 == 0

        else:
            logger.info("测试用例执行成功")
            code = 'success'
            timeNow = getNowTime()
            self.newMultiDomesticTravelBoePage.screenshot(code, timeNow)
            allure.attach.file(getPicturePath(code, timeNow), name=timeNow + code + "screenshot",
                               attachment_type=allure.attachment_type.PNG)
            assert 1 == 1


    @allure.story("多人差旅报账单费用报销界面业务审批")
    @allure.step("多人差旅报账单费用报销界面业务审批步骤")
    @pytest.mark.dependency(depends=["submit"] )
    def test_businessApprove(self):
        logger.info(" ----- 单据业务审批开始 ----- ")
        global boeNum
        self.businessApprove = BusinessApprove(boeNum)
        content = self.businessApprove.boeBusinessApprove()
        logger.info(" ----- 单据业务审批结束 ----- ")
        assert content == '审批成功'


    @allure.story("多人差旅报账单共享中心界面财务审批")
    @allure.step("多人差旅报账单共享中心界面财务审批步骤")
    @pytest.mark.dependency(depends=["submit"])
    def test_sharingCenterApprove(self):
        logger.info(" ----- 单据财务审批开始 ----- ")
        global boeNum
        self.sharingCenterApprove = SharingCenterApprove(boeNum)
        self.sharingCenterApprove.sharingCenterApproveChuShen()
        self.sharingCenterApprove.sharingCenterApproveFuShen()
        logger.info(" ----- 单据财务审批结束 ----- ")