# -*- coding:utf-8 -*-
import datetime
import os
import random
import string

import allure
import pytest

from PageClass.basIndexPageClass.receivableEasPageClass.billingApplicationBoePage import BillingApplicationBoePage
from Testcases.common.boeBusinessApprove import BusinessApprove
from Testcases.common.boeSharingCenterApprove import SharingCenterApprove
from Testcases.common.loginDepend import LoginDepend
from Util import logger
from Util.util import getNowTime, getPicturePath, writeInvoiceNum


@allure.feature("开票申请单流程")
class TestBillingApplicationBoe():

    boeNum = globals()

    def setup_class(self):
        self.publicLogin = LoginDepend('basHost', 'user')
        self.billingApplicationBoePage = BillingApplicationBoePage(self.publicLogin.driver)

    def teardown_class(self):
        self.billingApplicationBoePage.driver.quit()

    @allure.story("开票申请单业务报账界面单据提交")
    @allure.step("开票申请单业务报账界面单据提交步骤")
    @allure.severity("blocker")
    @pytest.mark.dependency(name='submit')
    def test_billingApplicationBoe(self):
        try:

            logger.info(" ----- 单据提交流程开始 ----- ")

            with allure.step("点击选择收入收款页面"):
                self.billingApplicationBoePage.selectTabType('收入收款')
            with allure.step("进入收入报账单单据提交页面"):
                self.billingApplicationBoePage.boeRntry('开票申请单')

            global boeNum
            boeNum = self.billingApplicationBoePage.getBoeNum()

            with allure.step("选择业务类型"):
                self.billingApplicationBoePage.input_operationType('UI通用')
            with allure.step("选择发票类型"):
                self.billingApplicationBoePage.selectInvoiceType('增值税普通发票')

            self.billingApplicationBoePage.selectBuyer('UI客户')

            # self.billingApplicationBoePage.selectContract('hcKH000002')
            # self.billingApplicationBoePage.input_orderNumber('hcOrder000001')

            with allure.step("选择项目"):
                self.billingApplicationBoePage.input_project('UI项目')
            with allure.step("选择商品"):
                self.billingApplicationBoePage.selectGoods('UISP', goodsName = 'UI商品')
            with allure.step("输入商品数量"):
                self.billingApplicationBoePage.input_goodsAmount('10')
            with allure.step("输入含税单价"):
                self.billingApplicationBoePage.input_goodPrice('100.00')
            with allure.step("输入含税金额"):
                self.billingApplicationBoePage.input_goodsExpenseAmount('1000.00')
            with allure.step("选择商品税率"):
                self.billingApplicationBoePage.input_goodsTaxRate('5')

            with allure.step("选择纳税人"):
                self.billingApplicationBoePage.selectSaler('UI纳税人')

            with allure.step("点击单据提交"):
                self.billingApplicationBoePage.click_boeSubmitButton()
            with allure.step("点击单据关闭按钮"):
                self.billingApplicationBoePage.click_close()

            with allure.step("进行单据生成校验"):
                self.billingApplicationBoePage.click_more()
                self.billingApplicationBoePage.input_boeNumQuery(boeNum)
                self.billingApplicationBoePage.click_queryButton()

            with allure.step("断言结果：{}".format(self.billingApplicationBoePage.checkBoeNumExistIsOrNot(boeNum))):
                assert self.billingApplicationBoePage.checkBoeNumExistIsOrNot(boeNum) == True

            logger.info(" ----- 单据提交流程结束 ----- ")

        except Exception as e:
            logger.error("出现异常，异常信息为：{}".format(type(e)))
            code = 'wrong'
            timeNow = getNowTime()
            self.billingApplicationBoePage.screenshot(code, timeNow)
            allure.attach.file(getPicturePath(code, timeNow), name=timeNow + code + "screenshot",
                               attachment_type=allure.attachment_type.PNG)
            self.billingApplicationBoePage.driver.quit()
            assert 1 == 0

        else:
            logger.info("测试用例执行成功")
            code = 'success'
            timeNow = getNowTime()
            self.billingApplicationBoePage.screenshot(code, timeNow)
            allure.attach.file(getPicturePath(code, timeNow), name=timeNow + code + "screenshot",
                               attachment_type=allure.attachment_type.PNG)
            assert 1 == 1

    @allure.story("开票申请单费用报销界面业务审批")
    @allure.step("开票申请单费用报销界面业务审批步骤")
    @pytest.mark.dependency(depends=["submit"])
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
        invoiceNum = ''.join(random.choice(string.digits) for _ in range(8))
        invoiceDataDict = {'invoiceNo': ''.join(random.choice(string.digits) for _ in range(12)),
                           'invoiceCode': invoiceNum,
                           'invoiceDate': datetime.datetime.now().strftime('%Y-%m-%d'),
                           'invoiceFee': '1000.00',
                           'invoiceTax': '47.62',
                           'invoiceRemark': '测试开票申请单'}
        self.sharingCenterApprove.sharingCenterApproveChuShen(modify=True, **invoiceDataDict)
        self.sharingCenterApprove.sharingCenterApproveFuShen()

        invoiceNumPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'invoiceNum.json')
        writeInvoiceNum(invoiceNumPath, invoiceNum)

        logger.info(" ----- 单据财务审批结束 ----- ")




