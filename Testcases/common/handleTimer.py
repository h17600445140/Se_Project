# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Util import config
from PageClass.configIndexPage.interfacePlatformPage import TimerManage



class HandleTimer():

    def __init__(self, timerType, timerName, driver):
        self.timerType = timerType
        self.timerName = timerName
        self.driver = driver
        self.driver.get(config.getUrlDict()['url']['timerHost'])
        self.timerManage = TimerManage(self.driver)

    def runTimer(self):
        if self.timerType == '共享中心':
            sleep(1)
            self.timerManage.click_sharingCenterTimer()
            self.timerManage.input_selectTimerName(self.timerName)
            self.timerManage.click_selectButton()
            self.timerManage.click_runTimer()
            sleep(1)
            self.timerManage.back()


