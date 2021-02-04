# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageClass.basIndexPageClass.basIndexPage import BasIndexPage
from PageClass.common.boeCommon import BoeCommon
from Util import logger



# 收入报账单
class NewIncomeStatementBoePage(BasIndexPage,BoeCommon):

    def __init__(self, driver):
        BasIndexPage.__init__(self, driver)

    # 订单编号
    _orderNumber = (By.ID, 'cost.0.orderNumber')
    def input_orderNumber(self, text):
        self.send_text(text, *self._orderNumber)
        logger.info('输入的订单编号为：{}'.format(text))

    # 收入类型
    _operationSubType = (By.ID, 'cost.0.operationSubTypeId')
    def input_operationSubType(self, text):
        self.click(*self._operationSubType)
        self.send_text(text, *self._operationSubType)
        logger.info('输入的收入类型为：{}'.format(text))

    # 利润中心
    _costExpenseDept = (By.ID, 'cost.0.expenseDeptId')
    def click_costExpenseDept(self):
        self.click(*self._costExpenseDept)
    def selectExpenseDept(self, deptCode, deptName=''):
        self.click_costExpenseDept()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(
            (By.ID, 'itemDEPT_CODE')))
        self.send_text(deptCode, *(By.ID, 'itemDEPT_CODE'))
        self.send_text(deptName, *(By.ID, 'itemDEPT_NAME'))
        self.click(*(By.XPATH, '/html/body//form/div[3]/div/button[1]'))
        sleep(1)
        try:
            self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[
                len(self.find_elements(*(By.CLASS_NAME, 'el-table__row'))) - 1].click()
        except:
            logger.warning('警告,第一次没找到,重新查找点击')
            self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[
                len(self.find_elements(*(By.CLASS_NAME, 'el-table__row'))) - 1].click()
        logger.info('选择利润中心编码为 : {}'.format(deptCode))
        logger.info('选择利润中心名称为 : {}'.format(deptName))
        self.click(*(By.XPATH, '/html/body//div//span/button[2]'))

    # 金额
    _incomeDetailExpenseAmount = (By.ID, 'cost.0.expenseAmount')
    def input_incomeDetailExpenseAmount(self, text):
        self.input_amount(text, *self._incomeDetailExpenseAmount)
        logger.info('输入的金额为：{}'.format(text))

    # 税额
    _incomeDetailTaxAmount = (By.ID, 'cost.0.taxAmount')
    def input_incomeDetailTaxAmount(self, text):
        self.input_amount(text, *self._incomeDetailTaxAmount)
        logger.info('输入的税额为：{}'.format(text))