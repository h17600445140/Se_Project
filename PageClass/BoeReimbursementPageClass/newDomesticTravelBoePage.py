# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By

from PageClass.common.boeCommon import BoeCommon
from PageClass.easIndexPageClass.easIndexPage import EasIndexPage




# 差旅报账单实例
class NewDomesticTravelBoePage(EasIndexPage,BoeCommon):

    def __init__(self, driver):
        EasIndexPage.__init__(self, driver)

    def click_modifySubsidyButton(self):
        for i in range(len(self.find_element(*(By.ID, 'cost')).find_elements(*(By.TAG_NAME, 'button')))):
            if self.find_element(*(By.ID, 'cost')).find_elements(*(By.TAG_NAME, 'button'))[i].text == '修改补贴':
                self.find_element(*(By.ID, 'cost')).find_elements(*(By.TAG_NAME, 'button'))[i].click()





