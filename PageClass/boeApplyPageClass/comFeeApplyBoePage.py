# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from PageClass.common.boeCommon import BoeCommen
from PageClass.easIndexPageClass.easIndexPage import EasIndexPage



class ComFeeApplyBoePage(EasIndexPage,BoeCommen):

    _comFeeApplyBoe = (By.XPATH, '//*[@id="app"]/section/main/div/div/div[2]/div[3]/div[3]/div/div[2]/div[1]/div[2]/div/div[1]/i')
    _boeNum = (By.XPATH, '//*[@id="top"]/span[3]')


    # 主表区
    # _employee = (By.ID, 'boeHeader.0.employeeId')
    # _operationType = (By.ID, 'boeHeader.0.operationTypeId')
    # _paperAccessories = (By.ID, 'boeHeader.0.paperAccessories')
    # _boeAbstract = (By.ID, 'boeHeader.0.boeAbstract')


    # 费用区
    _operationSubTypeId = (By.ID, 'cost.0.operationSubTypeId')
    _expenseAmount = (By.ID, 'cost.0.expenseAmount')
    _remark = (By.ID, 'cost.0.remark')


    def __init__(self, driver):
        EasIndexPage.__init__(self, driver)

    def open_comFeeApplyBoe(self):
        self.click(*self._comFeeApplyBoe)

    def getBoeNum(self):
        return self.get_elementText(*self._boeNum)

    # def input_operationType(self, text):
    #     self.clear(*self._operationType)
    #     self.send_text(text, *self._operationType)

    # def input_boeAbstract(self, text):
    #     self.clear(*self._boeAbstract)
    #     self.send_text(text, *self._boeAbstract)
    #
    # def getBoeAbstract(self):
    #     return self._boeAbstract

    def input_operationSubTypeId(self, text):
        self.clear(*self._operationSubTypeId)
        self.send_text(text, *self._operationSubTypeId)

    def input_expenseAmount(self, text):
        self.click(*self._expenseAmount)
        element = self.find_element(*self._expenseAmount)
        ActionChains(self.driver).send_keys_to_element(element, Keys.BACKSPACE).perform()
        ActionChains(self.driver).send_keys_to_element(element, text).perform()

    def input_remark(self, text):
        self.clear(*self._remark)
        self.send_text(text, *self._remark)







