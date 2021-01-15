# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from PageClass.fscIndexPageClass.fscCommonPage import FscCommonPage



class MyAuditListPage(FscCommonPage):

    _boeNumQuery = (By.ID, 'undefined_boeNo')
    _boeNumQueryButton = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div[2]/div[1]/form/div[8]/div/button[1]')
    _boeNumQueryResult = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div[2]/div[3]/div/div[3]/table/tbody/tr/td[3]/div/button')

    def __init__(self,driver):
        FscCommonPage.__init__(self,driver)

    def input_boeNumQuery(self, text):
        self.send_text(text, *self._boeNumQuery)

    def click_boeNumQueryButton(self):
        self.click(*self._boeNumQueryButton)

    def getIntoBoe(self):
        self.click(*self._boeNumQueryResult)
