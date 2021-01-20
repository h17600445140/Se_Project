# -*- coding:utf-8 -*-
from time import sleep

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageClass.baseIndexPageClass.reimbursementBasisPage import BusinessTypePage, BillConfigPage
from Testcases.common.loginDepend import LoginDepend
from Util import logger



class TestBusinessTypePage(object):

    def setup_class(self):
        self.login = LoginDepend('baseHost', 'user')
        self.businessTypePage = BusinessTypePage(self.login.driver)
        # self.businessTypePage.driver.implicitly_wait(2)

    def teardown_class(self):
        # self.businessTypePage.driver.quit()
        pass

    @pytest.mark.run(order=1)
    def test_addBusinessCategoryBig(self):

        WebDriverWait(self.businessTypePage.driver, 5).until(
            EC.visibility_of_element_located(self.businessTypePage.getReimbursementBasis()))

        self.businessTypePage.open_reimbursementBasis()
        self.businessTypePage.open_businessType()

        WebDriverWait(self.businessTypePage.driver, 5).until(
            EC.visibility_of_element_located(self.businessTypePage.getTotalBusinessType()))

        self.businessTypePage.click_totalBusinessType()
        self.businessTypePage.click_addBusinessCategoryBigButton()

        self.businessTypePage.input_businessTypeCodeBox("test")
        self.businessTypePage.input_businessTypeNameCBox("test")


        self.businessTypePage.input_appDisplayNameCBox("test")
        self.businessTypePage.input_auditPointsCBox("test")

        self.businessTypePage.click_submitButton()

        WebDriverWait(self.businessTypePage.driver, 5).until(
            EC.visibility_of_element_located(self.businessTypePage.getToastBox()))

        logger.info("这是：------->{}".format(self.businessTypePage.getToastBoxText()))

        assert self.businessTypePage.getToastBoxText() == "新建成功"

    @pytest.mark.run(order=4)
    def test_deleteBusinessCategoryBig(self):
        sleep(1)
        self.businessTypePage.open_businessType()

        sleep(1)
        self.businessTypePage.input_filterBox("test")

        sleep(1)
        self.businessTypePage.click_businessOpen()

        self.businessTypePage.click_businessTypeBig()

        sleep(1)
        self.businessTypePage.click_deleteButton()

        sleep(1)
        self.businessTypePage.click_deleteSubmitButton()

        self.businessTypePage.click_totalBusinessType()

        WebDriverWait(self.businessTypePage.driver, 5).until(
            EC.visibility_of_element_located(self.businessTypePage.getToastBox()))

        logger.info("这是：------->{}".format(self.businessTypePage.getToastBoxText()))

        assert self.businessTypePage.getToastBoxText() == "删除成功"

    @pytest.mark.run(order=2)
    def test_updateBusinessCategoryBig(self):
        sleep(1)
        self.businessTypePage.open_businessType()

        sleep(1)
        self.businessTypePage.input_filterBox("test")

        sleep(1)
        self.businessTypePage.click_businessOpen()

        self.businessTypePage.click_businessTypeBig()

        self.businessTypePage.click_editButton()

        self.businessTypePage.input_businessTypeCodeBox("test")
        self.businessTypePage.input_businessTypeNameCBox("test")

        self.businessTypePage.input_appDisplayNameCBox("test")
        self.businessTypePage.input_auditPointsCBox("test")

        self.businessTypePage.click_submitButton()

        WebDriverWait(self.businessTypePage.driver, 5).until(
            EC.visibility_of_element_located(self.businessTypePage.getToastBox()))

        logger.info("这是：------->{}".format(self.businessTypePage.getToastBoxText()))

        assert self.businessTypePage.getToastBoxText() == "编辑成功"

    @pytest.mark.run(order=3)
    def test_selectBusinessCategoryBig(self):
        sleep(1)
        self.businessTypePage.open_businessType()

        sleep(1)
        self.businessTypePage.input_filterBox("test")

        sleep(1)
        self.businessTypePage.click_businessOpen()

        sleep(1)
        assert self.businessTypePage.elementIsDisplay(*self.businessTypePage.getBusinessTypeBig()) == True



