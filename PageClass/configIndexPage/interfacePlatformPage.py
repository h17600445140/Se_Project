# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from PageClass.basePage import BasePage



class TimerManage(BasePage):

    _selectTimerName = (By.ID, 'form_remark')
    _selectButton = (By.XPATH, '//*[@id="form"]/div[3]/div/button[2]')

    _sharingCenterTimer = (By.ID, 'tab-zfs-fsc')

    _runTimer = (By.XPATH, '//*[@id="app"]/section/section/section/main/div/div/div[3]/div[2]/div[14]/div/div/div[4]/div[2]')


    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def input_selectTimerName(self, text):
        self.send_text(text, *self._selectTimerName)

    def click_selectButton(self):
        self.click(*self._selectButton)

    def click_sharingCenterTimer(self):
        self.click(*self._sharingCenterTimer)

    def click_runTimer(self):
        self.click(*self._runTimer)