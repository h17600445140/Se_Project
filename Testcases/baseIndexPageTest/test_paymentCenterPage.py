# -*- coding:utf-8 -*-
from time import sleep

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageClass.baseIndexPageClass.paymentCenterPageClass import CompanyAccountPageClass, PayMethodPageClass
from Testcases.common.loginDepend import LoginDepend



class TestCompanyAccountPageClass(object):

    def setup_class(self):
        self.login = LoginDepend('baseHost')
        self.companyAccountPageClass = CompanyAccountPageClass(self.login.driver)

    def teardown_class(self):
        self.companyAccountPageClass.driver.quit()

    @pytest.mark.run(order=1)
    def test_addCompanyAccount(self):
        WebDriverWait(self.companyAccountPageClass.driver, 5).until(
            EC.visibility_of_element_located(self.companyAccountPageClass.getPaymentCenter()))

        self.companyAccountPageClass.open_paymentCenter()

        self.companyAccountPageClass.open_companyAccount()

        self.companyAccountPageClass.click_addButton()

        sleep(1)
        self.companyAccountPageClass.input_priorityInput('100')
        sleep(1)
        self.companyAccountPageClass.accountingEntitySelect('爆破核算主体')
        sleep(1)
        self.companyAccountPageClass.input_code('test')
        sleep(1)
        self.companyAccountPageClass.subBankSelect('中国工商银行深圳市景田支行', '中国工商银行', '102584002985')
        sleep(1)
        self.companyAccountPageClass.input_bankAccountName('测试专用账户')
        sleep(1)
        self.companyAccountPageClass.input_bankAccountNum('13121196337001')
        sleep(1)
        self.companyAccountPageClass.collectionTypeSelect('收付款')
        sleep(1)
        self.companyAccountPageClass.currencyIdSelect('CNY')
        sleep(1)
        self.companyAccountPageClass.bankAccountTypeSelect('基本账户')
        sleep(1)
        self.companyAccountPageClass.click_addEditSubmit()

    @pytest.mark.run(order=4)
    def test_deleteCompanyAccount(self):
        pass

    @pytest.mark.run(order=2)
    def test_UpdateCompanyAccount(self):
        sleep(1)
        self.companyAccountPageClass.open_companyAccount()

        sleep(1)
        self.companyAccountPageClass.input_selectCode('test')

        sleep(1)
        self.companyAccountPageClass.click_selectButton()

        sleep(1)
        self.companyAccountPageClass.click_editButton()

        sleep(1)
        self.companyAccountPageClass.input_priorityInput('100')
        sleep(1)
        self.companyAccountPageClass.accountingEntitySelect('爆破核算主体')
        sleep(1)
        self.companyAccountPageClass.input_code('test1')
        sleep(1)
        self.companyAccountPageClass.subBankSelect('中国工商银行深圳市景田支行', '中国工商银行', '102584002985')
        sleep(1)
        self.companyAccountPageClass.input_bankAccountName('测试专用账户')
        sleep(1)
        self.companyAccountPageClass.input_bankAccountNum('13121196337002')
        sleep(1)
        self.companyAccountPageClass.collectionTypeSelect('收付款')
        sleep(1)
        self.companyAccountPageClass.currencyIdSelect('CNY')
        sleep(1)
        self.companyAccountPageClass.bankAccountTypeSelect('一般账户')
        sleep(1)
        self.companyAccountPageClass.click_addEditSubmit()

    @pytest.mark.run(order=3)
    def test_selectCompanyAccount(self):
        pass


class TestPayMethodPageClass(object):

    def setup_class(self):
        self.login = LoginDepend('baseHost')
        self.payMethodPageClass = PayMethodPageClass(self.login.driver)

    def teardown_class(self):
        pass

    def test_addPayMethod(self):
        WebDriverWait(self.payMethodPageClass.driver, 5).until(
            EC.visibility_of_element_located(self.payMethodPageClass.getPaymentCenter()))

        self.payMethodPageClass.open_paymentCenter()

        self.payMethodPageClass.open_payMethod()
        sleep(1)
        self.payMethodPageClass.click_addButton()

        sleep(1)
        self.payMethodPageClass.input_priorityInput('5000')
        sleep(1)
        self.payMethodPageClass.input_code('test')
        sleep(1)
        self.payMethodPageClass.input_paymentNameC('测试')
        sleep(1)
        self.payMethodPageClass.input_paymentNameE('test')
        sleep(1)
        self.payMethodPageClass.accountingEntitySelect('爆破核算主体')
        sleep(1)
        self.payMethodPageClass.paymentModeBoeSelect('日常费用报账单')
        sleep(1)
        self.payMethodPageClass.onAccountFlagSelect('不挂账')
        sleep(1)
        self.payMethodPageClass.transferFundFlagSelect('转账')
        sleep(1)
        self.payMethodPageClass.whetherToBankAccountFlagSelect(flag=True)
        sleep(1)
        self.payMethodPageClass.click_subjectAdd()
        sleep(1)
        self.payMethodPageClass.subjectAccountingEntitySelect('爆破核算主体')
        sleep(1)
        self.payMethodPageClass.subjectCodeSelect('00')
        sleep(1)
        self.payMethodPageClass.click_subjectAddSubmit()
        sleep(1)
        self.payMethodPageClass.click_paymentSubmit()
