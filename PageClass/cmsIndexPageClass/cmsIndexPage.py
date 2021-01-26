# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from PageClass.basePage import BasePage
from Util import logger



# 合同结算系统
class CmsIndexPage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)


    # 进入合同结算系统各个页面
    def getIntoPage(self, pageType):
        for i in range(len(self.find_elements(*(By.CLASS_NAME, 'action-card')))):
            if self.find_elements(*(By.CLASS_NAME, 'action-card'))[i].text == pageType:
                self.find_elements(*(By.CLASS_NAME, 'action-card'))[i].click()
                logger.info('进入页面 -> {}'.format(pageType))
                self.switchWindow()
                break


    # 我的合同
    _myContract = (By.ID, 'tab-auths')
    def click_myContract(self):
        self.click(*self._myContract)
        logger.info('点击我的合同Tab')


    # 合同草稿
    _contractDraft = (By.ID, 'tab-draft')
    def click_contractDraft(self):
        self.click(*self._contractDraft)
        logger.info('点击合同草稿Tab')


    # 合同类型
    def clickContractType(self, contractType):
        for i in range(len(self.find_elements(*(By.CLASS_NAME, 'el-menu-item')))):
            if self.find_elements(*(By.CLASS_NAME, 'el-menu-item'))[i].text == contractType:
                self.find_elements(*(By.CLASS_NAME, 'el-menu-item'))[i].click()
                logger.info('点击合同类型 -> {}'.format(contractType))
                break


    # 更多
    _more = (By.CLASS_NAME, 'more')
    def click_more(self):
        self.click(*self._more)

