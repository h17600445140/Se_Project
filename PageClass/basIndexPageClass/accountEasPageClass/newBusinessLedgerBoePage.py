# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageClass.basIndexPageClass.basIndexPage import BasIndexPage
from PageClass.common.boeCommon import BoeCommon

from Util import logger



# 业务记账单（新）
class NewBusinessLedgerBoePage(BasIndexPage,BoeCommon):

    def __init__(self, driver):
        BasIndexPage.__init__(self, driver)


    # 业务类型
    def input_costOperationSubType(self, text, count='0'):
        self._costOperationSubType = (By.ID, 'cost.{}.operationSubTypeId'.format(count))
        self.find_elements(*self._costOperationSubType)[len(self.find_elements(*self._costOperationSubType))-1].click()
        self.find_elements(*self._costOperationSubType)[len(self.find_elements(*self._costOperationSubType))-1].send_keys(text)
        sleep(1)
        logger.info("选择的业务类型为：{}".format(text))


    # 成本中心
    def selectCostExpenseDept(self, deptCode, deptName='', count='0'):
        self._costExpenseDept = (By.ID, 'cost.{}.expenseDeptId'.format(count))
        self.find_elements(*self._costExpenseDept)[len(self.find_elements(*self._costExpenseDept))-1].click()
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
        logger.info('选择的部门编码为 : {}'.format(deptCode))
        logger.info('选择的部门名称为 : {}'.format(deptName))
        self.click(*(By.XPATH, '/html/body//div//span/button[2]'))


    # 项目
    def input_costProject(self, text, count='0'):
        self._costProject = (By.ID, 'cost.{}.projectId'.format(count))
        self.find_elements(*self._costProject)[len(self.find_elements(*self._costProject))-1].click()
        self.find_elements(*self._costProject)[len(self.find_elements(*self._costProject))-1].send_keys(text)
        sleep(1)
        logger.info("选择的项目为：{}".format(text))


    # 总金额
    def input_costExpenseAmount(self, text, count='0'):
        self._costExpenseAmount = (By.ID, 'cost.{}.expenseAmount'.format(count))
        self.find_elements(*self._costExpenseAmount)[len(self.find_elements(*self._costExpenseAmount))-2].click()
        element = self.find_elements(*self._costExpenseAmount)[len(self.find_elements(*self._costExpenseAmount))-2]
        self.find_elements(*self._costExpenseAmount)[len(self.find_elements(*self._costExpenseAmount))-2].send_keys(Keys.BACKSPACE)
        ActionChains(self.driver).send_keys_to_element(element, text).perform()
        logger.info('输入的总金额为 : {}'.format(text))


    # 新增明细信息按钮
    _addDetailButton = (By.XPATH, '/html/body//form/div[7]/div/button[1]')
    def click_addDetailButton(self):
        self.find_elements(*self._addDetailButton)[len(self.find_elements(*self._addDetailButton))-1].click()
        logger.info('点击新增明细信息按钮')