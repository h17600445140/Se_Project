# -*- coding:utf-8 -*-


from selenium.webdriver.common.by import By
from PageClass.easIndexPageClass.easIndexPage import EasIndexPage


class employeeLoansBoePage(EasIndexPage):

    _employeeLoansBoe = (By.XPATH, '//*[@id="app"]/section/main/div/div/div[2]/div[3]/div[3]/div/div[2]/div[1]/div[2]/div/div[1]/i')
    _boeNum = (By.XPATH, '//*[@id="top"]/span[3]')

    _employeeId = (By.ID, 'boeHeader.0.employeeId')
    _operationTypeId = (By.ID, 'boeHeader.0.operationTypeId')
    _paperAccessories = (By.ID, 'boeHeader.0.paperAccessories')
    _paymentCurrency = (By.ID, 'boeHeader.0.paymentCurrency')
    _applyBoeId = (By.ID, 'boeHeaderChild.0.applyBoeId')
    _paymentCurrency = (By.ID, 'boeHeader.0.paymentCurrency')
    _expenseAmount = (By.ID, 'loan.0.expenseAmount')
    _projectId = (By.ID, 'loan.0.projectId')
    _paymentModeCode = (By.ID, 'zfsBoePayments.0.paymentModeCode')
    _vendorId = (By.ID, 'zfsBoePayments.0.vendorId')
    _paymentAmount = (By.ID, 'zfsBoePayments.0.paymentAmount')
    _paymentMemo = (By.ID, 'zfsBoePayments.0.paymentMemo')

    def __init__(self, driver):
        EasIndexPage.__init__(self, driver)

    def open_employeeLoansBoe(self):
        self.click(*self._employeeLoansBoe)

    def getBoeNum(self):
        return self.get_elementText(*self._boeNum)