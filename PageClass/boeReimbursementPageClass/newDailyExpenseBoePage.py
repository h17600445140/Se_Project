# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from PageClass.common.boeCommon import BoeCommon
from PageClass.easIndexPageClass.easIndexPage import EasIndexPage
from Util import logger


class NewDailyExpenseBoePage(EasIndexPage,BoeCommon):

    _newDailyExpenseBoe = (By.XPATH, '//*[@id="app"]/section/main/div/div/div[2]/div[3]/div[3]/div/div[2]/div[1]/div[2]/div/div[1]/i')

    # 关联发票
    _relatedInvoice = (By.XPATH, '//*[@id="cost"]/div/div/button[1]')
    # 业务小类
    _operationSubType =  (By.XPATH, '/html//div[1]/div/div[2]/div[3]/div[2]/div/span')

    def __init__(self, driver):
        EasIndexPage.__init__(self, driver)

    def open_newDailyExpenseBoe(self):
        self.click(*self._newDailyExpenseBoe)

    def selectRelatedInvoice(self, invoiceCode):
        self.click(*self._relatedInvoice)
        self.send_text(invoiceCode, *(By.ID, 'itemairNumber'))
        self.click(*(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div/div[1]/form/div[4]/div/button[1]'))
        sleep(1)
        self.click(*(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div/div[3]/div/div[1]/div[1]/div/div/div[2]/div'))
        self.click(*(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[3]/span/button'))
        logger.info("选择的关联发票为：{}".format(invoiceCode))

    def selectOperationSubType(self, subType):
        self.click(*self._operationSubType)
        self.send_text(subType, *(By.ID, 'itemname'))
        self.click(*(By.XPATH, '/html/body//form/div[3]/div/button[1]'))
        sleep(1)
        self.click(*(By.XPATH, '/html/body//div[2]/div/div[1]/div[3]/table/tbody/tr'))
        self.click(*(By.XPATH, '/html/body//div[3]/span/button[2]'))
        logger.info("选择的业务类型为：{}".format(subType))







