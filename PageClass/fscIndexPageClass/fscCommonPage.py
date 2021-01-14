# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from PageClass.basePage import BasePage



class FscCommonPage(BasePage):

    _taskHandle = (By.XPATH, '//*[@id="app"]/section/section/header/ul/li[1]/div/span')
    _auditList = (By.XPATH, '/html/body/div[2]/ul/li[1]/span')
    _auditAdjustDirector = (By.XPATH, '/html/body/div[2]/ul/li[2]/span')
    _auditAdjustGroup = (By.XPATH, '/html/body/div[2]/ul/li[3]/span')
    _missionAudit = (By.XPATH, '/html/body/div[2]/ul/li[4]/span')
    _hasAuditList = (By.XPATH, '/html/body/div[2]/ul/li[5]/span')
    _receiptBoe = (By.XPATH, '/html/body/div[2]/ul/li[6]/span')

    _perationMonitoring = (By.XPATH, '//*[@id="app"]/section/section/header/ul/li[2]/div/span')
    _operationsMonitorV2 = (By.XPATH, '/html/body/div[3]/ul/li[1]/span')
    _groupMonitorV2 = (By.XPATH, '/html/body/div[3]/ul/li[2]/span')
    _auditReportList = (By.XPATH, '/html/body/div[3]/ul/li[3]/span')
    _memberManagement = (By.XPATH, '/html/body/div[3]/ul/li[4]/span')

    _voucherManagement = (By.XPATH, '//*[@id="app"]/section/section/header/ul/li[3]/div/span')
    _voucherEntryQuery = (By.XPATH, '/html/body/div[5]/ul/li[1]/span')
    _voucherTeamwork = (By.XPATH, '/html/body/div[5]/ul/li[2]/span')

    _paymentCenter = (By.XPATH, '//*[@id="app"]/section/section/header/ul/li[4]/div/span')
    _billExchange = (By.XPATH, '/html/body/div[4]/ul/li[1]/span')
    _paymentQuery = (By.XPATH, '/html/body/div[4]/ul/li[2]/span')
    _paymentConfirm = (By.XPATH, '/html/body/div[4]/ul/li[3]/span')
    _failPayment = (By.XPATH, '/html/body/div[4]/ul/li[4]/span')
    _cashierAudit = (By.XPATH, '/html/body/div[4]/ul/li[5]/span')
    _paymentQueryData = (By.XPATH, '/html/body/div[4]/ul/li[6]/span')

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def click_taskHandle(self):
        self.click(*self._taskHandle)

    def click_auditList(self):
        self.click(*self._auditList)

    def click_auditAdjustDirector(self):
        self.click(*self._auditAdjustDirector)

    def click_auditAdjustGroup(self):
        self.click(*self._auditAdjustGroup)

    def click_missionAudit(self):
        self.click(*self._missionAudit)