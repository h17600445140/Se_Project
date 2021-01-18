# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from PageClass.basePage import BasePage
from Util import logger, config


class EasMyInvoiceIndexPage(BasePage):

    _reimbursementState = (By.ID, 'undefined_reimbursementState')
    _billTypeInvoice = (By.ID, 'undefined_billTypeInvoice')
    _billingCode = (By.ID, 'undefined_billingCode')

    _myInvoiceQueryButton = (By.XPATH, '//*[@id="app"]/section/main/div[2]/div/div[1]/div[1]/form/div[10]/div/button[1]')
    _invoiceQueryResult = (By.XPATH, '//*[@id="app"]/section/main/div[2]/div/div[1]/div[4]/div/div[1]/div/div[2]/div[1]')

    _manualInvoiceEntry = (By.XPATH, '//*[@id="app"]/section/main/div[2]/div/div[1]/div[2]/button[1]')

    _invoiceType = (By.ID, 'form_billTypeInvoice')

    # ----- 发票公用 -----
    # 发票代码
    _invoiceNo = (By.ID, 'form_billingNo')
    # 发票号码
    _invoiceCode = (By.ID, 'form_billingCode')
    # 日期
    _invoiceDate = (By.ID, 'form_billingTime')
    # 校验码
    _checkCode = (By.ID, 'form_checkCode')
    # 总金额
    _feeTotal = (By.ID, 'form_fee')
    # 税前金额
    _preFee = (By.ID, 'form_feeWithoutTax')
    # 税额
    _tax = (By.ID, 'form_tax')

    _personRemark = (By.ID, 'form_personnelAttribution')
    _personName = (By.ID, 'form_passengerName')
    _tripDate = (By.ID, 'form_tripDate')
    _ticketPrice = (By.ID, 'form_fee')


    _seatLevel = (By.ID, 'form_seatLevel')
    _startOffCityName = (By.XPATH, '//*[@id="form_startOffCityName"]/div[2]/div/div[1]/input')
    _arriveCityName = (By.XPATH, '//*[@id="form_arriveCityName"]/div/div/div[1]/input')

    # 提交
    _invoiceSubmitButton = (By.XPATH, '//*[@id="form"]//div/button[2]')

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def input_billingCode(self, text):
        self.send_text(text, *self._billingCode)

    def click_myInvoiceQueryButton(self):
        self.click(*self._myInvoiceQueryButton)

    def open_manualInvoiceEntry(self):
        self.click(*self._manualInvoiceEntry)

    def click_invoiceType(self):
        self.click(*self._invoiceType)

    def open_addInvoiceWindow(self, type):
        for i in range(17):
            text = self.get_elementText(*(By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[{}]/span'.format(i+1)))
            if text == type:
                self.moveToclick(*(By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[{}]'.format(i+1)))
                break

    def input_invoiceNo(self, text):
        self.send_text(text, *self._invoiceNo)

    def input_invoiceCode(self, text):
        self.send_text(text, *self._invoiceCode)

    def selectInvoiceDate(self):
        self.click(*self._invoiceDate)
        sleep(1)
        self.click(*(By.XPATH, '/html/body/div[4]/div[1]/div/div[2]/table[1]/tbody/tr[5]/td[4]/div/span'))

    def input_feeTotal(self, text):
        self.click(*self._feeTotal)
        element = self.find_element(*self._feeTotal)
        ActionChains(self.driver).send_keys_to_element(element, Keys.BACKSPACE).perform()
        ActionChains(self.driver).send_keys_to_element(element, text).perform()

    def input_tax(self, text):
        self.click(*self._tax)
        element = self.find_element(*self._tax)
        ActionChains(self.driver).send_keys_to_element(element, Keys.BACKSPACE).perform()
        ActionChains(self.driver).send_keys_to_element(element, text).perform()

    def input_checkCode(self, text):
        self.send_text(text, *self._checkCode)

    def click_invoiceSubmitButton(self):
        self.click(*self._invoiceSubmitButton)

    @property
    def invoiceQueryResult(self):
        return self.elementExistIsOrNot(*self._invoiceQueryResult)

    def gotoInvoiceQueryPage(self):
        self.driver.get(config.getUrlDict()['url']['invoiceIpoolHost'])
