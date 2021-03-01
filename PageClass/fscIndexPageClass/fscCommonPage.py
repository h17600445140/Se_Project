# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageClass.basePage import BasePage
from Util import logger, config



class FscCommonPage(BasePage):



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

    _taskHandle = (By.XPATH, '//*[@id="app"]/section/section/header/ul/li[1]/div/span')
    def click_taskHandle(self):
        self.moveToclick(*self._taskHandle)
        logger.info('点击任务处理')

    _auditList = (By.XPATH, '/html/body/div[2]/ul/li[1]/span')
    def click_auditList(self):
        sleep(1)
        self.moveToclick(*self._auditList)
        logger.info('点击我的工作台')
        self.refresh()
    def gotoAuditList(self):
        sleep(1)
        self.driver.get(config.getUrlDict()['url']['fscAuditList'])

    _auditAdjustDirector = (By.XPATH, '/html/body/div[2]/ul/li[2]/span')
    def click_auditAdjustDirector(self):
        sleep(1)
        self.moveToclick(*self._auditAdjustDirector)
        logger.info('点击任务调整（主任）')
        self.refresh()
    def gotoAuditAdjustDirectorPage(self):
        sleep(1)
        self.driver.get(config.getUrlDict()['url']['fscAuditAdjustDirector'])

    _sharingItem = (By.CLASS_NAME, 'el-menu-item')
    def click_item(self, itemName):
        itemList = self.find_elements(*self._sharingItem)
        for i in range(len(itemList)):
            if itemList[i].get_attribute('title') == itemName:
                itemList[i].click()
        self.refresh()

    def click_auditAdjustGroup(self):
        self.click(*self._auditAdjustGroup)

    def click_missionAudit(self):
        self.click(*self._missionAudit)


    def gotoBillExchangePage(self):
        """
        describe：
            进入支付中心票据台账
        :param : No param
        :return: None
        """
        self.driver.get(config.getUrlDict()['url']['fscBillExchange'])