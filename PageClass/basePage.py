# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By

from Util.util import getPicturePath
from Util import logger



class BasePage(object):

    _toastBox = (By.XPATH, '/html/body/div[2]/p')

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def send_text(self, text, *loc):
        self.find_element(*loc).send_keys(text)

    def click(self, *loc):
        self.find_element(*loc).click()

    def clear(self, *loc):
        self.find_element(*loc).clear()

    def get_elementText(self, *loc):
        return self.find_element(*loc).text

    def get_title(self):
        return self.driver.title

    def refresh(self):
        self.driver.refresh()
        logger.info("页面刷新")

    def screenshot(self, code, timeNow):
        self.driver.get_screenshot_as_file(getPicturePath(code,timeNow))

    def elementExistIsOrNot(self, *loc) -> bool:
        try:
            self.driver.find_element(*loc)
        except:
            logger.info("元素不存在")
            return False
        else:
            logger.info("元素存在")
            return True

    def elementIsEnable(self, *loc) -> bool:
        return self.driver.find_element(*loc).is_enabled()

    def elementIsDisplay(self, *loc) -> bool:
        return self.driver.find_element(*loc).is_displayed()

    def getToastBoxText(self):
        return self.get_elementText(*self._toastBox)

    def getToastBox(self):
        return self._toastBox

