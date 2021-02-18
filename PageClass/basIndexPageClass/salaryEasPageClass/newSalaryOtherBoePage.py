# -*- coding:utf-8 -*-
from time import sleep

from PageClass.basIndexPageClass.basIndexPage import BasIndexPage
from PageClass.common.boeCommon import BoeCommon
from selenium.webdriver.common.by import By
from Util import logger



# 工资报账单（新）
class NewSalaryOtherBoePage(BasIndexPage,BoeCommon):

    def __init__(self, driver):
        BasIndexPage.__init__(self, driver)


    # 关联薪资
    _salaryId = (By.ID, 'boeHeaderChild.0.salaryId')
    def select_salary(self):
        self.click(*self._salaryId)
        sleep(1)
        self.click(*(By.XPATH, '//*[@id="boeHeaderChild.0.salaryId.table"]/div/div/div[1]/div[3]/table/tbody/tr/td[1]'))
