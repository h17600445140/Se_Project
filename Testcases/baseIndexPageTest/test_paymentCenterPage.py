# -*- coding:utf-8 -*-
from time import sleep

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageClass.baseIndexPageClass.paymentCenterPage import CompanyAccountPage, PayMethodPage
from Testcases.common.loginDepend import LoginDepend



class TestCompanyAccountPage(object):

    def setup_class(self):
        self.login = LoginDepend('baseHost', 'user')
        self.companyAccountPage = CompanyAccountPage(self.login.driver)

    def teardown_class(self):
        self.companyAccountPage.driver.quit()

    @pytest.mark.run(order=1)
    def test_addCompanyAccount(self):
        WebDriverWait(self.companyAccountPage.driver, 5).until(
            EC.visibility_of_element_located(self.companyAccountPage.getPaymentCenter()))

        self.companyAccountPage.open_paymentCenter()

        self.companyAccountPage.open_companyAccount()

        self.companyAccountPage.click_addButton()

        sleep(1)
        self.companyAccountPage.input_priorityInput('100')
        sleep(1)
        self.companyAccountPage.accountingEntitySelect('hc核算主体')
        sleep(1)
        self.companyAccountPage.input_code('test')
        sleep(1)
        self.companyAccountPage.subBankSelect('中国工商银行深圳市景田支行', '中国工商银行', '102584002985')
        sleep(1)
        self.companyAccountPage.input_bankAccountName('测试专用账户')
        sleep(1)
        self.companyAccountPage.input_bankAccountNum('13121196337001')
        sleep(1)
        self.companyAccountPage.collectionTypeSelect('收付款')
        sleep(1)
        self.companyAccountPage.currencyIdSelect('CNY')
        sleep(1)
        self.companyAccountPage.bankAccountTypeSelect('基本账户')
        sleep(1)
        self.companyAccountPage.click_addEditSubmit()

    @pytest.mark.run(order=4)
    def test_deleteCompanyAccount(self):
        pass

    @pytest.mark.run(order=2)
    def test_UpdateCompanyAccount(self):
        sleep(1)
        self.companyAccountPage.open_companyAccount()

        sleep(1)
        self.companyAccountPage.input_selectCode('test')

        sleep(1)
        self.companyAccountPage.click_selectButton()

        sleep(1)
        self.companyAccountPage.click_editButton()

        sleep(1)
        self.companyAccountPage.input_priorityInput('100')
        sleep(1)
        self.companyAccountPage.accountingEntitySelect('爆破核算主体')
        sleep(1)
        self.companyAccountPage.input_code('test1')
        sleep(1)
        self.companyAccountPage.subBankSelect('中国工商银行深圳市景田支行', '中国工商银行', '102584002985')
        sleep(1)
        self.companyAccountPage.input_bankAccountName('测试专用账户')
        sleep(1)
        self.companyAccountPage.input_bankAccountNum('13121196337002')
        sleep(1)
        self.companyAccountPage.collectionTypeSelect('收付款')
        sleep(1)
        self.companyAccountPage.currencyIdSelect('CNY')
        sleep(1)
        self.companyAccountPage.bankAccountTypeSelect('一般账户')
        sleep(1)
        self.companyAccountPage.click_addEditSubmit()

    @pytest.mark.run(order=3)
    def test_selectCompanyAccount(self):
        pass



class TestPayMethodPage(object):

    def setup_class(self):
        self.login = LoginDepend('baseHost', 'user')
        self.payMethodPage = PayMethodPage(self.login.driver)

    def teardown_class(self):
        pass

    def test_addPayMethod(self):
        WebDriverWait(self.payMethodPage.driver, 5).until(
            EC.visibility_of_element_located(self.payMethodPage.getPaymentCenter()))

        self.payMethodPage.open_paymentCenter()

        self.payMethodPage.open_payMethod()
        sleep(1)
        self.payMethodPage.click_addButton()

        sleep(1)
        self.payMethodPage.input_priorityInput('5000')
        sleep(1)
        self.payMethodPage.input_code('test')
        sleep(1)
        self.payMethodPage.input_paymentNameC('测试')
        sleep(1)
        self.payMethodPage.input_paymentNameE('test')
        sleep(1)
        self.payMethodPage.accountingEntitySelect('hc核算主体')
        sleep(1)
        self.payMethodPage.paymentModeBoeSelect('日常费用报账单')
        sleep(1)
        self.payMethodPage.onAccountFlagSelect('不挂账')
        sleep(1)
        self.payMethodPage.transferFundFlagSelect('转账')
        sleep(1)
        self.payMethodPage.whetherToBankAccountFlagSelect(flag=True)
        sleep(1)
        self.payMethodPage.click_subjectAdd()
        sleep(1)
        self.payMethodPage.subjectAccountingEntitySelect('爆破核算主体')
        sleep(1)
        self.payMethodPage.subjectCodeSelect('00')
        sleep(1)
        self.payMethodPage.click_subjectAddSubmit()
        sleep(1)
        self.payMethodPage.click_paymentSubmit()
