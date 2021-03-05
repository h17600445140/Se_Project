# -*- coding:utf-8 -*-
import datetime
import string
import random
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageClass.fscIndexPageClass.fscCommonPage import FscCommonPage
from Util import logger
from dateutil.relativedelta import relativedelta



class BillExchangePage(FscCommonPage):


    def __init__(self,driver):
        FscCommonPage.__init__(self,driver)


    _le = (By.ID, 'undefined_leId')
    def click_le(self):
        """
        describe：
            点击核算主体选择框
        :param : No param
        :return: None
        """
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self._le))
        self.click(*self._le)


    def selectLe(self, leCode, leName=''):
        """
        describe：
            进入核算主体选择框选择对应的核算主体
        :param leCode: 核算主体编码
        :param leName: 核算主体名称
        :return: None
        """
        self.click_le()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(
            (By.ID, 'undefined_CODE')))
        self.send_text(leCode, *(By.ID, 'undefined_CODE'))
        self.send_text(leName, *(By.ID, 'undefined_NAME'))
        self.click(*(By.XPATH, '/html/body//form/div[3]/div/button[1]'))
        sleep(1)
        try:
            self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[
                len(self.find_elements(*(By.CLASS_NAME, 'el-table__row'))) - 1].click()
        except:
            logger.warning('警告,第一次没找到,重新查找点击')
            self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[
                len(self.find_elements(*(By.CLASS_NAME, 'el-table__row'))) - 1].click()
        logger.info('选择的核算主体编码为 : {}'.format(leCode))
        logger.info('选择的核算主体名称为 : {}'.format(leName))
        self.click(*(By.XPATH, '/html/body//div//span/button[2]'))


    def __selectLe(self, leCode, leName=''):
        """
        describe：
            form表单点击新增选择核算主体
        :param leCode: 核算主体编码
        :param leName: 核算主体名称
        :return: None
        """
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, 'form_leId')))
        self.click(*(By.ID, 'form_leId'))
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(
            (By.ID, 'undefined_CODE')))
        self.send_text(leCode, *(By.ID, 'undefined_CODE'))
        self.send_text(leName, *(By.ID, 'undefined_NAME'))
        self.click(*(By.XPATH, '/html/body//form/div[3]/div/button[1]'))
        sleep(1)
        try:
            self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[
                len(self.find_elements(*(By.CLASS_NAME, 'el-table__row'))) - 1].click()
        except:
            logger.warning('警告,第一次没找到,重新查找点击')
            self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[
                len(self.find_elements(*(By.CLASS_NAME, 'el-table__row'))) - 1].click()
        logger.info('选择的核算主体编码为 : {}'.format(leCode))
        logger.info('选择的核算主体名称为 : {}'.format(leName))
        self.click(*(By.XPATH, '/html/body//div//span/button[2]'))


    def __selectCompanyBank(self, account):
        """
        describe：
            form表单点击新增选择归属账户
        :param account: 银行账户
        :return: None
        """
        self.click(*(By.ID, 'form_companyBankId'))
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(
            (By.ID, 'undefined_BANK_ACCOUNT_NUM')))
        self.send_text(account, *(By.ID, 'undefined_BANK_ACCOUNT_NUM'))
        self.click(*(By.XPATH, '/html/body//form/div[2]/div/button[1]'))
        sleep(1)
        try:
            self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[
                len(self.find_elements(*(By.CLASS_NAME, 'el-table__row'))) - 1].click()
        except:
            logger.warning('警告,第一次没找到,重新查找点击')
            self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[
                len(self.find_elements(*(By.CLASS_NAME, 'el-table__row'))) - 1].click()
        logger.info('选择的核算主体编码为 : {}'.format(account))
        self.click(*(By.XPATH, '/html/body//div//span/button[2]'))


    def __inputPostalOrderCode(self, text):
        """
        describe：
            form表单输入汇票编码
        :param text: 汇票编码
        :return: None
        """
        self.send_text(text, *(By.ID, 'form_postalOrderCode'))


    def __selectBillType(self, text):
        """
        describe：
                form表单选择汇票类型
        :param text: 汇票类型
        :return: None
        """
        self.click(*(By.ID, 'form_billType'))
        logger.info('选择的汇票类型为 : {}'.format(text))
        self.select_item(text)


    def __selectPaperTypeCode(self, text):
        """
        describe：
                form表单选择汇票形式
        :param text: 汇票形式
        :return: None
        """
        self.click(*(By.ID, 'form_paperTypeCode'))
        logger.info('选择的汇票形式为 : {}'.format(text))
        self.select_item(text)


    def __inputPayVendorName(self, text):
        """
        describe：
                form表单输入出票方
        :param text: 出票方
        :return: None
        """
        self.send_text(text, *(By.ID, 'form_payVendorName'))


    def __selectPreEndorse(self, name):
        """
        describe：
            form表单选择往来方
        :param name: 往来方名字
        :return: None
        """
        self.click(*(By.ID, 'form_preEndorseId'))
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(
            (By.ID, 'undefined_NAME')))
        self.send_text(name, *(By.ID, 'undefined_NAME'))
        self.click(*(By.XPATH, '/html/body//form/div[2]/div/button[1]'))
        sleep(1)
        try:
            self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[
                len(self.find_elements(*(By.CLASS_NAME, 'el-table__row'))) - 1].click()
        except:
            logger.warning('警告,第一次没找到,重新查找点击')
            self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[
                len(self.find_elements(*(By.CLASS_NAME, 'el-table__row'))) - 1].click()
        logger.info('选择的供应商名称为 : {}'.format(name))
        self.click(*(By.XPATH, '/html/body//div//span/button[2]'))


    def __selectTicketDate(self, date):
        """
        describe：
            form表单选择出票日期
        :param date: 出票日期
        :return: None
        """
        self.click(*(By.ID, 'form_ticketDate'))
        year, month, day = date.split('-')[0], date.split('-')[1], date.split('-')[2]
        self.select_date(year, month, day)
        logger.info('选择的出票日期为：{}'.format(date))


    def __selectBillExpireDate(self, date):
        """
        describe：
            form表单选择到期日期
        :param date: 到期日期
        :return: None
        """
        self.click(*(By.ID, 'form_billExpireDate'))
        year, month, day = date.split('-')[0], date.split('-')[1], date.split('-')[2]
        self.select_date(year, month, day)
        logger.info('选择的到期日期为：{}'.format(date))


    def __inputTicketAmount(self, text):
        """
        describe：
            form表单输入出票金额
        :param text: 出票金额
        :return: None
        """
        self.input_amount(text, *(By.ID, 'form_ticketAmount'))
        logger.info("输入的出票金额为：{}".format(text))


    def __inputContractCode(self, text):
        """
        describe：
                form表单输入合同编码
        :param text: 合同编码
        :return: None
        """
        self.send_text(text, *(By.ID, 'form_contractCode'))


    def __selectOperator(self, empNo, empName=''):
        """
        describe：
            form表单选择经办人
        :param empNo: 员工工号
        :param empNum: 员工名称
        :return: None
        """
        self.click(*(By.ID, 'form_operatorId'))
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(
            (By.ID, 'undefined_EMP_NO')))
        self.send_text(empNo, *(By.ID, 'undefined_EMP_NO'))
        self.send_text(empName, *(By.ID, 'undefined_EMP_NAME'))
        self.click(*(By.XPATH, '/html/body//form/div[3]/div/button[1]'))
        sleep(1)
        try:
            self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[
                len(self.find_elements(*(By.CLASS_NAME, 'el-table__row'))) - 1].click()
        except:
            logger.warning('警告,第一次没找到,重新查找点击')
            self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[
                len(self.find_elements(*(By.CLASS_NAME, 'el-table__row'))) - 1].click()
        logger.info('选择员工工号为 : {}'.format(empNo))
        logger.info('选择员工名称为 : {}'.format(empName))
        self.click(*(By.XPATH, '/html/body//div//span/button[2]'))


    def __selectOperatorDept(self, deptName, companyName=''):
        """
        describe：
            form表单选择经办部门
        :param deptName: 部门名称
        :param companyName: 公司名称
        :return: None
        """
        self.click(*(By.ID, 'form_operatorDeptId'))
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(
            (By.ID, 'undefined_DEPT_NAME')))
        self.send_text(deptName, *(By.ID, 'undefined_DEPT_NAME'))
        self.send_text(companyName, *(By.ID, 'undefined_COMPANY_NAME'))
        self.click(*(By.XPATH, '/html/body//form/div[3]/div/button[1]'))
        sleep(1)
        try:
            self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[
                len(self.find_elements(*(By.CLASS_NAME, 'el-table__row'))) - 1].click()
        except:
            logger.warning('警告,第一次没找到,重新查找点击')
            self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[
                len(self.find_elements(*(By.CLASS_NAME, 'el-table__row'))) - 1].click()
        logger.info('选择部门名称为 : {}'.format(deptName))
        logger.info('选择公司名称为 : {}'.format(companyName))
        self.click(*(By.XPATH, '/html/body//div//span/button[2]'))


    def __selectSignEmp(self, loginName, realName=''):
        """
        describe：
            form表单选择签收人
        :param loginName: 登录账号
        :param realName: 员工名称
        :return: None
        """
        self.click(*(By.ID, 'form_signEmpId'))
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(
            (By.ID, 'undefined_LOGIN_NAME')))
        self.send_text(loginName, *(By.ID, 'undefined_LOGIN_NAME'))
        self.send_text(realName, *(By.ID, 'undefined_REAL_NAME'))
        self.click(*(By.XPATH, '/html/body//form/div[3]/div/button[1]'))
        sleep(3)
        try:
            self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[
                len(self.find_elements(*(By.CLASS_NAME, 'el-table__row'))) - 1].click()
        except:
            logger.warning('警告,第一次没找到,重新查找点击')
            self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[
                len(self.find_elements(*(By.CLASS_NAME, 'el-table__row'))) - 1].click()
        logger.info('选择登录账号为 : {}'.format(loginName))
        logger.info('选择员工名称为 : {}'.format(realName))
        self.click(*(By.XPATH, '/html/body//div//span/button[2]'))


    def __selectSignDate(self, date):
        """
        describe：
            form表单选择到期日期
        :param date: 到期日期
        :return: None
        """
        self.click(*(By.ID, 'form_signDate'))
        year, month, day = date.split('-')[0], date.split('-')[1], date.split('-')[2]
        self.select_date(year, month, day)
        logger.info('选择的签收日期为：{}'.format(date))


    def addReceivableExchangeBill(self):

        self.clickTargetButton('新增')

        self.__selectLe('UIHSZT')

        self.__selectCompanyBank('1109123456789')

        postalOrder = 'UI' + "".join(random.choice(string.digits) for _ in range(8))

        self.__inputPostalOrderCode(postalOrder)

        self.__selectBillType('银行承兑汇票')

        self.__selectPaperTypeCode('电票')

        self.__inputPayVendorName('UI01')

        self.__selectPreEndorse('UI供应商')

        self.__selectTicketDate(datetime.datetime.now().strftime("%Y-%m-%d"))

        self.__selectBillExpireDate(str(datetime.date.today() + relativedelta(months=+1)))

        self.__inputTicketAmount('100.00')

        self.__inputContractCode('UI' + "".join(random.choice(string.digits) for _ in range(8)))

        self.__selectOperator('UI01')

        self.__selectOperatorDept('UI部门')

        self.__selectSignDate(datetime.datetime.now().strftime("%Y-%m-%d"))

        self.__selectSignEmp('UI01')

        self.clickTargetButton('提交')

        return postalOrder


if __name__ == '__main__':
    print(str(datetime.date.today() + relativedelta(months=+3)))




