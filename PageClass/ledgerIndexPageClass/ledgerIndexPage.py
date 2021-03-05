# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By

from PageClass.basePage import BasePage
from Util import logger



class LedgerIndexPage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)


    _ledgerDetail = (By.ID, 'tab-detail')
    def click_ledgerDetail(self) -> None:
        """
        说明：
            点击台账明细Tab页签
        :return: None
        """
        self.click(*self._ledgerDetail)
        logger.info(' 点击台账明细Tab ')


    def getInLedger(self, typeName: str) -> None:
        """
        说明：
            根据 typeName 进入不同的台账页面
        :param typeName: 台账名字
        :return: None
        """
        self.driver.implicitly_wait(1)
        for i in range(len(self.find_elements( *(By.CLASS_NAME, 'card') ))):
            if self.find_elements(*(By.CLASS_NAME, 'card'))[i].find_element(*(By.CLASS_NAME, 'title')).text == typeName:
                self.find_elements(*(By.CLASS_NAME, 'card'))[i].find_element(*(By.CLASS_NAME, 'svg-icon')).click()
                logger.info('进入 {} 页面'.format(typeName))
                break
            if i == len(self.find_elements( *(By.CLASS_NAME, 'card') ))-1:
                logger.warning('Don\'t find Page')
                raise Exception('Don\'t find Page')






















