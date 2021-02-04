# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PageClass.basIndexPageClass.basIndexPage import BasIndexPage
from PageClass.common.boeCommon import BoeCommon
from Util import logger



# 总账单
class NewBoeTypeGeneralLedgerBoePage(BasIndexPage,BoeCommon):

    def __init__(self, driver):
        BasIndexPage.__init__(self, driver)


    # 总账记账日期
    _glDate = (By.ID, 'boeHeader.0.glDate')
    def select_glDate(self, date):
        self.click(*self._glDate)
        year, month, day = date.split('-')[0], date.split('-')[1], date.split('-')[2]
        self.select_date(year, month, day)
        logger.info('选择的总账记账日期为：{}'.format(date))


    # 摘要
    _voucherRemark = (By.ID, 'voucher.0.remark')
    def input_voucherRemark(self, text, count='0'):
        self._voucherRemark = (By.ID, 'voucher.{}.remark'.format(count))
        self.find_elements(*self._voucherRemark)[len(self.find_elements(*self._voucherRemark))-1].click()
        self.find_elements(*self._voucherRemark)[len(self.find_elements(*self._voucherRemark))-1].send_keys(text)
        logger.info("输入的摘要为：{}".format(text))


    # 会计科目
    def input_voucherAccount(self, text, count='0'):
        self._voucherAccount = (By.ID, 'voucher.{}.accountId'.format(count))
        self.find_elements(*self._voucherAccount)[len(self.find_elements(*self._voucherAccount))-1].click()
        sleep(1)
        self.find_elements(*self._voucherAccount)[len(self.find_elements(*self._voucherAccount))-1].send_keys(text)
        logger.info("选择的会计科目为：{}".format(text))


    # 借方金额
    def input_voucherDebitAmount(self, text, count='0'):
        self._voucherDebitAmount = (By.ID, 'voucher.{}.debitAmount'.format(count))
        self.find_elements(*self._voucherDebitAmount)[len(self.find_elements(*self._voucherDebitAmount))-2].click()
        element = self.find_elements(*self._voucherDebitAmount)[len(self.find_elements(*self._voucherDebitAmount))-2]
        self.find_elements(*self._voucherDebitAmount)[len(self.find_elements(*self._voucherDebitAmount))-2].send_keys(Keys.BACKSPACE)
        ActionChains(self.driver).send_keys_to_element(element, text).perform()
        logger.info('输入的借方金额为 : {}'.format(text))


    # 贷方金额
    def input_voucherCreditAmount(self, text, count='0'):
        self._voucherCreditAmount = (By.ID, 'voucher.{}.creditAmount'.format(count))
        self.find_elements(*self._voucherCreditAmount)[len(self.find_elements(*self._voucherCreditAmount))-2].click()
        element = self.find_elements(*self._voucherCreditAmount)[len(self.find_elements(*self._voucherCreditAmount))-2]
        self.find_elements(*self._voucherCreditAmount)[len(self.find_elements(*self._voucherCreditAmount))-2].send_keys(Keys.BACKSPACE)
        ActionChains(self.driver).send_keys_to_element(element, text).perform()
        logger.info('输入的贷方金额为 : {}'.format(text))


    _addVoucherButton = (By.XPATH, '/html/body//form/div[9]/div/button[1]')
    def click_addVoucherButton(self):
        self.find_elements(*self._addVoucherButton)[len(self.find_elements(*self._addVoucherButton))-1].click()
        logger.info('点击新增凭证分录按钮')