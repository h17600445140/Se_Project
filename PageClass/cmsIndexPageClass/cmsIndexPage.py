# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageClass.basePage import BasePage
from Util import logger



# 合同结算系统
class CmsIndexPage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)


    # 进入合同结算系统各个页面
    def getIntoPage(self, pageType):
        for i in range(len(self.find_elements(*(By.CLASS_NAME, 'action-name')))):
            if self.find_elements(*(By.CLASS_NAME, 'action-name'))[i].text == pageType:
                self.find_elements(*(By.CLASS_NAME, 'action-name'))[i].click()
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
        self.find_elements(*self._more)[1].click()
        self.switchWindow()
        logger.info('点击更多按钮')

    # ---------- 首页 ----------

    # 数据校验行 - 合同编码
    _contractCodeCheck =  (By.XPATH, '//*[@id="app"]/section/main/div/div/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div[3]/table/tbody/tr[1]/td[3]/div/button/span')
    def checkContractCode(self, code):
        contractCode = self.find_element(*self._contractCodeCheck).text
        logger.info('查找到的合同编码为：{}'.format(contractCode))
        if code == contractCode:
            return True
        else:
            return False

    # 数据校验行 - 合同状态
    _contractStatusCheck = (By.XPATH, '//*[@id="app"]/section/main/div/div/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div[3]/table/tbody/tr[1]/td[12]/div')
    def checkContractStatus(self, status):
        contractStatus = self.get_elementText(*self._contractStatusCheck)
        logger.info('查找到的合同状态为：{}'.format(contractStatus))
        if status == contractStatus:
            return True
        else:
            return False

    # -------------------------


    # ---------- 更多界面 ----------

    # 查询结果 - 合同编码
    _contractCodeSelectResultMore = (By.XPATH, '//*[@id="app"]/section/main/div[2]/div/div/div[3]/div/div[3]/table/tbody/tr/td[3]/div/button/span')
    def getResultContractCodeMorePage(self):
        logger.info('合同编号查询结果为 : {}'.format(self.get_elementText(*self._contractCodeSelectResultMore)))
        return self.get_elementText(*self._contractCodeSelectResultMore)


    # 查询结果 - 合同状态
    _contractStatusSelectResultMore= (By.XPATH, '//*[@id="app"]/section/main/div[2]/div/div/div[3]/div/div[3]/table/tbody/tr/td[17]/div')
    def getResultContractStatusMorePage(self):
        logger.info('合同状态查询结果为 : {}'.format(self.get_elementText(*self._contractStatusSelectResultMore)))
        return self.get_elementText(*self._contractStatusSelectResultMore)

    # ----------------------------


    # ---------- 通用 ----------

    # 首页
    _homePage = (By.XPATH, '//*[@id="app"]/section/main/div[1]/span[1]/span[1]')
    def backToHomePage(self):
        self.click(*self._homePage)
        logger.info('回到首页')


    # 合同名称
    _contractNameQuery = (By.ID, 'undefined_contractName')
    def input_contractNameQuery(self, text):
        self.send_text(text, *self._contractNameQuery)
        logger.info('输入的合同名称为 : {}'.format(text))


    # 合同编码
    _contractCodeQuery = (By.ID, 'undefined_contractCode')
    def input_contractCodeQuery(self, text):
        self.send_text(text, *self._contractCodeQuery)
        logger.info('输入的合同编码为 : {}'.format(text))


    # 合同类型
    _contractTypeQuery = (By.ID, 'undefined_type')
    def input_contractTypeQuery(self, text):
        self.click(*self._contractTypeQuery)
        self.select_item(text)
        logger.info('选择的合同类型为 : {}'.format(text))


    # 申请人
    _contractUserQuery = (By.ID, 'undefined_draftUserId')

    # 所属核算主体
    _contractOgnQuery = (By.ID, 'undefined_ognId')


    # 查询
    def click_selectButton(self):
        self.click_button('查询')
        logger.info('点击查询按钮')





