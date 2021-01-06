# -*- coding:utf-8 -*-
from Util.util import getPicturePath


class BasePage(object):
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

    def get_title(self):
        return self.driver.title

    def screenshot(self, code, timeNow):
        self.driver.get_screenshot_as_file(getPicturePath(code,timeNow))