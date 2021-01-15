# -*- coding:utf-8 -*-


from selenium.webdriver.common.by import By

from PageClass.basePage import BasePage
from Util import logger



class EasMyInvoiceIndexPage(BasePage):

    _reimbursementState = (By.ID, 'undefined_reimbursementState')
    _billTypeInvoice = (By.ID, 'undefined_billTypeInvoice')
    _billingCode = (By.ID, 'undefined_billingCode')

    _myInvoiceQueryButton = (By.XPATH, '//*[@id="app"]/section/main/div[2]/div/div[1]/div[1]/form/div[10]/div/button[1]')

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

    '//*[@id="form_startOffCityName"]/div[2]/div/div[1]/input'
    '//*[@id="form_arriveCityName"]/div/div/div[1]/input'


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
            text = self.get_elementText(*(By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[{}]/span'.format(i)))
            if text == type:
                self.click(*(By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[{}]/span'.format(i)))
                break

