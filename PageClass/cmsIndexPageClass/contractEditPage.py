# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from PageClass.cmsIndexPageClass.cmsIndexPage import CmsIndexPage
from Util import logger



# 合同录入界面
class ContractEditPage(CmsIndexPage):

    def __init__(self, driver):
        CmsIndexPage.__init__(self, driver)

    # 提交
    _submitButton = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/button[1]')
    def click_submitButton(self):
        self.click(*self._submitButton)
        logger.info('点击提交按钮')

    # 确定
    def click_confirmButoon(self):
        sleep(1)
        self.click_button('确定')
        logger.info('点击确定按钮')
        self.switchWindow()

    # 申请人
    _draftUser = (By.ID, 'form_draftUserId')

    # 合同类型
    _contractType = (By.ID, 'form_contractType')
    def selectContractType(self, text):
        self.click(*self._contractType)
        self.select_item(text)
        logger.info('选择的合同类型为 : {}'.format(text))

    # 合同名称
    _contractName = (By.ID, 'form_contractName')
    def input_contractName(self, text):
        WebDriverWait(self.driver, 8).until(EC.visibility_of_element_located( self._contractName ))
        self.send_text(text, *self._contractName)
        logger.info('输入的合同名称为 : {}'.format(text))

    # 合同编号
    _contractCode = (By.ID, 'form_contractCode')
    def input_contractCode(self, text):
        self.send_text(text, *self._contractCode)
        logger.info('输入的合同编号为 : {}'.format(text))

    # 合同总金额
    _contractAmount = (By.ID, 'form_contractAmount')
    def input_contractAmount(self, text):
        self.input_amount(text, *self._contractAmount)
        logger.info('输入的合同金额为 : {}'.format(text))

    # 币种
    _currencyId = (By.ID, 'form_currencyId')
    def selectCurrency(self, currencyCode, currencyName = ''):
        self.click(*self._currencyId)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located( (By.ID, 'undefined_CURRENCY_CODE') ))
        self.send_text(currencyCode, *(By.ID, 'undefined_CURRENCY_CODE'))
        self.send_text(currencyName, *(By.ID, 'undefined_NAME'))
        self.click(*(By.XPATH, '/html/body//form/div[3]/div/button[1]'))
        try:
            targetAttribute = self.find_element(*(By.CLASS_NAME, 'el-table__row')).find_element(
            *(By.CLASS_NAME, 'el-checkbox')).get_attribute('class')

        except:
            sleep(1)
            targetAttribute = self.find_element(*(By.CLASS_NAME, 'el-table__row')).find_element(
            *(By.CLASS_NAME, 'el-checkbox')).get_attribute('class')

        if 'is-checked' not in targetAttribute:
            try:
                self.find_element(*(By.CLASS_NAME, 'el-table__row')).find_element(
                    *(By.CLASS_NAME, 'el-checkbox')).click()

            except:
                logger.warning('选中失败,重新点击选中')
                self.find_element(*(By.CLASS_NAME, 'el-table__row')).find_element(
                    *(By.CLASS_NAME, 'el-checkbox')).click()

            logger.info('选择币种编码 : {}'.format(currencyCode))
            logger.info('选择币种名称 : {}'.format(currencyName))
            self.click(*(By.XPATH, '/html/body//div[3]/span/button[2]'))
        else:
            logger.info('已经选择了币种编码 : {}'.format(currencyCode))
            logger.info('已经选择了币种名称 : {}'.format(currencyName))
            self.click(*(By.XPATH, '/html/body//div[3]/span/button[1]'))

    # 客商类型
    _vendorType = (By.ID, 'form_vendorType')
    def selectVendorType(self, text):
        self.click(*self._vendorType)
        self.select_item(text)
        logger.info('选择的客商类型为 : {}'.format(text))

    # 客商名称
    _vendorCode = (By.ID, 'form_vendorId')
    def selectVendorName(self, vendorCode, vendorName = ''):
        self.click(*self._vendorCode)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located( (By.ID, 'undefined_vendorCode') ))
        self.send_text(vendorCode, *(By.ID, 'undefined_vendorCode'))
        self.send_text(vendorName, *(By.ID, 'undefined_vendorName'))
        self.click(*(By.XPATH, '/html/body//form/div[3]/div/button[1]'))
        try:
            targetAttribute = self.find_element(*(By.CLASS_NAME, 'el-table__row')).find_element(
                *(By.CLASS_NAME, 'el-checkbox')).get_attribute('class')

        except:
            sleep(1)
            targetAttribute = self.find_element(*(By.CLASS_NAME, 'el-table__row')).find_element(
                *(By.CLASS_NAME, 'el-checkbox')).get_attribute('class')

        if 'is-checked' not in targetAttribute:
            try:
                self.find_element(*(By.CLASS_NAME, 'el-table__row')).find_element(
                    *(By.CLASS_NAME, 'el-checkbox')).click()

            except:
                logger.warning('选中失败,重新点击选中')
                self.find_element(*(By.CLASS_NAME, 'el-table__row')).find_element(
                    *(By.CLASS_NAME, 'el-checkbox')).click()

            logger.info('选择客商编码为 : {}'.format(vendorCode))
            logger.info('选择客商名称为 : {}'.format(vendorName))
            self.click(*(By.XPATH, '/html/body//div[3]/span/button[2]'))
        else:
            logger.info('已经选择了客商编码为 : {}'.format(vendorCode))
            logger.info('已经选择了客商名称为 : {}'.format(vendorName))
            self.click(*(By.XPATH, '/html/body//div[3]/span/button[1]'))

    # 签订日期
    _signDate = (By.ID, 'form_signDate')
    def input_signDate(self, date):
        self.click(*self._signDate)
        year, month, day = date.split('-')[0], date.split('-')[1], date.split('-')[2]
        self.select_date(year, month, day)
        logger.info('选择的签订日期为：{}'.format(date))

    # 合同日期开始时间
    _contractDataFrom = (By.XPATH, '//*[@id="form"]/div[10]/div/div/div[1]')
    def input_contractDataFrom(self, date):
        self.click(*self._contractDataFrom)
        year, month, day = date.split('-')[0], date.split('-')[1], date.split('-')[2]
        self.select_date(year, month, day)
        logger.info('选择的合同日期开始时间为：{}'.format(date))
    # 合同日期结束时间
    _contractDataTo = (By.XPATH, '//*[@id="form"]/div[10]/div/div/div[3]')
    def input_contractDataTo(self, date):
        self.click(*self._contractDataTo)
        year, month, day = date.split('-')[0], date.split('-')[1], date.split('-')[2]
        self.select_date(year, month, day)
        logger.info('选择的合同日期结束时间为：{}'.format(date))

    # 报账人
    _respUser = (By.ID, 'form_respUserId')
    def selectResUser(self, empNo, empName = ''):
        self.click(*self._respUser)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, 'undefined_EMP_NO')))
        self.send_text(empNo, *(By.ID, 'undefined_EMP_NO'))
        self.send_text(empName, *(By.ID, 'undefined_REAL_NAME'))
        self.click(*(By.XPATH, '/html/body//form/div[3]/div/button[1]'))
        sleep(1)
        try:
            self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[len(self.find_elements(*(By.CLASS_NAME, 'el-table__row')))-1].click()
        except:
            logger.warning('警告,第一次没找到,重新查找点击')
            self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[len(self.find_elements(*(By.CLASS_NAME, 'el-table__row')))-1].click()
        logger.info('选择的报账人工号为 : {}'.format(empNo))
        logger.info('选择的报账人名称为 : {}'.format(empName))
        self.click(*(By.XPATH, '/html/body//div[3]/span/button[2]'))

    # 责任部门
    _respDept = (By.ID, 'form_respDeptId')
    def selectDept(self, deptNo, deptName = ''):
        self.click(*self._respDept)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, 'undefined_CODE')))
        self.send_text(deptNo, *(By.ID, 'undefined_CODE'))
        self.send_text(deptName, *(By.ID, 'undefined_NAME'))
        self.click(*(By.XPATH, '/html/body//form/div[3]/div/button[1]'))
        sleep(1)
        try:
            self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[len(self.find_elements(*(By.CLASS_NAME, 'el-table__row')))-1].click()
        except:
            logger.warning('警告,第一次没找到,重新查找点击')
            self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[len(self.find_elements(*(By.CLASS_NAME, 'el-table__row')))-1].click()
        logger.info('选择的责任部门编码为 : {}'.format(deptNo))
        logger.info('选择的责任部门名称为 : {}'.format(deptName))
        self.click(*(By.XPATH, '/html/body//div[3]/span/button[2]'))

    # 合同范围
    _contractScope = (By.ID, 'form_contractScope')
    def selectContractScope(self, text):
        self.click(*self._contractScope)
        self.select_item(text)
        logger.info('选择的合同范围为 : {}'.format(text))

    # 是否框架合同
    _frameworkContract = (By.ID, 'form_frameworkContract')
    def selectFrameworkContract(self, text):
        self.click(*self._frameworkContract)
        self.select_item(text)
        logger.info('是否框架合同 : {}'.format(text))

    # 是否有影像
    _haveImage = (By.ID, 'form_haveImage')
    def selectHaveImage(self, text):
        self.click(*self._haveImage)
        try:
            self.select_item(text)
        except:
            self.select_item(text)
        logger.info('是否有影像 : {}'.format(text))


    ### --------------- 框架合同为否 --------------- ###
    # 新增按钮
    _addPaymentPlan = (By.XPATH, '//*[@id="form"]/div/div/div/div/button[1]')
    def click_addPaymentPlan(self):
        # self.click(*self._addPaymentPlan)
        self.find_elements(*self._addPaymentPlan)[len(self.find_elements(*self._addPaymentPlan))-1].click()
        element = self.find_elements(*self._addPaymentPlan)[len(self.find_elements(*self._addPaymentPlan))-1]
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        logger.info('点击新增收付款计划按钮')

    # 放款性质
    _paymentType = (By.ID, 'form_paymentType')
    def selectPaymentType(self, text):
        self.find_elements(*self._paymentType)[len(self.find_elements(*self._paymentType))-1].click()
        self.select_item(text)
        logger.info('选择的款项性质为 : {}'.format(text))
        return self.find_elements(*self._paymentType)[len(self.find_elements(*self._paymentType))-1]

    # 结算条件
    _paymentCondition = (By.ID, 'form_paymentCondition')
    def input_paymentCondition(self, text):
        self.find_elements(*self._paymentCondition)[len(self.find_elements(*self._paymentCondition))-1].send_keys(text)
        logger.info('结算条件为 : {}'.format(text))

    # 计划执行时间
    _plansDate = (By.ID, 'form_plansDate')
    def input_plansDate(self, date):
        self.find_elements(*self._plansDate)[len(self.find_elements(*self._plansDate))-1].click()
        year, month, day = date.split('-')[0], date.split('-')[1], date.split('-')[2]
        self.select_date(year, month, day)
        logger.info('选择的计划执行时间为：{}'.format(date))

    # 结算单位
    def selectSettlementUnit(self, vendorCode, vendorName = ''):
        self.find_element(*(By.CLASS_NAME, 'contract-payment-plan')).find_elements(*(By.ID, 'form_vendorId'))[len(self.find_element(
            *(By.CLASS_NAME, 'contract-payment-plan')).find_elements(*(By.ID, 'form_vendorId')))-1].click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, 'undefined_vendorCode')))
        self.send_text(vendorCode, *(By.ID, 'undefined_vendorCode'))
        self.send_text(vendorName, *(By.ID, 'undefined_vendorName'))
        self.click(*(By.XPATH, '/html/body//form/div[3]/div/button[1]'))
        sleep(1)
        try:
            self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[len(self.find_elements(*(By.CLASS_NAME, 'el-table__row')))-1].click()
        except:
            logger.warning('警告,第一次没找到,重新查找点击')
            self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[len(self.find_elements(*(By.CLASS_NAME, 'el-table__row')))-1].click()
        logger.info('选择结算单位的部门编码为 : {}'.format(vendorCode))
        logger.info('选择结算单位的部门名称为 : {}'.format(vendorName))
        self.click(*(By.XPATH, '/html/body//div[3]/span/button[2]'))

    # 结算金额
    _settlementAmount = (By.ID, 'form_amount')
    def input_settlementAmount(self, text):
        self.find_elements(*self._settlementAmount)[len(self.find_elements(*self._settlementAmount))-2].click()
        element = self.find_elements(*self._settlementAmount)[len(self.find_elements(*self._settlementAmount))-2]
        ActionChains(self.driver).send_keys_to_element(element, Keys.BACKSPACE).send_keys_to_element(element, text).perform()
        logger.info('输入的结算金额为 : {}'.format(text))

    # 控制方式
    _controlType = (By.ID, 'form_controlType')
    def selectPaymentCondition(self, text):
        self.find_elements(*self._controlType)[len(self.find_elements(*self._controlType))-1].click()
        self.select_item(text)
        logger.info('选择的控制方式为 : {}'.format(text))

    # 支付方式
    _paymentMethod = (By.ID, 'form_paymentMethod')
    def selectPaymentMethod(self, text):
        self.find_elements(*self._paymentMethod)[len(self.find_elements(*self._paymentMethod)) - 1].click()
        self.select_item(text)
        logger.info('选择的支付方式为 : {}'.format(text))
