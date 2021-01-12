# -*- coding:utf-8 -*-
from time import sleep

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageClass.baseIndexPageClass.reimbursementBasisPageClass import BusinessTypePageClass, BillConfigPageClass
from Testcases.common.loginDepend import LoginDepend
from Util import logger



class TestBusinessTypePageClass(object):

    def setup_class(self):
        self.login = LoginDepend('baseHost')
        self.businessTypePageClass = BusinessTypePageClass(self.login.driver)
        # self.businessTypePageClass.driver.implicitly_wait(2)

    def teardown_class(self):
        self.businessTypePageClass.driver.quit()


    @pytest.mark.run(order=1)
    def test_addBusinessCategoryBig(self):

        WebDriverWait(self.businessTypePageClass.driver, 5).until(
            EC.visibility_of_element_located(self.businessTypePageClass.getReimbursementBasis()))

        self.businessTypePageClass.open_reimbursementBasis()
        self.businessTypePageClass.open_businessType()

        WebDriverWait(self.businessTypePageClass.driver, 5).until(
            EC.visibility_of_element_located(self.businessTypePageClass.getTotalBusinessType()))

        self.businessTypePageClass.click_totalBusinessType()
        self.businessTypePageClass.click_addBusinessCategoryBigButton()

        self.businessTypePageClass.input_businessTypeCodeBox("test")
        self.businessTypePageClass.input_businessTypeNameCBox("test")


        self.businessTypePageClass.input_appDisplayNameCBox("test")
        self.businessTypePageClass.input_auditPointsCBox("test")

        self.businessTypePageClass.click_submitButton()

        WebDriverWait(self.businessTypePageClass.driver, 5).until(
            EC.visibility_of_element_located(self.businessTypePageClass.getToastBox()))

        logger.info("这是：------->{}".format(self.businessTypePageClass.getToastBoxText()))

        assert self.businessTypePageClass.getToastBoxText() == "新建成功"

    @pytest.mark.run(order=4)
    def test_deleteBusinessCategoryBig(self):
        sleep(1)
        self.businessTypePageClass.open_businessType()

        sleep(1)
        self.businessTypePageClass.input_filterBox("test1")

        sleep(1)
        self.businessTypePageClass.click_businessOpen()

        self.businessTypePageClass.click_businessTypeBig()

        sleep(1)
        self.businessTypePageClass.click_deleteButton()

        sleep(1)
        self.businessTypePageClass.click_deleteSubmitButton()

        self.businessTypePageClass.click_totalBusinessType()

        WebDriverWait(self.businessTypePageClass.driver, 5).until(
            EC.visibility_of_element_located(self.businessTypePageClass.getToastBox()))

        logger.info("这是：------->{}".format(self.businessTypePageClass.getToastBoxText()))

        assert self.businessTypePageClass.getToastBoxText() == "删除成功"

    @pytest.mark.run(order=2)
    def test_updateBusinessCategoryBig(self):
        sleep(1)
        self.businessTypePageClass.open_businessType()

        sleep(1)
        self.businessTypePageClass.input_filterBox("test")

        sleep(1)
        self.businessTypePageClass.click_businessOpen()

        self.businessTypePageClass.click_businessTypeBig()

        self.businessTypePageClass.click_editButton()

        self.businessTypePageClass.input_businessTypeCodeBox("test1")
        self.businessTypePageClass.input_businessTypeNameCBox("test1")

        self.businessTypePageClass.input_appDisplayNameCBox("test1")
        self.businessTypePageClass.input_auditPointsCBox("test1")

        self.businessTypePageClass.click_submitButton()

        WebDriverWait(self.businessTypePageClass.driver, 5).until(
            EC.visibility_of_element_located(self.businessTypePageClass.getToastBox()))

        logger.info("这是：------->{}".format(self.businessTypePageClass.getToastBoxText()))

        assert self.businessTypePageClass.getToastBoxText() == "编辑成功"

    @pytest.mark.run(order=3)
    def test_selectBusinessCategoryBig(self):
        sleep(1)
        self.businessTypePageClass.open_businessType()

        sleep(1)
        self.businessTypePageClass.input_filterBox("test1")

        sleep(1)
        self.businessTypePageClass.click_businessOpen()

        sleep(1)
        assert self.businessTypePageClass.elementIsDisplay(*self.businessTypePageClass.getBusinessTypeBig()) == True



class TestBillConfigPageClass(object):

    def setup_class(self):
        self.login = LoginDepend('baseHost')
        self.billConfigPageClass = BillConfigPageClass(self.login.driver)
        # self.businessTypePageClass.driver.implicitly_wait(2)

    def teardown_class(self):
        # self.businessTypePageClass.driver.quit()
        pass

    def test_configureBusinessType(self):

        sleep(2)

        self.billConfigPageClass.open_reimbursementBasis()

        self.billConfigPageClass.open_billConfig()

        self.billConfigPageClass.input_billName('日常费用报账单')

        self.billConfigPageClass.click_selectButton()

        self.billConfigPageClass.click_businessTypeButton()

        self.billConfigPageClass.input_businessInputBox('test')

        info = self.billConfigPageClass.getElementAttribute('class', *self.billConfigPageClass.getSelectFirstBox())

        logger.info("hello,-----> {}".format(info))

        self.billConfigPageClass.click_selectFirstBox()

        self.billConfigPageClass.click_confirmButton()

        WebDriverWait(self.billConfigPageClass.driver, 5).until(
            EC.visibility_of_element_located(self.billConfigPageClass.getToastBox()))

        logger.info("这是：------->{}".format(self.billConfigPageClass.getToastBoxText()))

        assert self.billConfigPageClass.getToastBoxText() == "保存成功"

        sleep(3)

        self.billConfigPageClass.click_businessTypeButton()

        self.billConfigPageClass.input_businessInputBox('test')

        info = self.billConfigPageClass.getElementAttribute('class', *self.billConfigPageClass.getSelectFirstBox())

        logger.info("hello,-----> {}".format(info))

        self.billConfigPageClass.click_closeButton()

        assert 'is-checked' in info













