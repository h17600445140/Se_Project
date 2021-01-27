# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By

from PageClass.cmsIndexPageClass.cmsIndexPage import CmsIndexPage

from Util import logger



# 合同复核
class ContractExaminePage(CmsIndexPage):

    def __init__(self, driver):
        CmsIndexPage.__init__(self, driver)


    # 我已复核
    _contractReviewedTab = (By.ID, 'tab-Checked')
    def click_contractReviewedTab(self):
        self.click(*self._contractReviewedTab)


    # 查询结果 - 合同编码
    _contractCodeSelectResult = (By.XPATH, '//*[@id="app"]/section/main/div[2]/div/div[2]/div/div[2]/div/div[3]/table/tbody/tr[1]/td[3]/div/button/span')
    def getResultContractCode(self):
        logger.info('合同编号查询结果为 : {}'.format(self.get_elementText(*self._contractCodeSelectResult)))
        return self.get_elementText(*self._contractCodeSelectResult)


    # 查询结果 - 合同状态
    _contractStatusSelectResult= (By.XPATH, '//*[@id="app"]/section/main/div[2]/div/div[2]/div/div[2]/div/div[3]/table/tbody/tr[1]/td[12]/div')
    def getResultContractStatus(self):
        logger.info('合同状态查询结果为 : {}'.format(self.get_elementText(*self._contractStatusSelectResult)))
        return self.get_elementText(*self._contractStatusSelectResult)


    # 同意按钮
    _agreeButton = (By.XPATH, '//*[@id="app"]/section/main/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/table/tbody/tr/td[13]/div/div/button[1]/span')
    def click_agreeButton(self):
        self.click(*self._agreeButton)
        logger.info('点击同意按钮')


    # 确定按钮
    def click_confirmButoon(self):
        sleep(0.5)
        self.click_button('确定')
        logger.info('点击确定按钮')
