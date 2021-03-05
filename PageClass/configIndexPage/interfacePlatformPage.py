# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageClass.basePage import BasePage
from Util import logger


class TimerManage(BasePage):


    def __init__(self, driver):
        BasePage.__init__(self, driver)

    # 定时器名称
    _selectTimerName = (By.ID, 'form_remark')
    def input_selectTimerName(self, text):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located( self._selectTimerName ))
        self.send_text(text, *self._selectTimerName)
        logger.info("输入定时器名字为：{}".format(text))

    # 查询
    _selectButton = (By.XPATH, '//*[@id="form"]/div[3]/div/button[2]')
    def click_selectButton(self):
        self.click(*self._selectButton)
        logger.info("点击查询按钮")

    # 共享中心Tab
    _sharingCenterTimer = (By.ID, 'tab-zfs-fsc')
    def click_sharingCenterTimer(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located( self._sharingCenterTimer ))
        self.click(*self._sharingCenterTimer)
        logger.info("点击共享中心TimerTab")

    # 运行定时器
    _runTimer = (By.XPATH, '//*[@id="app"]//div/div/div[4]/div[2]')
    def click_runTimer(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located( self._runTimer ))
        self.click(*self._runTimer)
        logger.info("运行定时器")
        try:
            content = self.getToastBoxText()
        except:
            self.click(*self._runTimer)
            content = self.getToastBoxText()
        logger.info("定时器运行结果：{}".format(content))