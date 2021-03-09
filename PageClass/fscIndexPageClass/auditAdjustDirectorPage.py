# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageClass.basePage import BasePage
from PageClass.fscIndexPageClass.fscCommonPage import FscCommonPage
from Util import logger



class AuditAdjustDirectorPage(FscCommonPage):


    _selectFirstGroup = (By.XPATH, '/html/body/div[5]/div[1]/div[1]/ul/li')
    _selectFirstGroup1 = (By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li')


    _selectFirstOperatorUser = (By.XPATH, '/html/body/div[5]/div[1]/div[1]/ul/li')
    _selectFirstOperatorUser1 = (By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li')


    def __init__(self,driver):
        FscCommonPage.__init__(self,driver)

    # 单据编号
    _selectBoeNum = (By.ID, 'undefined_boeNo')
    def input_selectBoeNum(self, text):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located( self._selectBoeNum ))
        self.send_text(text, *self._selectBoeNum)
        logger.info('输入查询的任务单据编号为：{}'.format(text))

    # 查询
    def click_selectButton(self):
        self.click_button('查询')
        logger.info("点击查询按钮")

    # 查询结果
    _selectResult = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div[3]/div/div[4]/div[2]/table/tbody/tr/td[1]/div/label/span/span')
    def click_selectResult(self):
        try:
            sleep(1)
            self.click(*self._selectResult)
            logger.info("点击查询结果")
        except:
            logger.error("没有找到查询结果，--- try again ---")
            sleep(1)
            self.click(*self._selectResult)

    def getSelectResult(self):
        return self._selectResult

    # 分配到组
    _distributeToGroup = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div[2]/button[2]/span')
    _selectGroup = (By.ID, 'form_fGroupId')
    _selectGroupSubmit = (By.XPATH, '//*[@id="form"]/div[3]/div/button[2]')
    def choiceGroup(self, groupType):
        self.click(*self._distributeToGroup)
        logger.info("点击分配到组")
        self.click(*self._selectGroup)
        sleep(0.5)
        self.select_item(groupType)
        logger.info("选择组：{}".format(groupType))
        self.click(*self._selectGroupSubmit)
        logger.info("点击提交按钮")

    # 分配人员
    _distributeToStaff = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div[2]/button[3]/span')
    _selectOperatorUser = (By.ID, 'form_operatorUserId')
    _selectOperatorUserSubmit = (By.XPATH, '//*[@id="form"]/div[4]/div/button[2]')
    def choiceOperatorUser(self, userType):
        self.click(*self._distributeToStaff)
        logger.info("点击分配人员")
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located( self._selectOperatorUser ))
        self.click(*self._selectOperatorUser)
        self.select_item(userType)
        logger.info("选择组：{}".format(userType))
        self.click(*self._selectOperatorUserSubmit)
        logger.info("点击提交按钮")


    # 任务收回
    _taskTakeToBack = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div[2]/button[4]/span')
    def click_taskTakeToBack(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located( self._taskTakeToBack ))
        self.click(*self._taskTakeToBack)
        logger.info("点击任务收回")