class TestbillConfigPage(object):

    def setup_class(self):
        self.login = LoginDepend('baseHost', 'user')
        self.billConfigPage = BillConfigPage(self.login.driver)
        # self.businessTypePage.driver.implicitly_wait(2)

    def teardown_class(self):
        # self.businessTypePage.driver.quit()
        pass

    def test_configureBusinessType(self):

        sleep(2)

        self.billConfigPage.open_reimbursementBasis()

        self.billConfigPage.open_billConfig()

        self.billConfigPage.input_billName('日常费用报账单')

        self.billConfigPage.click_selectButton()

        self.billConfigPage.click_businessTypeButton()

        self.billConfigPage.input_businessInputBox('test1')

        info = self.billConfigPage.getElementAttribute('class', *self.billConfigPage.getSelectFirstBox())

        logger.info("hello,-----> {}".format(info))

        self.billConfigPage.click_selectFirstBox()

        self.billConfigPage.click_businessTypeConfirmButton()

        WebDriverWait(self.billConfigPage.driver, 5).until(
            EC.visibility_of_element_located(self.billConfigPage.getToastBox()))

        logger.info("这是：------->{}".format(self.billConfigPage.getToastBoxText()))

        assert self.billConfigPage.getToastBoxText() == "保存成功"

        sleep(3)

        self.billConfigPage.click_businessTypeButton()

        self.billConfigPage.input_businessInputBox('test1')

        info = self.billConfigPage.getElementAttribute('class', *self.billConfigPage.getSelectFirstBox())

        logger.info("hello,-----> {}".format(info))

        self.billConfigPage.click_businessTypeCloseButton()

        assert 'is-checked' in info


    def test_configureVoucherType(self):

        sleep(2)

        self.billConfigPage.open_reimbursementBasis()

        self.billConfigPage.open_billConfig()

        self.billConfigPage.input_billName('日常费用报账单')

        self.billConfigPage.click_selectButton()

        self.billConfigPage.click_voucherTypeButton()

        self.billConfigPage.click_voucherAddButton()

        sleep(1)
        self.billConfigPage.accountingEntitySelect("hc核算主体")

        sleep(1)
        self.billConfigPage.vendorTypeSelect('客户')

        sleep(1)
        self.billConfigPage.voucherCategorySelect('付款凭证')

        sleep(1)
        self.billConfigPage.voucherTypeSelect('资产过账')

        sleep(1)
        self.billConfigPage.createNodeSelect('审核完成')

        sleep(1)
        self.billConfigPage.importNodeSelect('审核完成')

        sleep(1)
        self.billConfigPage.whetherMergeSelect('是')

        sleep(1)
        self.billConfigPage.click_voucherAddSubmit()

        sleep(1)
        self.billConfigPage.click_voucherSubmit()


    def test_configureEditBill(self):

        sleep(2)

        self.billConfigPage.open_reimbursementBasis()

        self.billConfigPage.open_billConfig()

        self.billConfigPage.input_billName('日常费用报账单')

        self.billConfigPage.click_selectButton()

        self.billConfigPage.click_billEditButton()

        isStandardControl = True
        isPay = True
        isAPPSubmitBill = False
        isGenerateVoucher = True
        isStatistics = False
        isEnableBillImageArea = False
        isEnableOCR = False



        if isStandardControl != True:
            if 'is-checked' in self.billConfigPage.getElementAttribute(
                    'class', *self.billConfigPage.getBillWhetherToStandardControlButton()):
                self.billConfigPage.click_billWhetherToStandardControlButton()
                logger.info("状态由选中转变为未选中状态")
            else:
                logger.info("状态已经为未选中状态")
        else:
            if 'is-checked' in self.billConfigPage.getElementAttribute(
                    'class', *self.billConfigPage.getBillWhetherToStandardControlButton()):
                logger.info("状态已经为选中状态")
            else:
                self.billConfigPage.click_billWhetherToStandardControlButton()
                logger.info("状态由未选中转变为选中状态")

        sleep(2)
        if isPay != True:
            if 'is-checked' in self.billConfigPage.getElementAttribute(
                    'class', *self.billConfigPage.getBillWhetherToPayButton()):
                self.billConfigPage.click_billWhetherToPayButton()
                logger.info("状态由选中转变为未选中状态")
            else:
                logger.info("状态已经为未选中状态")
        else:
            if 'is-checked' in self.billConfigPage.getElementAttribute(
                    'class', *self.billConfigPage.getBillWhetherToPayButton()):
                logger.info("状态已经为选中状态")
            else:
                self.billConfigPage.click_billWhetherToPayButton()
                logger.info("状态由未选中转变为选中状态")

        sleep(2)
        if isAPPSubmitBill != True:
            if 'is-checked' in self.billConfigPage.getElementAttribute(
                    'class', *self.billConfigPage.getBillWhetherToAPPSubmitBill()):
                self.billConfigPage.click_billWhetherToAPPSubmitBill()
                logger.info("状态由选中转变为未选中状态")
            else:
                logger.info("状态已经为未选中状态")
        else:
            if 'is-checked' in self.billConfigPage.getElementAttribute(
                    'class', *self.billConfigPage.getBillWhetherToAPPSubmitBill()):
                logger.info("状态已经为选中状态")
            else:
                self.billConfigPage.click_billWhetherToAPPSubmitBill()
                logger.info("状态由未选中转变为选中状态")

        sleep(2)
        if isGenerateVoucher != True:
            if 'is-checked' in self.billConfigPage.getElementAttribute(
                    'class', *self.billConfigPage.getBillWhetherToGenerateVoucher()):
                self.billConfigPage.click_billWhetherToGenerateVoucher()
                logger.info("状态由选中转变为未选中状态")
            else:
                logger.info("状态已经为未选中状态")
        else:
            if 'is-checked' in self.billConfigPage.getElementAttribute(
                    'class', *self.billConfigPage.getBillWhetherToGenerateVoucher()):
                logger.info("状态已经为选中状态")
            else:
                self.billConfigPage.click_billWhetherToGenerateVoucher()
                logger.info("状态由未选中转变为选中状态")

        sleep(2)
        if isStatistics != True:
            if 'is-checked' in self.billConfigPage.getElementAttribute(
                    'class', *self.billConfigPage.getBillWhetherToStatistics()):
                self.billConfigPage.click_billWhetherToStatistics()
                logger.info("状态由选中转变为未选中状态")
            else:
                logger.info("状态已经为未选中状态")
        else:
            if 'is-checked' in self.billConfigPage.getElementAttribute(
                    'class', *self.billConfigPage.getBillWhetherToStatistics()):
                logger.info("状态已经为选中状态")
            else:
                self.billConfigPage.click_billWhetherToStatistics()
                logger.info("状态由未选中转变为选中状态")

        sleep(2)
        if isEnableBillImageArea != True:
            if 'is-checked' in self.billConfigPage.getElementAttribute(
                    'class', *self.billConfigPage.getBillWhetherToEnableBillImageArea()):
                self.billConfigPage.click_billWhetherToEnableBillImageArea()
                logger.info("状态由选中转变为未选中状态")
            else:
                logger.info("状态已经为未选中状态")
        else:
            if 'is-checked' in self.billConfigPage.getElementAttribute(
                    'class', *self.billConfigPage.getBillWhetherToEnableBillImageArea()):
                logger.info("状态已经为选中状态")
            else:
                self.billConfigPage.click_billWhetherToEnableBillImageArea()
                logger.info("状态由未选中转变为选中状态")

        sleep(2)
        if isEnableOCR != True:
            if 'is-checked' in self.billConfigPage.getElementAttribute(
                    'class', *self.billConfigPage.getBillWhetherToEnableOCR()):
                self.billConfigPage.click_billWhetherToEnableOCR()
                logger.info("状态由选中转变为未选中状态")
            else:
                logger.info("状态已经为未选中状态")
        else:
            if 'is-checked' in self.billConfigPage.getElementAttribute(
                    'class', *self.billConfigPage.getBillWhetherToEnableOCR()):
                logger.info("状态已经为选中状态")
            else:
                self.billConfigPage.click_billWhetherToEnableOCR()
                logger.info("状态由未选中转变为选中状态")

        sleep(2)
        self.billConfigPage.click_billSubmitButton()

        WebDriverWait(self.billConfigPage.driver, 5).until(
            EC.visibility_of_element_located(self.billConfigPage.getToastBox()))

        logger.info("这是：------->{}".format(self.billConfigPage.getToastBoxText()))

        assert self.billConfigPage.getToastBoxText() == "保存成功"















