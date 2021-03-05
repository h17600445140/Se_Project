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



# 预提申请单（新）
class NewWithholdingAmortizationPage(BasIndexPage,BoeCommon):

    def __init__(self, driver):
        BasIndexPage.__init__(self, driver)


    # 预提规则
    _yuTiRule = (By.ID, 'boeHeaderChild.0.rule')
    def selectYuTiRule(self, type):
        self.click(*self._yuTiRule)
        self.select_item(type)
        logger.info('输入的预提规则为：{}'.format(type))


    # 预提类型
    _costOperationSubType = (By.ID, 'cost.0.operationSubTypeId')
    def input_costOperationSubType(self, text):
        self.click(*self._costOperationSubType)
        self.send_text(text, *self._costOperationSubType)
        logger.info('输入的预提类型为：{}'.format(text))


    # 责任部门
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


    # 金额
    def input_costExpenseAmount(self, text, count='0'):
        self._costExpenseAmount = (By.ID, 'cost.{}.expenseAmount'.format(count))
        self.find_elements(*self._costExpenseAmount)[len(self.find_elements(*self._costExpenseAmount))-2].click()
        element = self.find_elements(*self._costExpenseAmount)[len(self.find_elements(*self._costExpenseAmount))-2]
        self.find_elements(*self._costExpenseAmount)[len(self.find_elements(*self._costExpenseAmount))-2].send_keys(Keys.BACKSPACE)
        ActionChains(self.driver).send_keys_to_element(element, text).perform()
        logger.info('输入的总金额为 : {}'.format(text))


    # 开始日期
    def select_costBeginDateStr(self, date, count='0'):
        self._costBeginDateStr = (By.ID, 'cost.{}.beginDateStr'.format(count))
        self.find_elements(*self._costBeginDateStr)[len(self.find_elements(*self._costBeginDateStr))-1].click()
        year, month, day = date.split('-')[0], date.split('-')[1], date.split('-')[2]
        self.select_date(year, month, day)
        logger.info('选择的开始日期为：{}'.format(date))


    # 期限
    def input_costTheTerm(self, text, count='0'):
        self._costTheTerm = (By.ID, 'cost.{}.theTerm'.format(count))

        self._costViewDetails = (By.ID, 'cost.0.viewDetails')
        elements = self.find_elements(*self._costViewDetails)[len(self.find_elements(*self._costViewDetails))-1]
        self.driver.execute_script("arguments[0].scrollIntoView();", elements)

        self.find_elements(*self._costTheTerm)[len(self.find_elements(*self._costTheTerm))-1].click()
        element = self.find_elements(*self._costTheTerm)[len(self.find_elements(*self._costTheTerm))-1]
        ActionChains(self.driver).send_keys_to_element(element, Keys.ARROW_RIGHT).send_keys_to_element(element, Keys.BACKSPACE).perform()
        ActionChains(self.driver).send_keys_to_element(element, text).perform()
        logger.info('输入的期限（月）为 : {}'.format(text))
        print(len(self.find_elements(*self._costTheTerm)))


    # 贷方科目
    def input_voucherAccount(self, text, count='0'):
        self._voucherAccount = (By.ID, 'cost.{}.accountId'.format(count))

        self._costViewDetails = (By.XPATH, '/html/body//form/div[11]')
        elements = self.find_elements(*self._costViewDetails)[len(self.find_elements(*self._costViewDetails))-1]
        self.driver.execute_script("arguments[0].scrollIntoView();", elements)

        self.find_elements(*self._voucherAccount)[len(self.find_elements(*self._voucherAccount))-1].click()
        sleep(1)
        self.find_elements(*self._voucherAccount)[len(self.find_elements(*self._voucherAccount))-1].send_keys(text)
        logger.info("选择的贷方科目为：{}".format(text))


    def click_autoCalculation(self):
        self.click(*(By.XPATH, '//*[@id="app"]/div[1]/div/div[2]/div[3]/div[2]/div[1]/div/div[2]/div/form/div/div/button[3]'))
        logger.info('点击自动计算')
        sleep(1)
        self.click(*(By.XPATH, '//*[@id="app"]//span/button[2]'))
