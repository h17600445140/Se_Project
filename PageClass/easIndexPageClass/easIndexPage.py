# -*- coding:utf-8 -*-


from selenium.webdriver.common.by import By

from PageClass.basePage import BasePage
from Util import logger


class EasIndexPage(BasePage):

    _boeApply = (By.XPATH, '//*[@id="app"]/section/main/div/div/div[2]/div[3]/div[2]/div[1]/div/div')
    _boeReimburse = (By.XPATH, '//*[@id="app"]/section/main/div/div/div[2]/div[3]/div[2]/div[2]/div/div')
    _boeBorrow = (By.XPATH, '//*[@id="app"]/section/main/div/div/div[2]/div[3]/div[2]/div[3]/div/div')
    _menuMyInvoice = (By.XPATH, '//*[@id="app"]/section/main/div/div/div[2]/div[3]/div[2]/div[5]/div/div')

    _myWaitApprove = (By.ID, 'tab-waitApprovel')
    _myBoeList = (By.ID, 'tab-myBoeList')

    _moreButton = (By.XPATH, '//*[@id="app"]/section/main/div/div/div[2]/div[4]/div[2]')
    _boeNo = (By.ID, 'undefined_boeNo')
    _boeNoSelectButton = (By.XPATH, '//*[@id="app"]/section/main/div[2]/div/div/div[1]/form/div[8]/div/button[1]')
    _boeNoSelectResult = (By.XPATH, '//*[@id="app"]/section/main/div[2]/div/div/div[3]/div/div[3]/table/tbody/tr')
    _boeBusinessApprove = (By.XPATH, '//*[@id="app"]/section/main/div[2]/div/div/div[3]/div/div[5]/div[2]/table/tbody/tr/td[12]/div/button[1]')
    _boeBusinessRefuse = (By.XPATH, '//*[@id="app"]/section/main/div[2]/div/div/div[3]/div/div[5]/div[2]/table/tbody/tr/td[12]/div/button[2]')
    _boeBusinessTipCancel = (By.XPATH, '/html/body/div[2]/div/div[3]/button[1]')
    _boeBusinessTipConfirm = (By.XPATH, '/html/body/div[2]/div/div[3]/button[2]')


    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def open_boeApply(self):
        self.click(*self._boeApply)

    def open_boeReimburse(self):
        self.click(*self._boeReimburse)

    def open_boeBorrow(self):
        self.click(*self._boeBorrow)

    def open_menuMyInvoice(self):
        self.click(*self._menuMyInvoice)


    def click_myBoeList(self):
        self.click(*self._myBoeList)

    def click_myWaitApprove(self):
        self.click(*self._myWaitApprove)

    def click_moreButton(self):
        self.click(*self._moreButton)

    def input_boeNo(self, text):
        self.send_text(text, *self._boeNo)

    def getBoeNo(self):
        return self._boeNo

    def click_boeNoSelectButton(self):
        self.click(*self._boeNoSelectButton)

    def selectResultIsOrNot(self):
        try:
            self.find_element(self._boeNoSelectResult)
        except:
            logger.info("单据不存在")
            return False
        else:
            logger.info("单据存在")
            return True

    def click_boeBusinessApprove(self):
        self.click(*self._boeBusinessApprove)

    def click_boeBusinessTipConfirm(self):
        self.click(*self._boeBusinessTipConfirm)
