# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By

from PageClass.basePage import BasePage
from Util import logger


# 业务报账系统
class BasIndexPage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    # 选择业务报账类型
    def selectTabType(self, tabType):
        for i in range(len(self.find_elements(*(By.CLASS_NAME, 'el-badge')))):
            if self.find_elements(*(By.CLASS_NAME, 'el-badge'))[i].text == tabType:
                self.find_elements(*(By.CLASS_NAME, 'el-badge'))[i].click()
                logger.info('点击进入{}界面'.format(tabType))
                break

    # 我的单据
    _myBill = (By.ID, 'tab-myBill')
    def click_myBill(self):
        self.click(*self._myBill)
        logger.info('点击我的单据')

    # 我的草稿
    _myDraft = (By.ID, 'tab-myDraft')
    def click_myDraft(self):
        self.click(*self._myDraft)
        logger.info('点击我的草稿')

    # 待我处理
    _waitDeal = (By.ID, 'tab-waitDeal')
    def click_waitDeal(self):
        self.click(*self._waitDeal)
        logger.info('点击待我处理')

    # 我的付款
    _payFailed = (By.ID, 'tab-payFailed')
    def click_payFailed(self):
        self.click(*self._payFailed)
        logger.info('点击我的付款')

    # 更多
    _more = (By.CLASS_NAME, 'viewMore')
    def click_more(self):
        self.find_element(*self._more).click()
        logger.info('点击更多按钮')

    # 首页
    _homePage = (By.XPATH, '//*[@id="app"]/section/main/div/div[1]/span[1]/span[1]')
    def backToHomePage(self):
        self.click(*self._homePage)
        logger.info('回到首页')

    # 单据编号
    _boeNumQuery = (By.ID, 'undefined_boeNo')
    def input_boeNumQuery(self, text):
        self.send_text(text, *self._boeNumQuery)

    # 查询
    def click_queryButton(self):
        self.click_button('查询')
        logger.info('点击查询按钮')

    # 校验boeNum是否存在
    def checkBoeNumExistIsOrNot(self, boeNum):
        if self.find_element(*(By.XPATH, '//*[@id="app"]//table/tbody/tr/td[2]/div/button')).text == boeNum:
            logger.info('{} -> 单据存在'.format(boeNum))
            return True
        else:
            logger.info('{} -> 单据不存在'.format(boeNum))
            return False

    # 单据入口
    def boeRntry(self, boeType):
        for i in range(len(self.find_elements(*(By.CLASS_NAME, 'boe')))):
            if self.find_elements(*(By.CLASS_NAME, 'boe'))[i].text == boeType:
                self.find_elements(*(By.CLASS_NAME, 'boe'))[i].click()
                logger.info('进入单据 -> {}'.format(boeType))
                break