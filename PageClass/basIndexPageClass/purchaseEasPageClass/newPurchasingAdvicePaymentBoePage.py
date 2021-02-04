# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By

from PageClass.basIndexPageClass.basIndexPage import BasIndexPage
from PageClass.common.boeCommon import BoeCommon



# 采购付款
class NewPurchasingAdvicePaymentBoePage(BasIndexPage,BoeCommon):

    def __init__(self, driver):
        BasIndexPage.__init__(self, driver)


    def selectAccountReceivable(self, boeNum):
        self.find_element(By.CLASS_NAME, 'add').click()
        sleep(1)
        for i in range(len(self.find_elements(*(By.CLASS_NAME, 'el-table__row')))):
            try:
                if self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[i].find_element(By.CLASS_NAME, 'boeNo').text == boeNum:
                    self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[i].click()
                    break
            except:
                pass
            if i == len(self.find_elements(*(By.CLASS_NAME, 'el-table__row'))) - 1:
                raise Exception('没有找到：{}'.format(boeNum))
        self.click(*(By.XPATH, '/html/body//div//span/button[2]'))