# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageClass.basIndexPageClass.basIndexPage import BasIndexPage
from PageClass.common.boeCommon import BoeCommon

from Util import logger



# 贴现托收申请单（新）
class NewDisaccountApplyBoePage(BasIndexPage,BoeCommon):

    def __init__(self, driver):
        BasIndexPage.__init__(self, driver)


    def associateBill(self, postalOrderCode):
        """
        describe：
                关联票据
        :param postalOrderCode: 汇票编码
        :return: None
        """
        self.clickTargetButton('关联票据')
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(
            (By.ID, 'itempostalOrderCode')))
        self.send_text(postalOrderCode, *(By.ID, 'itempostalOrderCode'))
        self.click(*(By.XPATH, '/html/body//form/div[8]/div/button[1]'))
        sleep(1)
        try:
            self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[
                len(self.find_elements(*(By.CLASS_NAME, 'el-table__row'))) - 1].click()
        except:
            logger.warning('警告,第一次没找到,重新查找点击')
            self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[
                len(self.find_elements(*(By.CLASS_NAME, 'el-table__row'))) - 1].click()
        logger.info('选择的汇票编码为 : {}'.format(postalOrderCode))
        self.click(*(By.XPATH, '/html/body//div//span/button[2]'))