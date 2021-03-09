# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageClass.basIndexPageClass.basIndexPage import BasIndexPage
from PageClass.common.boeCommon import BoeCommon
from Util import logger



# 开票申请单
class BillingApplicationBoePage(BasIndexPage,BoeCommon):

    def __init__(self, driver):
        BasIndexPage.__init__(self, driver)

    # 购买方
    _buyer = (By.XPATH, '//*[@id="buyer"]/div/div')
    def click_buyer(self):
        self.click(*self._buyer)
    def selectBuyer(self, vendorName):
        self.click_buyer()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(
            (By.ID, 'itemVENDOR_NAME')))
        self.send_text(vendorName, *(By.ID, 'itemVENDOR_NAME'))
        self.click(*(By.XPATH, '/html/body//form/div[2]/div/button[1]'))
        sleep(1)
        try:
            self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[
                len(self.find_elements(*(By.CLASS_NAME, 'el-table__row'))) - 1].click()
        except:
            logger.warning('警告,第一次没找到,重新查找点击')
            self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[
                len(self.find_elements(*(By.CLASS_NAME, 'el-table__row'))) - 1].click()
        logger.info('选择的购买方为 : {}'.format(vendorName))
        self.click(*(By.XPATH, '/html/body//div//span/button[2]'))

    # 商品名称
    _goodsName = (By.ID, 'goodsInfo.0.tradeId')
    def click_goodsName(self):
        self.click(*self._goodsName)
    def selectGoods(self, goodsCode, goodsName=''):
        self.click_goodsName()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(
            (By.ID, 'itemtradeCode')))
        self.send_text(goodsCode, *(By.ID, 'itemtradeCode'))
        self.send_text(goodsName, *(By.ID, 'itemtradeName'))
        self.click(*(By.XPATH, '/html/body//form/div[3]/div/button[1]'))
        sleep(1)
        try:
            self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[
                len(self.find_elements(*(By.CLASS_NAME, 'el-table__row'))) - 1].click()
        except:
            logger.warning('警告,第一次没找到,重新查找点击')
            self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[
                len(self.find_elements(*(By.CLASS_NAME, 'el-table__row'))) - 1].click()
        logger.info('选择的商品编码为 : {}'.format(goodsCode))
        logger.info('选择的商品名称为 : {}'.format(goodsName))
        self.click(*(By.XPATH, '/html/body//div//span/button[2]'))

    # 商品数量
    _goodsAmount = (By.ID, 'goodsInfo.0.goodsAmount')
    def input_goodsAmount(self, text):
        self.input_amount(text, *self._goodsAmount)
        logger.info('输入的商品数量为：{}'.format(text))

    # 含税单价
    _goodPrice = (By.ID, 'goodsInfo.0.goodPrice')
    def input_goodPrice(self, text):
        self.input_amount(text, *self._goodPrice)
        logger.info('输入的含税单价为：{}'.format(text))

    # 含税金额
    _goodsExpenseAmount = (By.ID, 'goodsInfo.0.expenseAmount')
    def input_goodsExpenseAmount(self, text):
        self.input_amount(text, *self._goodsExpenseAmount)
        logger.info('输入的含税金额为：{}'.format(text))

    # 税率
    _goodsTaxRate = (By.ID, 'goodsInfo.0.taxRate')
    def input_goodsTaxRate(self, text):
        self.click(*self._goodsTaxRate)
        self.send_text(text, *self._goodsTaxRate)
        logger.info('输入的税率为：{}'.format(text))

    # 销售信息
    _salesInformation = (By.XPATH, '//*[@id="seller"]/div/div')
    def selectSaler(self, text):
        self.click(*self._salesInformation)
        sleep(3)
        for i in range(len(self.find_elements(*(By.CLASS_NAME, 'el-table__row')))):
            try:
                if self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[i].find_element(By.CLASS_NAME, 'name').text == text:
                    self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[i].click()
                    break
            except:
                pass
            if i == len(self.find_elements(*(By.CLASS_NAME, 'el-table__row'))) - 1:
                raise Exception('没有找到：{}'.format(text))
        self.click(*(By.XPATH, '/html/body//div//span/button[2]'))


