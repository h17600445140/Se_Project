# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageClass.common.boeCommon import BoeCommon
from PageClass.easIndexPageClass.easIndexPage import EasIndexPage
from Util import logger



class ComFeeApplyBoePage(EasIndexPage,BoeCommon):


    def __init__(self, driver):
        EasIndexPage.__init__(self, driver)

    # 费用区

    # 申请类型
    _operationSubTypeId = (By.ID, 'cost.0.operationSubTypeId')
    def click_operationSubTypeId(self):
        self.click(*self._operationSubTypeId)
    def input_operationSubTypeId(self, text):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self._operationSubTypeId))
        self.click(*self._operationSubTypeId)
        self.send_text(text, *self._operationSubTypeId)
        logger.info("选择的申请类型为：{}".format(text))
        sleep(1)

    # 申请金额
    _expenseAmount = (By.ID, 'cost.0.expenseAmount')
    def input_expenseAmount(self, text):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self._expenseAmount))
        self.input_amount(text, *self._expenseAmount)
        logger.info("输入的申请金额为：{}".format(text))

    # 申请说明
    _remark = (By.ID, 'cost.0.remark')
    def input_remark(self, text):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self._remark))
        self.clear(*self._remark)
        self.send_text(text, *self._remark)
        logger.info("输入的申请说明为：{}".format(text))







