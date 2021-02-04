# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By
from PageClass.basIndexPageClass.basIndexPage import BasIndexPage
from PageClass.common.boeCommon import BoeCommon
from Util import logger



# 采购预付
class NewPurchasePrepaymentBoePage(BasIndexPage,BoeCommon):

    def __init__(self, driver):
        BasIndexPage.__init__(self, driver)


    # 采购订单
    _loanOrderNumber = (By.ID, 'loan.0.orderNumber')
    def input_loanOrderNumber(self, text):
        self.send_text(text, *self._loanOrderNumber)
        logger.info('输入的采购订单为：{}'.format(text))


    # 预付类型
    _loanOperationSubType = (By.ID, 'loan.0.operationSubTypeId')
    def input_loanOperationSubType(self, text):
        self.click(*self._loanOperationSubType)
        self.send_text(text, *self._loanOperationSubType)
        sleep(1)
        logger.info('输入的预付类型为：{}'.format(text))


    # 预付金额
    _loanExpenseAmount = (By.ID, 'loan.0.expenseAmount')
    def input_loanExpenseAmount(self, text):
        self.input_amount(text, *self._loanExpenseAmount)
        logger.info('输入的预付金额为 : {}'.format(text))


