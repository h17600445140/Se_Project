# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageClass.basIndexPageClass.basIndexPage import BasIndexPage
from PageClass.common.boeCommon import BoeCommon
from Util import logger



# 资金调拨报账单（新）
class NewFundAllocationBoePage(BasIndexPage,BoeCommon):

    def __init__(self, driver):
        BasIndexPage.__init__(self, driver)


    def selectReceiveVendor(self, acountName):
        """
        describe：
                选择付款账号
        :param acountName: 账号名称
        :return: None
        """
        self.click(*(By.ID, 'boeHeaderChild.0.paymentAccountId'))
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(
            (By.ID, 'itembankAccountName')))
        self.send_text(acountName, *(By.ID, 'itembankAccountName'))
        self.click(*(By.XPATH, '/html/body//form/div[2]/div/button[1]'))
        sleep(1)
        try:
            self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[
                len(self.find_elements(*(By.CLASS_NAME, 'el-table__row'))) - 1].click()
        except:
            logger.warning('警告,第一次没找到,重新查找点击')
            self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[
                len(self.find_elements(*(By.CLASS_NAME, 'el-table__row'))) - 1].click()
        logger.info('选择的账号名称为 : {}'.format(acountName))
        self.click(*(By.XPATH, '/html/body//div//span/button[2]'))


    def addAccount(self, payee, bankAccount=''):
        """
        describe：
                添加账户
        :param postalOrderCode: 汇票编码
        :return: None
        """
        self.clickTargetButton('添加账户')
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(
            (By.ID, 'itemname')))
        self.send_text(payee, *(By.ID, 'itemname'))
        self.send_text(bankAccount, *(By.ID, 'itembankAccount'))
        self.click(*(By.XPATH, '/html/body//form/div[3]/div/button[1]'))
        sleep(1)
        try:
            self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[
                len(self.find_elements(*(By.CLASS_NAME, 'el-table__row'))) - 1].click()
        except:
            logger.warning('警告,第一次没找到,重新查找点击')
            self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[
                len(self.find_elements(*(By.CLASS_NAME, 'el-table__row'))) - 1].click()
        logger.info('选择的收款人为 : {}'.format(payee))
        logger.info('选择的银行账户为 : {}'.format(bankAccount))
        self.click(*(By.XPATH, '/html/body//div//span/button[2]'))


    def input_transferAmount(self, text):
        """
        describe：
                输入调拨金额
        :param text: 调拨金额
        :return: None
        """
        self.input_amount(text, *(By.XPATH, '/html//div[1]/div/div[2]/div[3]/div[2]/div/div[5]/div'))
        logger.info('输入的調撥金额为 : {}'.format(text))