# -*- coding:utf-8 -*-
import datetime
import os
import random
import string

import allure
import pytest

from PageClass.basIndexPageClass.receivableEasPageClass.newObsoleteRedLetterInvoiceApplictationBoePage import \
    NewObsoleteRedLetterInvoiceApplictationBoePage
from Testcases.common.boeBusinessApprove import BusinessApprove
from Testcases.common.boeSharingCenterApprove import SharingCenterApprove
from Testcases.common.loginDepend import LoginDepend
from Util import logger
from Util.util import getNowTime, getPicturePath, readInvoiceNum


@allure.feature("作废/红字发票申请单（新）")
class TestNewObsoleteRedLetterInvoiceApplictationBoe():

    boeNum = globals()

    def setup_class(self):
        self.publicLogin = LoginDepend('basHost', 'user')
        self.newObsoleteRedLetterInvoiceApplictationBoePage = NewObsoleteRedLetterInvoiceApplictationBoePage(self.publicLogin.driver)

    def teardown_class(self):
        self.newObsoleteRedLetterInvoiceApplictationBoePage.driver.quit()

    @allure.story("作废/红字发票申请单（新）业务报账界面单据提交")
    @allure.step("作废/红字发票申请单（新）业务报账界面单据提交步骤")
    @allure.severity("blocker")
    @pytest.mark.dependency(name='submit')
    def test_newObsoleteRedLetterInvoiceApplictationBoePage(self):

        try:

            logger.info(" ----- 单据提交流程开始 ----- ")

            with allure.step("点击选择收入收款页面"):
                self.newObsoleteRedLetterInvoiceApplictationBoePage.selectTabType('收入收款')
            with allure.step("进入作废/红字发票申请单（新）单据提交页面"):
                self.newObsoleteRedLetterInvoiceApplictationBoePage.boeRntry('作废/红字发票申请单（新）')

            global boeNum
            boeNum = self.newObsoleteRedLetterInvoiceApplictationBoePage.getBoeNum()

            with allure.step("选择业务类型"):
                self.newObsoleteRedLetterInvoiceApplictationBoePage.input_operationType('UI红字发票')
            with allure.step("输入备注"):
                self.newObsoleteRedLetterInvoiceApplictationBoePage.input_boeAbstract('测试作废/红字发票申请单（新）')

            boeNumPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'invoiceNum.json')
            self.invoiceNum = readInvoiceNum(boeNumPath)

            with allure.step("选择关联发票"):
                self.newObsoleteRedLetterInvoiceApplictationBoePage.relateTargetInvoice(self.invoiceNum)

            with allure.step("点击单据提交"):
                self.newObsoleteRedLetterInvoiceApplictationBoePage.click_boeSubmitButton()
            with allure.step("点击单据关闭按钮"):
                self.newObsoleteRedLetterInvoiceApplictationBoePage.click_close()

            with allure.step("进行单据生成校验"):
                self.newObsoleteRedLetterInvoiceApplictationBoePage.click_more()
                self.newObsoleteRedLetterInvoiceApplictationBoePage.input_boeNumQuery(boeNum)
                self.newObsoleteRedLetterInvoiceApplictationBoePage.click_queryButton()

            with allure.step("断言结果：{}".format(self.newObsoleteRedLetterInvoiceApplictationBoePage.checkBoeNumExistIsOrNot(boeNum))):
                assert self.newObsoleteRedLetterInvoiceApplictationBoePage.checkBoeNumExistIsOrNot(boeNum) == True

            logger.info(" ----- 单据提交流程结束 ----- ")

        except Exception as e:
            logger.error("出现异常，异常信息为：{}".format(type(e)))
            code = 'wrong'
            timeNow = getNowTime()
            self.newObsoleteRedLetterInvoiceApplictationBoePage.screenshot(code, timeNow)
            allure.attach.file(getPicturePath(code, timeNow), name=timeNow + code + "screenshot",
                               attachment_type=allure.attachment_type.PNG)
            self.newObsoleteRedLetterInvoiceApplictationBoePage.driver.quit()
            assert 1 == 0

        else:
            logger.info("测试用例执行成功")
            code = 'success'
            timeNow = getNowTime()
            self.newObsoleteRedLetterInvoiceApplictationBoePage.screenshot(code, timeNow)
            allure.attach.file(getPicturePath(code, timeNow), name=timeNow + code + "screenshot",
                               attachment_type=allure.attachment_type.PNG)
            assert 1 == 1


    @allure.story("作废/红字发票申请单（新）费用报销界面业务审批")
    @allure.step("作废/红字发票申请单（新）费用报销界面业务审批步骤")
    @pytest.mark.dependency(depends=["submit"] )
    def test_businessApprove(self):
        logger.info(" ----- 单据业务审批开始 ----- ")
        global boeNum
        self.businessApprove = BusinessApprove(boeNum)
        content = self.businessApprove.boeBusinessApprove()
        logger.info(" ----- 单据业务审批开始 ----- ")
        assert content == '审批成功'


    @allure.story("作废/红字发票申请单（新）共享中心界面财务审批")
    @allure.step("作废/红字发票申请单（新）共享中心界面财务审批步骤")
    @pytest.mark.dependency(depends=["submit"])
    def test_sharingCenterApprove(self):
        logger.info(" ----- 单据财务审批开始 ----- ")
        global boeNum
        self.sharingCenterApprove = SharingCenterApprove(boeNum)

        invoiceNum = ''.join(random.choice(string.digits) for _ in range(8))
        invoiceDataDict = {'invoiceNo': ''.join(random.choice(string.digits) for _ in range(12)),
                           'invoiceCode': invoiceNum,
                           'invoiceDate': datetime.datetime.now().strftime('%Y-%m-%d'),
                           'invoiceFee': '-1000.00',
                           'invoiceTypeCode': '增值税普通发票',
                           'checkCode': '123456'}

        self.sharingCenterApprove.sharingCenterApproveChuShen(modify=True, **invoiceDataDict)
        self.sharingCenterApprove.sharingCenterApproveFuShen()
        logger.info(" ----- 单据财务审批结束 ----- ")