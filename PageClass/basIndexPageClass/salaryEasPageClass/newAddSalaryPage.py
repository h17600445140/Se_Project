# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageClass.basIndexPageClass.basIndexPage import BasIndexPage
from PageClass.common.boeCommon import BoeCommon
from Util import logger,DC


# 新增薪酬
class NewAddSalaryPage(BasIndexPage,BoeCommon):

    def __init__(self, driver):
        BasIndexPage.__init__(self, driver)


    # 获取 boeNum 号码
    _boeNum = (By.XPATH, '//*[@id="form"]/div[1]/div/div/label/span')
    def getBoeNum(self):
        self.switchWindow()
        boeNum = self.get_elementText(*self._boeNum)
        if boeNum == '':
            sleep(1)
            boeNum = self.get_elementText(*self._boeNum)
        logger.info("当前提单单据号为：{}".format(boeNum))
        return boeNum


    # 期间
    _salaryPeriod = (By.ID, 'form_salaryPeriod')
    def selectSalaryPeriod(self, date):
        self.click(*self._salaryPeriod)
        sleep(1)

        year, month = date.split('-')[0], date.split('-')[1]

        year = str(int(year))
        month = str(int(month))

        # 操作年份
        dateHeaderPanel = self.find_element(*(By.CLASS_NAME, 'el-date-picker__header'))
        selected = dateHeaderPanel.find_elements(*(By.TAG_NAME, 'span'))[0].text
        selectedYear = selected.split(' ')[0]
        if year > selectedYear:
            num = int(year) - int(selectedYear)
            for i in range(num):
                dateHeaderPanel.find_elements(*(By.TAG_NAME, 'button'))[2].click()
        elif year < selectedYear:
            num = int(selectedYear) - int(year)
            for i in range(num):
                dateHeaderPanel.find_elements(*(By.TAG_NAME, 'button'))[0].click()
        elif year == selectedYear:
            pass

        # 操作月份
        dateContentPanel = self.find_element(*(By.CLASS_NAME, 'el-picker-panel__content'))
        monthTable = dateContentPanel.find_element(*(By.CLASS_NAME, 'el-month-table'))
        for i in range(len(monthTable.find_elements(*(By.TAG_NAME, 'a')))):
            if monthTable.find_elements(*(By.TAG_NAME, 'a'))[i].text == DC.dateConvert(month):
                monthTable.find_elements(*(By.TAG_NAME, 'a'))[i].click()


    # 业务类型
    _salaryOperationType = (By.ID, 'form_operationTypeId')
    def selectSalaryOperationType(self, text):
        self.click(*self._salaryOperationType)
        self.select_item(text)
        logger.info('选择的薪酬业务类型为 : {}'.format(text))


    # 备注
    _salaryRemark = (By.ID, 'form_remark')
    def input_salaryRemark(self, text):
        self.send_text(text, *self._salaryRemark)
        logger.info('输入的备注为 : {}'.format(text))


    # 保存
    _salarySaveButton = (By.XPATH, '//*[@id="form"]/div[7]/div/button')
    def click_salarySaveButton(self):
        self.click(*self._salarySaveButton)
        logger.info('点击保存按钮')


    # 新增
    _salaryAddButton = (By.XPATH, '//*[@id="app"]/section/main/div/div/div[2]/div/div[2]/div[2]/div[1]/button[1]')
    def click_salaryAddButton(self):
        try:
            self.click(*self._salaryAddButton)
        except:
            sleep(1)
            self.click(*self._salaryAddButton)
        logger.info('点击新增按钮')


    # 责任部门
    _salaryDept = (By.ID, 'form_deptId')
    def click_salaryDept(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(
            self._salaryDept))
        self.click(*self._salaryDept)
    def selectSalaryDept(self, deptCode, deptName=''):
        self.click_salaryDept()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(
            (By.ID, 'undefined_CODE')))
        self.send_text(deptCode, *(By.ID, 'undefined_CODE'))
        self.send_text(deptName, *(By.ID, 'undefined_NAME'))
        self.click(*(By.XPATH, '/html/body//form/div[3]/div/button[1]'))
        sleep(1)
        try:
            self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[
                len(self.find_elements(*(By.CLASS_NAME, 'el-table__row'))) - 1].click()
        except:
            logger.warning('警告,第一次没找到,重新查找点击')
            self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[
                len(self.find_elements(*(By.CLASS_NAME, 'el-table__row'))) - 1].click()
        logger.info('选择的责任部门编码为 : {}'.format(deptCode))
        logger.info('选择的责任部门名称为 : {}'.format(deptName))
        self.click(*(By.XPATH, '/html/body//div//span/button[2]'))


    # 应发
    def input_JiTiYingFa(self, text):
        self.input_amount(text, *(By.ID, 'form_f90592c3232eca0477c7b1b2b7ae5a88'))
        logger.info('输入的计提实发为：{}'.format(text))
    # 扣款
    def input_JiTiKouKuan(self, text):
        self.input_amount(text, *(By.ID, 'form_f90592c32335259001feb1b2b7ae5a8b'))
        logger.info('输入的计提应发为：{}'.format(text))
    # 实发
    def input_JiTiShiFa(self, text):
        self.input_amount(text, *(By.ID, 'form_f90592c32339248de152b1b2b7ae5a8e'))
        logger.info('输入的计提扣款为：{}'.format(text))

    # 提交
    def clickSalarySubmitButton(self):
        self.clickTargetButton('提交')
        sleep(1)


