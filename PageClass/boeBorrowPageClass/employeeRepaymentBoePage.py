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



class EmployeeRepaymentBoePage(EasIndexPage,BoeCommon):

    _employeeRepaymentBoe = (By.XPATH, '//*[@id="app"]/section/main/div/div/div[2]/div[3]/div[3]/div/div[2]/div[2]/div[2]/div/div[1]/i')


    # 还款金额
    _expenseAmount = (By.ID, 'loan.0.expenseAmount')
    # 收款账号
    _favoriteId = (By.ID, 'loan.0.favoriteId')
    # 还款日期
    _loanRepaymentDate = (By.ID, 'loan.0.loanRepaymentDate')
    # 还款说明
    _remark = (By.ID, 'loan.0.remark')

    # 我要核销
    _writeOffButton = (By.XPATH, '//*[@id="loan"]/div/div/button')

    def __init__(self, driver):
        EasIndexPage.__init__(self, driver)

    def open_employeeRepaymentBoe(self):
        self.click(*self._employeeRepaymentBoe)

    # 翻页代码代更新
    def selectWriteOffBoe(self, boeNum):
        sleep(1)
        boeFee = None
        self.click(*(By.ID, 'tab-001'))
        for i in range(1, 6):
            if self.get_elementText(*(By.XPATH, '//*[@id="pane-001"]//table/tbody/tr[{}]/td[3]/div'.format(i))) == boeNum:
                boeFee = self.get_elementText(*(By.XPATH, '//*[@id="pane-001"]//table/tbody/tr[{}]/td[8]/div'.format(i)))
                self.click(*(By.XPATH, '//*[@id="pane-001"]//table/tbody/tr[{}]/td[1]/div/label/span/span'.format(i)))
                self.click(*(By.XPATH, '/html/body//span/button[2]'.format(i)))
                break
        return boeFee

    # 还款方式
    _operationSubTypeId = (By.ID, 'loan.0.operationSubTypeId')
    def selectReplaymentType(self, option):
        self.click(*self._operationSubTypeId)
        # sleep(1)
        # for i in range(0, 2):
        #     # logger.info("业务类型为：{}".format(self.find_element(*(By.ID, 'loan.0.operationSubTypeId.option.{}'.format(i))).text))
        #     # logger.info(self.find_element(*(By.ID, 'loan.0.operationSubTypeId.option.{}'.format(i))).is_displayed())
        #     # print(type(self.find_element(*(By.ID, 'loan.0.operationSubTypeId.option.{}'.format(i))).text))
        #
        #     if self.get_elementText(*(By.ID, 'loan.0.operationSubTypeId.option.{}'.format(i))) == type:
        #         self.click(*(By.ID, 'loan.0.operationSubTypeId.option.{}'.format(i)))
        #         break
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self._operationSubTypeId))
        self.select_item(option)
        logger.info('选择的还款方式为：{}'.format(option))


    def input_expenseAmount(self, text):
        self.click(*self._expenseAmount)
        element = self.find_element(*self._expenseAmount)
        ActionChains(self.driver).send_keys_to_element(element, Keys.BACKSPACE).perform()
        ActionChains(self.driver).send_keys_to_element(element, text).perform()
        logger.info('还款金额为：{}'.format(text))

    def selectCollectionAccount(self, accountName):
        self.click(*self._favoriteId)
        sleep(3)
        self.send_text(accountName, *(By.ID, 'itemBANK_ACCOUNT_NAME'))
        self.click(*(By.XPATH, '/html/body//form/div[2]/div/button[1]'))
        self.click(*(By.XPATH, '/html/body//table/tbody/tr'))
        self.click(*(By.XPATH, '/html/body//span/button[2]'))
        logger.info('选择的还款账户为：{}'.format(accountName))

    def selectLoanRepaymentDate(self, date):
        self.click(*self._loanRepaymentDate)
        year, month, day = date.split('-')[0], date.split('-')[1], date.split('-')[2]
        self.select_date(year, month, day)
        logger.info('选择的还款日期为：{}'.format(date))

    def input_remark(self, text):
        self.send_text(text, *self._remark)
        logger.info('还款说明为：{}'.format(text))