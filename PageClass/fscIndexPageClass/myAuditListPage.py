# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageClass.fscIndexPageClass.fscCommonPage import FscCommonPage
from Util import logger



class MyAuditListPage(FscCommonPage):

    _boeNumQuery = (By.ID, 'undefined_boeNo')


    def __init__(self,driver):
        FscCommonPage.__init__(self,driver)

    def input_boeNumQuery(self, text):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self._boeNumQuery))
        self.send_text(text, *self._boeNumQuery)
        logger.info('输入的单据编号为：{}'.format(text))

    def click_boeNumQueryButton(self):
        self.click_button('查询')
        logger.info('点击查询按钮')

    _boeNumQueryResult = (
    By.XPATH, '//*[@id="app"]/section/section/main/div/div/div[2]/div[3]/div/div[3]/table/tbody/tr/td[3]/div/button')
    def getIntoBoe(self):
        self.click(*self._boeNumQueryResult)
        logger.info('进入对应单据进行审批操作')



