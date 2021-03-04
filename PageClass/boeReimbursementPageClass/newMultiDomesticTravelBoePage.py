# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageClass.common.boeCommon import BoeCommon
from PageClass.easIndexPageClass.easIndexPage import EasIndexPage



# 多人差旅报账单实例
from Util import logger


class NewMultiDomesticTravelBoePage(EasIndexPage,BoeCommon):

    def __init__(self, driver):
        EasIndexPage.__init__(self, driver)

    # ---------- 头部附加区 ----------

    # 出行人员
    def add_travelers(self, keyWord):
        self.click_button('+')
        self.send_text(keyWord, *(By.ID, 'itemkeyword'))
        self.click_button('查询')
        try:
            self.click(*(By.XPATH, '/html/body//table/tbody/tr/td[1]/div/label/span'))
        except:
            sleep(2)
            self.click(*(By.XPATH, '/html/body//table/tbody/tr/td[1]/div/label/span'))
        self.click(*(By.XPATH, '/html/body//div[3]/span/button[2]'))
        logger.info('增加出行人员，出行人员的工号为：{}'.format(keyWord))

    # 项目
    _projectId = (By.ID, 'boeHeaderChild.0.projectId')
    def select_projectId(self, text):
        self.click(*self._projectId)
        self.send_text(text, *self._projectId)
        logger.info('选择的项目为：{}'.format(text))
        sleep(1)

    # ------------------------------

    # 清空卡片内容操作
    def clearPersonCard(self):
        self.find_elements(*(By.CLASS_NAME, 'person-card'))[0].click()
        invoiceLength = len(self.find_elements(*(By.CLASS_NAME, 'bill-wrapper')))
        for i in range(invoiceLength):
            self.find_elements(*(By.CLASS_NAME, 'bill-wrapper'))[invoiceLength-i-1].find_element(*(By.CLASS_NAME, 'bill-wrapper-operator')).click()
        print(len(self.find_elements(*(By.CLASS_NAME, 'el-dialog__headerbtn'))))
        self.find_elements(*(By.CLASS_NAME, 'el-dialog__headerbtn'))[1].click()


