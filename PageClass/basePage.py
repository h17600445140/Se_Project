# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Util.util import getPicturePath
from Util import logger



class BasePage(object):


    _toastBoxRe = (By.XPATH, '/html/body/div[3]/p')

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

    def moveToclick(self, *loc):
        element = self.find_element(*loc)
        ActionChains(self.driver).move_to_element(element).perform()
        self.click(*loc)

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
        logger.info("进行截图操作")

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

    def elementIsSelect(self, *loc) -> bool:
        return self.driver.find_element(*loc).is_selected()

    def getElementAttribute(self, attribute, *loc):
        return self.driver.find_element(*loc).get_attribute(attribute)

    _toastBox = (By.CLASS_NAME, 'el-message__content')
    def getToastBoxText(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self._toastBox))
        content = self.find_element(*self._toastBox).text
        return content

    def getWindowHandles(self):
        return self.driver.window_handles

    def getCurrentWindowHandle(self):
        return self.driver.current_window_handle

    def switchToWin(self, window):
        self.driver.switch_to.window(window)

    def back(self):
        self.driver.back()
        logger.info("浏览器回退操作")

    # 操作切换黄口
    def switchWindow(self):
        num = 0
        while True:
            if len(self.getWindowHandles()) > 1:
                break
            if num > 1000:
                break
            num = num + 1
        logger.debug("所有窗口为：{}".format(self.getWindowHandles()))
        windowsList = self.getWindowHandles()
        index = 0
        for i in range(len(self.getWindowHandles())):
            if len(self.getWindowHandles()) == 1:
                break
            if self.getCurrentWindowHandle() != self.getWindowHandles()[i]:
                index = i
        self.switchToWin(windowsList[index])
        logger.debug("当前窗口为：{}".format(self.getCurrentWindowHandle()))

    # 点击按钮
    def click_button(self, buttonName):
        for i in range(len(self.find_elements(*(By.TAG_NAME, 'button')))):
            if self.find_elements(*(By.TAG_NAME, 'button'))[i].text == buttonName:
                self.find_elements(*(By.TAG_NAME, 'button'))[i].click()
                break

    # 浮动下拉框选择
    def select_item(self, type):
        for i in range(len(self.find_elements(*(By.CLASS_NAME, 'el-select-dropdown__item')))):
            if self.find_elements(*(By.CLASS_NAME, 'el-select-dropdown__item'))[i].text == type:
                element = self.find_elements(*(By.CLASS_NAME, 'el-select-dropdown__item'))[i]
                ActionChains(self.driver).move_to_element(element).perform()
                element.click()
