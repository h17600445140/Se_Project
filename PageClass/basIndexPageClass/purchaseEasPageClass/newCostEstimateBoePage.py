# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from PageClass.basIndexPageClass.basIndexPage import BasIndexPage
from PageClass.common.boeCommon import BoeCommon
from Util import logger



# 成本暂估（新）
class NewCostEstimateBoePage(BasIndexPage,BoeCommon):

    def __init__(self, driver):
        BasIndexPage.__init__(self, driver)


    # 关联验收单
    _relateAcceptanceLedgerButton = (By.XPATH, '//*[@id="cost"]/div/div/button')
    def click_relateAcceptanceLedgerButton(self):
        self.click(*self._relateAcceptanceLedgerButton)
        logger.info('点击关联验收单按钮')


    # 关联对应验收单
    def relateAcceptanceLedger(self, num):
        self.click_relateAcceptanceLedgerButton()
        for i in range(len(self.find_elements( *(By.CLASS_NAME, 'acceptanceNo') ))):
            content = self.find_elements( *(By.CLASS_NAME, 'acceptanceNo') )[i].text
            if content.split(' ')[1] == num:
                self.find_elements(*(By.CLASS_NAME, 'acceptance-card'))[i].click()
                break
        self.clickTargetButton('确定')