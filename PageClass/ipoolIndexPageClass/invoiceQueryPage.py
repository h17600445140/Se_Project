# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from PageClass.basePage import BasePage



class InvoiceQueryPage(BasePage):

    # 发票代码
    _billingNoQuery = (By.ID, 'undefined_billingNo')
    # 发票号码
    _billingCodeQuery = (By.ID, 'undefined_billingCode')
    # 查询
    _invoiceQueryButton = (By.XPATH, '//*[@id="app"]/section/section/section/main/div/div/div[1]/div[1]/form//button[1]')
    # 查询结果
    _invoiceQueryResult = (By.XPATH, '//*[@id="app"]/section/section/section/main/div/div/div[1]/div[3]/div/div[3]/table/tbody/tr[1]')

    # 发票查询
    _invoiceQueryTab = (By.XPATH, '//*[@id="app"]/section/section/aside/div/div[2]/div[1]/div/ul/li[1]/div/span')


    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def open_invoiceQueryTab(self):
        self.click(*self._invoiceQueryTab)

    def open_subInvoiceQueryTab(self, invoiceType):
        for i in range(1,11):
            text = self.get_elementText(*(By.XPATH, '//*[@id="app"]/section/section/aside/div/div[2]/div[1]/div/ul/li[1]/ul/li[{}]/span'.format(i)))
            if text == invoiceType:
                self.moveToclick(*(By.XPATH, '//*[@id="app"]/section/section/aside/div/div[2]/div[1]/div/ul/li[1]/ul/li[{}]'.format(i)))
                break

    def input_billingNoQuery(self, text):
        self.send_text(text, *self._billingNoQuery)

    def input_billingCodeQuery(self, text):
        self.send_text(text, *self._billingCodeQuery)

    def click_invoiceQueryButton(self):
        self.click(*self._invoiceQueryButton)

    def invoiceQueryResult(self):
        return self.elementExistIsOrNot(*self._invoiceQueryResult)


