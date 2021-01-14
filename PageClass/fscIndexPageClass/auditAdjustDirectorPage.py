# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from PageClass.basePage import BasePage
from PageClass.fscIndexPageClass.fscCommonPage import FscCommonPage



class AuditAdjustDirectorPage(FscCommonPage):

    _selectBoeNum = (By.ID, 'undefined_boeNo')
    _selectButton = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div[1]/form/div[11]/div/button[1]')
    _selectResult = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div[3]/div/div[4]/div[2]/table/tbody/tr/td[1]/div/label/span/span')

    _distributeToGroup = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div[2]/button[2]/span')
    _distributeToStaff = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div[2]/button[3]/span')
    _taskTakeToBack = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div[2]/button[4]/span')

    def __init__(self,driver):
        FscCommonPage.__init__(self,driver)

    def input_selectBoeNum(self, text):
        self.send_text(text, *self._selectBoeNum)

    def click_selectButton(self):
        self.click(*self._selectButton)

    def click_selectResult(self):
        self.click(*self._selectResult)

    def click_distributeToGroup(self):
        self.click(*self._distributeToGroup)

    def click_distributeToStaff(self):
        self.click(*self._distributeToStaff)

    def click_taskTakeToBack(self):
        self.click(*self._taskTakeToBack)
