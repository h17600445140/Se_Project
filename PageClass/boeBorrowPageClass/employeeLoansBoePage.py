# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from PageClass.common.boeCommon import BoeCommon
from PageClass.easIndexPageClass.easIndexPage import EasIndexPage
from Util import logger


class EmployeeLoansBoePage(EasIndexPage,BoeCommon):

    _employeeLoansBoe = (By.XPATH, '//*[@id="app"]/section/main/div/div/div[2]/div[3]/div[3]/div/div[2]/div[1]/div[2]/div/div[1]/i')

    _applyBoeId = (By.ID, 'boeHeaderChild.0.applyBoeId')

    _operationSubTypeId = (By.ID, 'loan.0.operationSubTypeId')
    _expenseAmount = (By.ID, 'loan.0.expenseAmount')
    _projectId = (By.ID, 'loan.0.projectId')

    def __init__(self, driver):
        EasIndexPage.__init__(self, driver)

    def open_employeeLoansBoe(self):
        self.click(*self._employeeLoansBoe)

    def input_operationSubTypeId(self, text):
        self.click(*self._operationSubTypeId)
        self.send_text(text, *self._operationSubTypeId)
        logger.info("输入的业务为：{}".format(text))
        sleep(1)

    def input_expenseAmount(self, text):
        self.click(*self._expenseAmount)
        element = self.find_element(*self._expenseAmount)
        ActionChains(self.driver).send_keys_to_element(element, Keys.BACKSPACE).perform()
        ActionChains(self.driver).send_keys_to_element(element, text).perform()
        logger.info("输入的总金额为：{}".format(text))

    def input_projectId(self, text):
        self.click(*self._projectId)
        self.send_text(text, *self._projectId)
        logger.info("输入的项目为：{}".format(text))
        sleep(1)