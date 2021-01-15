# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By

from PageClass.basePage import BasePage



class BoeCommen(BasePage):

    _boeSaveButton = (By.ID, 'save')
    _boeSubmitButton = (By.ID, 'submit')


    _printCover = (By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div[2]/div/div[2]/button[1]')
    _viewBoe = (By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div[2]/div/div[2]/button[2]')
    _copyBoe = (By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div[2]/div/div[2]/button[3]')
    _continueBoe = (By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div[2]/div/div[2]/button[4]')
    _close = (By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div[2]/div/div[2]/button[5]')


    _accountMessage = (By.ID, 'tab-accounting')
    _approveButton = (By.XPATH, '//*[@id="pane-accounting"]/div/div[1]/div[1]/div/div/div[1]/div[2]/div[4]/button[1]')
    _approveButton1 = (By.XPATH, '//*[@id="pane-accounting"]/div/div[1]/div[1]/div/div/div[2]/div[2]/div[4]/button[1]')



    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def click_boeSubmitButton(self):
        self.click(*self._boeSubmitButton)

    def click_printCover(self):
        self.click(*self._printCover)

    def click_viewBoe(self):
        self.click(*self._viewBoe)

    def click_copyBoe(self):
        self.click(*self._copyBoe)

    def click_continueBoe(self):
        self.click(*self._continueBoe)

    def click_close(self):
        self.click(*self._close)

    def click_accountMessage(self):
        self.click(*self._accountMessage)

    def click_approveButton(self):
        try:
            self.click(*self._approveButton)
        except:
            self.click(*self._approveButton1)