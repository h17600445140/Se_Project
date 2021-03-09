# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Util import config, logger
from PageClass.configIndexPage.interfacePlatformPage import TimerManage



class HandleTimer():

    def __init__(self, timerType, timerName, driver):
        self._timerType = timerType
        self._timerName = timerName
        self.driver = driver
        logger.info('准备开始运行定时器，运行的目标定时器为：{}'.format(timerName))
        self.driver.get(config.getUrlDict()['url']['timerHost'])
        self._timerManage = TimerManage(self.driver)

    def runTimer(self):
        if self._timerType == '共享中心':
            sleep(1)
            self._timerManage.input_selectTimerName(self._timerName)
            sleep(1)
            self._timerManage.click_selectButton()
            try:
                sleep(1)
                self._timerManage.click_sharingCenterTimer()
            except:
                logger.warning('重试点击共享中心定时器Tab页面')
                sleep(1)
                self._timerManage.click_sharingCenterTimer()
            try:
                sleep(1)
                self._timerManage.click_runTimer()
            except:
                sleep(1)
                self._timerManage.click_runTimer()
            sleep(1)
            self._timerManage.back()



