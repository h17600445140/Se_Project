# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
        content = self.find_elements(*self._toastBox)[len(self.find_elements(*self._toastBox))-1].text
        return content

    _boxMessage = (By.CLASS_NAME, 'el-message-box__message')
    def getBoxMessage(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self._boxMessage))
        content = self.find_element(*self._boxMessage).text
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

    # 执行JS代码
    def executeScript(self, js):
        # 'window.scrollTo(0,document.body.scrollHeight)'
        self.driver.execute_script(js)

    # 操作切换窗口
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


    # 关闭当前窗口and切换回原来的窗口
    def closeCurrentWindows(self):
        self.driver.close()
        self.switchWindow()


    # ------ 操作通用控件 ------

    def click_button(self, buttonName) -> None:
        """
        说明：
            通过按钮名字点击按钮（全页面）
        :param buttonName:    按钮名字
        :return: None
        """
        for i in range(len(self.find_elements(*(By.TAG_NAME, 'button')))):
            if self.find_elements(*(By.TAG_NAME, 'button'))[i].text == buttonName:
                self.find_elements(*(By.TAG_NAME, 'button'))[i].click()
                logger.info('点击按钮：{}'.format(buttonName))
                break
            if i == (len(self.find_elements(*(By.TAG_NAME, 'button')))-1):
                raise Exception('Don\'t find this button -> {}'.format(buttonName))


    def select_item(self, type) -> None:
        """
        说明：
            浮动下拉框选择
        :param type:    选择内容
        :return: None
        """
        for i in range(len(self.find_elements(*(By.CLASS_NAME, 'el-select-dropdown__item')))):
            if self.find_elements(*(By.CLASS_NAME, 'el-select-dropdown__item'))[i].text == type:
                element = self.find_elements(*(By.CLASS_NAME, 'el-select-dropdown__item'))[i]
                ActionChains(self.driver).move_to_element(element).perform()
                element.click()
                break


    def input_amount(self, text, *loc) -> None:
        """
        说明：
            金额输入框输入
        :param text:    金额
        :param *loc:    定位元素
        :return: None
        """
        self.click(*loc)
        element = self.find_element(*loc)
        # ActionChains(self.driver).send_keys_to_element(element, Keys.BACKSPACE).perform()
        # ActionChains(self.driver).send_keys_to_element(element, text).perform()
        ActionChains(self.driver).send_keys_to_element(element, Keys.BACKSPACE).send_keys_to_element(element, text).perform()


    def select_option(self, option, *loc) -> None:
        """
        说明：
            系统编码下拉选择框选择
        :param option:  下拉框选择项
        :param *loc:    定位元素
        :return: None
        """
        self.click(*loc)
        sleep(1)
        for i in range(30):
            if i == 29:
                logger.error('没有找到对应配置项，请检查配置')
                raise Exception('没有找到对应配置项，请检查配置')
            if self.get_elementText(*(loc[0], (loc[1] + '.option.{}').format(i))) == option:
                self.moveToclick(*(loc[0], (loc[1] + '.option.{}').format(i)))
                break
        logger.info('选择的数据为：{}'.format(option))



    _calendar = (By.CLASS_NAME, 'calendar')
    def select_date(self, year, month, day) -> None:
        """
        说明：
            日期控件选择 年 月 日
        :param year:    年
        :param month:   月
        :param day:     日
        :return: None
        """

        year = str(int(year))
        month = str(int(month))
        day = str(int(day))

        sleep(1)
        # WebDriverWait(self.driver, 5).until(
        #     EC.visibility_of_element_located( (By.CLASS_NAME, 'el-date-picker__header') ))
        if len(self.find_elements(*(By.CLASS_NAME, 'el-picker-panel__body'))) > 1 :
            index = len(self.find_elements(*(By.CLASS_NAME, 'el-picker-panel__body'))) - 1
            dateHeaderPanel = self.find_elements(*(By.CLASS_NAME, 'el-date-picker__header'))[index]
            dateContentPanel = self.find_elements(*(By.CLASS_NAME, 'el-picker-panel__content'))[index]
        else:
            dateHeaderPanel = self.find_element(*(By.CLASS_NAME, 'el-date-picker__header'))
            dateContentPanel = self.find_element(*(By.CLASS_NAME, 'el-picker-panel__content'))

        # 操作年份
        selectedY = dateHeaderPanel.find_elements(*(By.TAG_NAME, 'span'))[0].text
        selectedYear = selectedY.split(' ')[0]
        if year > selectedYear:
            num = int(year) - int(selectedYear)
            for i in range(num):
                dateHeaderPanel.find_elements(*(By.TAG_NAME, 'button'))[2].click()
        elif year < selectedYear:
            num = int(selectedYear) - int(year)
            for i in range(num):
                dateHeaderPanel.find_elements(*(By.TAG_NAME, 'button'))[0].click()
        elif year == selectedYear:
            pass

        # 操作月份
        selectedM = dateHeaderPanel.find_elements(*(By.TAG_NAME, 'span'))[1].text
        selectedMonth = selectedM.split(' ')[0]
        if month > selectedMonth:
            num = int(month) - int(selectedMonth)
            for i in range(num):
                dateHeaderPanel.find_elements(*(By.TAG_NAME, 'button'))[3].click()
        elif month < selectedMonth:
            num = int(selectedMonth) - int(month)
            for i in range(num):
                dateHeaderPanel.find_elements(*(By.TAG_NAME, 'button'))[1].click()
        elif month == selectedMonth:
            pass

        # 操作日
        dayTable = dateContentPanel.find_element(*(By.CLASS_NAME, 'el-date-table'))
        startNum = 0
        for i in range(len(dayTable.find_elements(*(By.TAG_NAME, 'span')))):
            if dayTable.find_elements(*(By.TAG_NAME, 'span'))[i].text == '1':
                startNum = i
                break
        for i in range(startNum, len(dayTable.find_elements(*(By.TAG_NAME, 'span')))):
            if dayTable.find_elements(*(By.TAG_NAME, 'span'))[i].text == day:
                dayTable.find_elements(*(By.TAG_NAME, 'span'))[i].click()
                break

        if 'display: none' not in self.find_element(*(By.CLASS_NAME, 'el-picker-panel__footer')).get_attribute('style'):
            self.find_element(*(By.CLASS_NAME, 'el-picker-panel__footer')).find_elements(*(By.TAG_NAME, 'button'))[1].click()


    def clickTargetButton(self, buttonType) -> None:
        """
        说明：
            根据 buttonType 选择不同类型的按钮进行点击(页签栏)
        :param buttonType: 按钮名字
        :return: None
        """
        for i in range(len(self.find_elements(*(By.CLASS_NAME, 'el-button')))):
            if self.find_elements(*(By.CLASS_NAME, 'el-button'))[i].text == buttonType:
                self.find_elements(*(By.CLASS_NAME, 'el-button'))[i].click()
                logger.info('点击 {} 按钮'.format(buttonType))
                break

