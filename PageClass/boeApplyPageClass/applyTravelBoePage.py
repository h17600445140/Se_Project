# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageClass.common.boeCommon import BoeCommon
from PageClass.easIndexPageClass.easIndexPage import EasIndexPage
from Util import logger


class ApplyTravelBoePage(EasIndexPage,BoeCommon):

    def __init__(self, driver):
        EasIndexPage.__init__(self, driver)

    # 支付金额
    _applyAmount = (By.ID, 'boeHeader.0.applyAmount')
    # 输入支付金额
    def input_applyAmount(self, amount):
        self.input_amount(amount, *self._applyAmount)
        logger.info("输入的金额为：{}".format(amount))

    # 开始日期
    _beginDateStr = (By.ID, 'boeHeaderChild.0.beginDateStr')
    def click_beginDateStr(self):
        self.click(*self._beginDateStr)
    # 输入开始日期
    def input_beginDateStr(self, date):
        self.click_beginDateStr()
        year, month, day = date.split('-')[0],  date.split('-')[1],  date.split('-')[2]
        self.select_date(year, month, day)
        logger.info('选择的开始日期为：{}'.format(date))

    # 结束日期
    _endDateStr = (By.ID, 'boeHeaderChild.0.endDateStr')
    def click_endDateStr(self):
        self.click(*self._endDateStr)
    # 输入结束日期
    def input_endDateStr(self, date):
        self.click_endDateStr()
        year, month, day = date.split('-')[0], date.split('-')[1], date.split('-')[2]
        self.select_date(year, month, day)
        logger.info('选择的结束日期为：{}'.format(date))

    # 出差任务
    _travelTask = (By.ID, 'boeHeaderChild.0.travelTask')
    def select_travelTask(self, option):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self._travelTask))
        self.select_option(option, *self._travelTask)
        logger.info('选择的出差任务为：{}'.format(option))

    # 出发城市
    _fromCity = (By.XPATH, '//*[@id="boeHeaderChild.0.fromSiteName"]/div/div/div[1]/input')
    # 输入出发城市
    def input_fromCity(self, text):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self._fromCity))
        self.click(*self._fromCity)
        self.send_text(text, *self._fromCity)
        logger.info('选择的出发城市为：{}'.format(text))
        sleep(1)

    # 到达城市
    _toCity = (By.XPATH, '//*[@id="boeHeaderChild.0.toSiteName"]/div/div/div[1]/input')
    # 输入到达城市
    def input_toCity(self, text):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self._toCity))
        self.click(*self._toCity)
        self.send_text(text, *self._toCity)
        logger.info('选择的到达城市为：{}'.format(text))
        sleep(1)

    # 交通工具
    _transportation = (By.ID, 'boeHeaderChild.0.transportation')
    def select_transportation(self, option):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self._transportation))
        self.select_option(option, *self._transportation)
        logger.info('选择的交通工具为：{}'.format(option))