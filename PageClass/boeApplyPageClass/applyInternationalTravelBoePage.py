# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By

from PageClass.common.boeCommon import BoeCommen
from PageClass.easIndexPageClass.easIndexPage import EasIndexPage



class ApplyInternationalTravelBoePage(EasIndexPage,BoeCommen):

    def __init__(self, driver):
        EasIndexPage.__init__(self, driver)

    # 支付金额
    _applyAmount = (By.ID, 'boeHeader.0.applyAmount')
    # 输入支付金额
    def input_applyAmount(self, amount):
        self.input_amount(amount, *self._applyAmount)

    # 开始日期
    _beginDateStr = (By.ID, 'boeHeaderChild.0.beginDateStr')
    def click_beginDateStr(self):
        self.click(*self._beginDateStr)
    # 输入开始日期
    def input_beginDateStr(self, date):
        self.click_beginDateStr()
        self.input_date(date)

    # 结束日期
    _endDateStr = (By.ID, 'boeHeaderChild.0.endDateStr')
    def click_endDateStr(self):
        self.click(*self._endDateStr)
    # 输入结束日期
    def input_endDateStr(self, date):
        self.click_endDateStr()
        self.input_date(date)

    # 出发城市
    _fromCity = (By.XPATH, '//*[@id="boeHeaderChild.0.fromSiteName"]/div/div/div[1]/input')
    # 输入出发城市
    def input_fromCity(self, text):
        self.click(*self._fromCity)
        self.send_text(text, *self._fromCity)

    # 到达城市
    _toCity = (By.XPATH, '//*[@id="boeHeaderChild.0.toSiteName"]/div/div/div[1]/input')
    # 输入到达城市
    def input_toCity(self, text):
        self.click(*self._toCity)
        self.send_text(text, *self._toCity)

    # 交通工具
    _transportation = (By.ID, 'boeHeaderChild.0.transportation')
    def select_transportation(self, option):
        self.select_option(option, *self._transportation)

    # 出差任务
    _travelTask = (By.ID, 'boeHeaderChild.0.travelTask')
    def select_travelTask(self, option):
        self.select_option(option, *self._travelTask)

    # 项目
    _projectId = (By.ID, 'boeHeaderChild.0.projectId')
    def input_projectId(self, projectName):
        self.click(*self._projectId)
        self.send_text(projectName, *self._projectId)