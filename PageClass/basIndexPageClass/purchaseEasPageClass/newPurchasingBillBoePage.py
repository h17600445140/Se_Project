# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from PageClass.basIndexPageClass.basIndexPage import BasIndexPage
from PageClass.common.boeCommon import BoeCommon



# 采购报账
class NewPurchasingBillBoePage(BasIndexPage,BoeCommon):

    def __init__(self, driver):
        BasIndexPage.__init__(self, driver)


    # 我要冲销
    _writeOff = (By.XPATH, '//*[@id="cost"]/div/div/button[1]')



    # 建立关联
    _makeRelated = (By.XPATH, '//*[@id="cost"]/div/div/button[2]')
    def click_makeRelated(self):
        self.click(*self._makeRelated)
    def relateAcceptancesheetAndInvoice(self, acceptancesheetNum, invoiceNum):

        self.find_elements(*(By.CLASS_NAME, 'filter-input'))[0].find_element(*(By.TAG_NAME, 'input')).send_keys(acceptancesheetNum)
        self.find_elements(*(By.CLASS_NAME, 'filter-input'))[1].find_element(*(By.TAG_NAME, 'input')).send_keys(invoiceNum)

        print( len( self.find_elements(*(By.CLASS_NAME, 'acceptance-card')) ) )
        print( len( self.find_elements(*(By.CLASS_NAME, 'bill-wrapper')) ) )
        print( len( self.find_elements(*(By.CLASS_NAME, 'doc-item')) ) )

        a = self.find_element(*(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div'))
        b = self.find_element(*(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div'))
        c = self.find_element(*(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[3]/div[2]/div[1]/div/div/div/div/div'))

        ActionChains(self.driver).drag_and_drop(a, c).perform()
        ActionChains(self.driver).drag_and_drop(b, c).perform()

        # ActionChains(self.driver).click_and_hold(a).pause(1).move_to_element(c).pause(1).release(a).perform()




