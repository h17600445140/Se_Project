# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageClass.ledgerIndexPageClass.ledgerIndexPage import LedgerIndexPage
from Util import logger



class AcceptanceLedgerPage(LedgerIndexPage):

    def __init__(self, driver):
        LedgerIndexPage.__init__(self, driver)

    # ---------- 新增验收单操作 ----------

    # 验收单号
    _acceptanceNo = (By.ID, 'form_acceptanceNo')
    def input_acceptanceNo(self, text):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(
            self._acceptanceNo) )
        self.send_text(text, *self._acceptanceNo)
        logger.info('输入的验收单号为：{}'.format(text))


    # 订单号
    _acceptOrderNo = (By.ID, 'form_orderNo')
    def input_acceptOrderNo(self, text):
        self.send_text(text, *self._acceptOrderNo)
        logger.info('输入的订单号为：{}'.format(text))


    # 供应商
    _acceptVendorId = (By.ID, 'form_vendorId')
    def selectAcceptVendor(self, vendorName):
        self.click(*self._acceptVendorId)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, 'undefined_NAME')))
        self.send_text(vendorName, *(By.ID, 'undefined_NAME'))
        self.click(*(By.XPATH, '/html/body//form/div[2]/div/button[1]'))
        sleep(1)
        try:
            self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[len(self.find_elements(*(By.CLASS_NAME, 'el-table__row')))-1].click()
        except:
            logger.warning('警告,第一次没找到,重新查找点击')
            self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[len(self.find_elements(*(By.CLASS_NAME, 'el-table__row')))-1].click()
        logger.info('选择的供应商为 : {}'.format(vendorName))
        self.click(*(By.XPATH, '/html/body//div[3]/span/button[2]'))


    # 合同
    _acceptContractId = (By.ID, 'form_contractId')
    def selectAcceptContract(self, contractCode, contractName=''):
        self.click(*self._acceptContractId)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, 'undefined_contractCode')))
        self.send_text(contractCode, *(By.ID, 'undefined_contractCode'))
        self.send_text(contractName, *(By.ID, 'undefined_contractName'))
        self.click(*(By.XPATH, '/html/body//form/div[3]/div/button[1]'))
        sleep(1)
        try:
            self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[
                len(self.find_elements(*(By.CLASS_NAME, 'el-table__row'))) - 1].click()
        except:
            logger.warning('警告,第一次没找到,重新查找点击')
            self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[
                len(self.find_elements(*(By.CLASS_NAME, 'el-table__row'))) - 1].click()
        logger.info('选择的合同编码为 : {}'.format(contractCode))
        logger.info('选择的合同名称为 : {}'.format(contractName))
        self.click(*(By.XPATH, '/html/body//div[3]/span/button[2]'))


    # 项目
    _acceptProjectId = (By.ID, 'form_projectId')
    def selectAcceptProject(self, projectCode, projectName=''):
        self.click(*self._acceptProjectId)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, 'undefined_CODE')))
        self.send_text(projectCode, *(By.ID, 'undefined_CODE'))
        self.send_text(projectName, *(By.ID, 'undefined_NAME'))
        self.click(*(By.XPATH, '/html/body//form/div[3]/div/button[1]'))
        sleep(1)
        try:
            self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[
                len(self.find_elements(*(By.CLASS_NAME, 'el-table__row'))) - 1].click()
        except:
            logger.warning('警告,第一次没找到,重新查找点击')
            self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[
                len(self.find_elements(*(By.CLASS_NAME, 'el-table__row'))) - 1].click()
        logger.info('选择的项目编码为 : {}'.format(projectCode))
        logger.info('选择的项目名称为 : {}'.format(projectName))
        self.click(*(By.XPATH, '/html/body//div[3]/span/button[2]'))


    # 收方单位
    _acceptReceivingUnitId = (By.ID, 'form_receivingUnitId')
    def selectAcceptReceivingUnit(self, deptCode, deptName=''):
        self.click(*self._acceptReceivingUnitId)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, 'undefined_CODE')))
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
        logger.info('选择的部门编码为 : {}'.format(deptCode))
        logger.info('选择的部门名称为 : {}'.format(deptName))
        self.click(*(By.XPATH, '/html/body//div[3]/span/button[2]'))


    # 经办人
    _acceptAgentId = (By.ID, 'form_agentId')
    def selectAcceptAgent(self, agentAccount, agentName=''):
        self.click(*self._acceptAgentId)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, 'undefined_EMP_NO')))
        self.send_text(agentAccount, *(By.ID, 'undefined_EMP_NO'))
        self.send_text(agentName, *(By.ID, 'undefined_REAL_NAME'))
        self.click(*(By.XPATH, '/html/body//form/div[3]/div/button[1]'))
        sleep(1)
        try:
            self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[
                len(self.find_elements(*(By.CLASS_NAME, 'el-table__row'))) - 1].click()
        except:
            logger.warning('警告,第一次没找到,重新查找点击')
            self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[
                len(self.find_elements(*(By.CLASS_NAME, 'el-table__row'))) - 1].click()
        logger.info('选择的用户账号为 : {}'.format(agentAccount))
        logger.info('选择的用户名称为 : {}'.format(agentName))
        self.click(*(By.XPATH, '/html/body//div[3]/span/button[2]'))


    # 验收日期
    _acceptanceDate = (By.ID, 'form_acceptanceDate')
    def input_acceptanceDate(self, date):
        self.click(*self._acceptanceDate)
        year, month, day = date.split('-')[0], date.split('-')[1], date.split('-')[2]
        self.select_date(year, month, day)
        logger.info('选择的验收日期为：{}'.format(date))


    # 提交
    def click_acceptSubmitButton(self):
        self.click_button('提交')
        logger.info('点击提交按钮')

    # ----------------------------------

    # 验收单号
    _acceptanceNoQuery = (By.ID, 'undefined_acceptanceNo')
    def input_acceptanceNoQuery(self, text):
        self.clear(*self._acceptanceNoQuery)
        self.send_text(text, *self._acceptanceNoQuery)
        logger.info('输入查询的验收单号为：{}'.format(text))


    # 查询
    def click_acceptanceQueryButton(self):
        self.click_button('查询')


    # 结果
    _acceptanceNoResult = (By.XPATH, '//*[@id="pane-detail"]//div[3]/table/tbody/tr/td[3]/div/button')
    def get_acceptanceNoResult(self):
        return self.find_element(*self._acceptanceNoResult).text


    # 编辑
    _resultEditButton = (By.XPATH, '//*[@id="pane-detail"]//div[5]/div[2]/table/tbody/tr/td[17]/div/button')
    def click_acceptanceEditButoon(self):
        self.find_elements(*self._resultEditButton)[len(self.find_elements(*self._resultEditButton))-1].click()


    # ---------- acceptanceEditPage ----------
    # 新增
    _detailAddButton = (By.XPATH, '//*[@id="app"]/section/main/div/div/div[2]/div/div[2]/div[2]/div/div[1]/button[1]')
    def click_addDetailButton(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located( self._detailAddButton ))
        self.click(*self._detailAddButton)
        logger.info('点击新增按钮')


    # 名称
    _detailName =  (By.ID, 'form_name')
    def input_detailName(self, text):
        self.send_text(text, *self._detailName)
        logger.info('输入的名称为：{}'.format(text))


    # 规格
    _detailSpecification = (By.ID, 'form_specification')
    def input_detailSpecification(self, text):
        self.send_text(text, *self._detailSpecification)
        logger.info('输入的规格为：{}'.format(text))


    # 单位
    _detailUnit = (By.ID, 'form_unit')
    def input_detailUnit(self, text):
        self.send_text(text, *self._detailUnit)
        logger.info('输入的单位为：{}'.format(text))


    # 数量
    _detailNum = (By.ID, 'form_num')
    def input_detailNum(self, text):
        self.input_amount(text, *self._detailNum)
        logger.info('输入的数量为：{}'.format(text))


    # 不含税单价
    _detailPrice = (By.ID, 'form_price')
    def input_detailPrice(self, text):
        self.input_amount(text, *self._detailPrice)
        logger.info('输入的不含税单价为：{}'.format(text))


    # 不含税金额
    def input_detailTaxAmount(self, text):
        self.find_elements( *(By.ID, 'form_taxAmount') )[len(self.find_elements( *(By.ID, 'form_taxAmount') ))-2].click()
        element = self.find_elements( *(By.ID, 'form_taxAmount') )[len(self.find_elements( *(By.ID, 'form_taxAmount') ))-2]
        # ActionChains(self.driver).send_keys_to_element(element, Keys.BACKSPACE).perform()
        # ActionChains(self.driver).send_keys_to_element(element, text).perform()
        ActionChains(self.driver).send_keys_to_element(element, Keys.BACKSPACE).send_keys_to_element(element, text).perform()
        logger.info('输入的不含税金额为：{}'.format(text))


    # 税率
    _detailTaxRate = (By.ID, 'form_taxRate')
    def input_detailTaxRate(self, text):
        self.input_amount(text, *self._detailTaxRate)
        logger.info('输入的税率为：{}'.format(text))


    # 税额
    def input_detailTax(self, text):
        self.find_elements( *(By.ID, 'form_tax') )[len(self.find_elements( *(By.ID, 'form_tax') ))-2].click()
        element = self.find_elements( *(By.ID, 'form_tax') )[len(self.find_elements( *(By.ID, 'form_tax') ))-2]
        ActionChains(self.driver).send_keys_to_element(element, Keys.BACKSPACE).perform()
        ActionChains(self.driver).send_keys_to_element(element, text).perform()
        logger.info('输入的税额为：{}'.format(text))


    # 提交
    _detailSubmit = (By.XPATH, '//*[@id="form"]/div[10]/div/button[2]')
    def click_detailSubmit(self):
        self.click(*self._detailSubmit)
        logger.info('点击提交按钮')


    _detailCloseButton = (By.XPATH, '//*[@id="form"]/div[13]/div/button[1]')
    _detailSubmitButton = (By.XPATH, '//*[@id="form"]/div[13]/div/button[2]')



