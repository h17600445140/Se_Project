# -*- coding:utf-8 -*-
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from PageClass.common.boeCommon import BoeCommen
from PageClass.easIndexPageClass.easIndexPage import EasIndexPage



class NewDailyExpenseBoePage(EasIndexPage,BoeCommen):

    _newDailyExpenseBoe = (By.XPATH, '//*[@id="app"]/section/main/div/div/div[2]/div[3]/div[3]/div/div[2]/div[1]/div[2]/div/div[1]/i')

    # 关联发票
    _relatedInvoice = (By.XPATH, '//*[@id="cost"]/div/div/button[1]')
    # 业务小类
    _operationSubType =  (By.XPATH, '/html/body/div[1]/div/div[2]/div[3]/div[2]/div/span')

    # 部门
    _expenseDeptId = (By.ID, 'apportion.0.expenseDeptId')
    # 项目
    _projectId = (By.ID, 'apportion.0.projectId')
    # 总金额
    _expenseAmount = (By.ID, 'apportion.0.expenseAmount')

    def __init__(self, driver):
        EasIndexPage.__init__(self, driver)

    def open_newDailyExpenseBoe(self):
        self.click(*self._newDailyExpenseBoe)

    def selectRelatedInvoice(self, invoiceCode):
        self.click(*self._relatedInvoice)
        self.send_text(invoiceCode, *(By.ID, 'itemairNumber'))
        self.click(*(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div/div[1]/form/div[4]/div/button[1]'))
        self.click(*(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div/div[3]/div/div[1]/div[1]/div/div/div[2]/div'))
        self.click(*(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[3]/span/button'))

    def selectOperationSubType(self, subType):
        self.click(*self._operationSubType)
        self.send_text(subType, *(By.ID, 'itemname'))
        self.click(*(By.XPATH, '/html/body//form/div[3]/div/button[1]'))
        self.click(*(By.XPATH, '/html/body//div[2]/div/div[1]/div[3]/table/tbody/tr'))
        self.click(*(By.XPATH, '/html/body//div[3]/span/button[2]'))

    def selectDepartment(self, deptName):
        self.click(*self._expenseDeptId)
        self.send_text(deptName, *(By.ID, 'itemDEPT_NAME'))
        self.click(*(By.XPATH, '/html/body//form/div[3]/div/button[1]'))
        self.click(*(By.XPATH, '/html/body//div[2]/div/div[1]/div[3]/table/tbody/tr[1]'))
        self.click(*(By.XPATH, '/html/body//span/button[2]'))

    def input_projectId(self, text):
        self.click(*self._projectId)
        self.send_text(text, *self._projectId)

    def input_expenseAmount(self, text):
        self.click(*self._expenseAmount)
        element = self.find_element(*self._expenseAmount)
        ActionChains(self.driver).send_keys_to_element(element, Keys.BACKSPACE).perform()
        ActionChains(self.driver).send_keys_to_element(element, text).perform()






