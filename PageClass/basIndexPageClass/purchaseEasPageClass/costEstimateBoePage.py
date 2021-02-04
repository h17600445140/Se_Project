# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageClass.basIndexPageClass.basIndexPage import BasIndexPage
from PageClass.common.boeCommon import BoeCommon
from Util import logger




# 成本暂估（旧）
class CostEstimateBoePage(BasIndexPage,BoeCommon):

    def __init__(self, driver):
        BasIndexPage.__init__(self, driver)


    # 订单编号
    _costOrderNumber = (By.ID, 'cost.0.orderNumber')
    def input_costOrderNumber(self, text):
        self.send_text(text, *self._costOrderNumber)
        logger.info('输入的订单编号为：{}'.format(text))


    # 业务小类
    _costOperationSubType = (By.ID, 'cost.0.operationSubTypeId')
    def input_costOperationSubType(self, text):
        self.click(*self._costOperationSubType)
        self.send_text(text, *self._costOperationSubType)
        sleep(1)
        logger.info('输入的业务小类为：{}'.format(text))


    # 总金额
    _costExpenseAmount = (By.ID, 'cost.0.expenseAmount')
    def input_costExpenseAmount(self, text):
        self.input_amount(text, *self._costExpenseAmount)
        logger.info('输入的总金额为 : {}'.format(text))


    # 责任部门
    _costCc = (By.ID, 'cost.0.ccId')
    def click_costCc(self):
        self.click(*self._costCc)
    def selectCc(self, deptCode, deptName=''):
        self.click_costCc()
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
        logger.info('选择的责任部门编码为 : {}'.format(deptCode))
        logger.info('选择的责任部门名称为 : {}'.format(deptName))
        self.click(*(By.XPATH, '/html/body//div//span/button[2]'))


    # 项目
    _costProject = (By.ID, 'cost.0.projectId')
    def input_costProject(self, text):
        self.click(*self._costProject)
        self.send_text(text, *self._costProject)
        logger.info('输入的项目为：{}'.format(text))
        sleep(1)


    # 备注
    _costRemark = (By.ID, 'cost.0.remark')
    def input_costRemark(self, text):
        self.send_text(text, *self._costRemark)
        logger.info('输入的备注为：{}'.format(text))