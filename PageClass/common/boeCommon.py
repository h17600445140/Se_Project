# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageClass.basePage import BasePage
from Util import logger,DC



class BoeCommon(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    # 获取 boeNum 号码
    _boeNum = (By.XPATH, '//*[@id="top"]/span[3]')
    def getBoeNum(self):
        self.switchWindow()
        boeNum = self.get_elementText(*self._boeNum)
        logger.info("当前提单单据号为：{}".format(boeNum))
        return boeNum

    # 单据保存
    _boeSaveButton = (By.ID, 'save')
    def click_boeSaveButton(self):
        self.click(*self._boeSaveButton)
    # 单据提交
    _boeSubmitButton = (By.ID, 'submit')
    def click_boeSubmitButton(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self._boeSubmitButton))
        self.click(*self._boeSubmitButton)
        logger.info("点击提交单据")

    # 打印封面
    _printCover = (By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div[2]/div/div[2]/button[1]')
    def click_printCover(self):
        self.click(*self._printCover)
    # 查看单据
    _viewBoe = (By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div[2]/div/div[2]/button[2]')
    def click_viewBoe(self):
        self.click(*self._viewBoe)
    # 复制单据
    _copyBoe = (By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div[2]/div/div[2]/button[3]')
    def click_copyBoe(self):
        self.click(*self._copyBoe)
    # 继续填单
    _continueBoe = (By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div[2]/div/div[2]/button[4]')
    def click_continueBoe(self):
        self.click(*self._continueBoe)
    # 关闭
    _close = (By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div[2]/div/div[2]/button[5]')
    def click_close(self):
        WebDriverWait(self.driver, 8).until(
            EC.visibility_of_element_located(self._close))
        self.click(*self._close)
        logger.info("点击单据关闭按钮")
        self.switchWindow()

    # ---------- 审批 ----------
    # 会记信息Tab
    _accountMessage = (By.ID, 'tab-accounting')
    def click_accountMessage(self):
        WebDriverWait(self.driver, 8).until(
            EC.visibility_of_element_located(self._accountMessage))
        try:
            self.click(*self._accountMessage)
        except:
            sleep(3)
            self.click(*self._accountMessage)
        logger.info("点击单据会记信息")

    # 同意
    _approveButton = (By.XPATH, '//*[@id="pane-accounting"]//div[2]/div[4]/button[1]')
    def click_approveButton(self):
        WebDriverWait(self.driver, 8).until(
            EC.visibility_of_element_located(self._approveButton))
        self.click(*self._approveButton)
        sleep(1)
        logger.info("点击单据审批同意")


    # —————————— 主表区 ——————————
    # 申请人
    _employeeId = (By.ID, 'boeHeader.0.employeeId')
    # 业务类型
    _operationTypeId = (By.ID, 'boeHeader.0.operationTypeId')
    # 纸质附件
    _paperAccessories = (By.ID, 'boeHeader.0.paperAccessories')
    # 借款币种
    _paymentCurrency = (By.ID, 'boeHeader.0.paymentCurrency')
    # 备注
    _boeAbstract = (By.ID, 'boeHeader.0.boeAbstract')

    # 操作主表区

    def input_operationType(self, text):
        self.click(*self._operationTypeId)
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self._operationTypeId))
        self.clear(*self._operationTypeId)
        self.send_text(text, *self._operationTypeId)
        logger.info("选择的业务类型为：{}".format(text))

    def input_boeAbstract(self, text):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self._boeAbstract))
        self.clear(*self._boeAbstract)
        self.send_text(text, *self._boeAbstract)
        logger.info("输入的备注为：{}".format(text))

    # ——————————————————————————————


    # -------------------- 头部附加区 --------------------
    # 供应商/客户
    _vendor = (By.ID, 'boeHeaderChild.0.vendorId')
    def click_vendor(self):
        self.click(*self._vendor)
        logger.info('点击 Vendor 输入框')
    # 选择供应商/客户
    def selectVendor(self, code, vendorName=''):
        self.click_vendor()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(
            (By.ID, 'itemvendorCode')))
        self.send_text(code, *(By.ID, 'itemvendorCode'))
        self.send_text(vendorName, *(By.ID, 'itemname'))
        self.click(*(By.XPATH, '/html/body//form/div[3]/div/button[1]'))
        sleep(1)
        try:
            self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[
                len(self.find_elements(*(By.CLASS_NAME, 'el-table__row'))) - 1].click()
        except:
            logger.warning('警告,第一次没找到,重新查找点击')
            self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[
                len(self.find_elements(*(By.CLASS_NAME, 'el-table__row'))) - 1].click()
        logger.info('选择 Vendor 编码为 : {}'.format(code))
        logger.info('选择 Vendor 名称为 : {}'.format(vendorName))
        self.click(*(By.XPATH, '/html/body//div//span/button[2]'))

    # 合同
    _contract = (By.ID, 'boeHeaderChild.0.contractId')
    def click_contract(self):
        self.click(*self._contract)
    # 选择合同
    def selectContract(self, keyContract):
        self.click_contract()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(
            (By.ID, 'itemkeyword')))
        self.send_text(keyContract, *(By.ID, 'itemkeyword'))
        self.click(*(By.XPATH, '/html/body//form/div[2]/div/button[1]'))
        sleep(1)
        try:
            self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[
                len(self.find_elements(*(By.CLASS_NAME, 'el-table__row'))) - 1].click()
        except:
            logger.warning('警告,第一次没找到,重新查找点击')
            self.find_elements(*(By.CLASS_NAME, 'el-table__row'))[
                len(self.find_elements(*(By.CLASS_NAME, 'el-table__row'))) - 1].click()
        logger.info('选择合同编码为 : {}'.format(keyContract))
        self.click(*(By.XPATH, '/html/body//div//span/button[2]'))

    # --------------------------------------------------


    # —————————— 费用归属区 ——————————

    # 部门
    _expenseDeptId = (By.ID, 'apportion.0.expenseDeptId')
    # 项目
    _projectId = (By.ID, 'apportion.0.projectId')
    # 总金额
    _expenseAmount = (By.ID, 'apportion.0.expenseAmount')

    # 操作费用归属区

    def selectDepartment(self, deptCode, deptName):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self._expenseDeptId))
        try:
            self.click(*self._expenseDeptId)
        except Exception as e:
            logger.warning("出现警告，警告信息为：{}，重试点击操作".format(type(e)))
            self.click(*self._expenseDeptId)
        self.send_text(deptCode, *(By.ID, 'itemDEPT_CODE'))
        self.send_text(deptName, *(By.ID, 'itemDEPT_NAME'))
        self.click(*(By.XPATH, '/html/body//form/div[3]/div/button[1]'))
        sleep(1)
        self.click(*(By.XPATH, '/html/body//table/tbody/tr[1]'))
        self.click(*(By.XPATH, '/html/body//div[3]/span/button[2]'))
        logger.info('选择的部门编码为：{}'.format(deptCode))
        logger.info('选择的部门名称为：{}'.format(deptName))

    def input_projectId(self, text):
        self.click(*self._projectId)
        self.send_text(text, *self._projectId)
        logger.info('选择的项目为：{}'.format(text))
        sleep(1)

    def input_expenseAmount(self, text):
        self.click(*self._expenseAmount)
        element = self.find_element(*self._expenseAmount)
        ActionChains(self.driver).send_keys_to_element(element, Keys.BACKSPACE).perform()
        ActionChains(self.driver).send_keys_to_element(element, text).perform()

    # ——————————————————————————————

    # —————————— 支付区 ——————————
    # 支付方式
    _paymentModeCode = (By.ID, 'zfsBoePayments.0.paymentModeCode')
    # 收款账户
    _vendorId = (By.ID, 'zfsBoePayments.0.vendorId')
    # 支付金额
    _paymentAmount = (By.ID, 'zfsBoePayments.0.paymentAmount')
    # 付款用途
    _paymentMemo = (By.ID, 'zfsBoePayments.0.paymentMemo')

    # 操作支付区

    def input_paymentAmount(self, text):
        self.click(*self._paymentAmount)
        element = self.find_element(*self._paymentAmount)
        ActionChains(self.driver).send_keys_to_element(element, Keys.BACKSPACE).perform()
        ActionChains(self.driver).send_keys_to_element(element, text).perform()

    def input_paymentMemo(self, text):
        self.clear(*self._boeAbstract)
        self.send_text(text, *self._paymentMemo)

    # ——————————————————————————————

    # —————————— 关联发票，新增发票按钮 ——————————
    def click_relateInvoiceButton(self):
        for i in range(len(self.find_element(*(By.ID, 'cost')).find_elements(*(By.TAG_NAME, 'button')))):
            if self.find_element(*(By.ID, 'cost')).find_elements(*(By.TAG_NAME, 'button'))[i].text == '关联发票':
                self.find_element(*(By.ID, 'cost')).find_elements(*(By.TAG_NAME, 'button'))[i].click()

    # 新增发票
    def click_addInvoiceButton(self):
        for i in range(len(self.find_element(*(By.ID, 'cost')).find_elements(*(By.TAG_NAME, 'button')))):
            if self.find_element(*(By.ID, 'cost')).find_elements(*(By.TAG_NAME, 'button'))[i].text == '新增发票':
                self.find_element(*(By.ID, 'cost')).find_elements(*(By.TAG_NAME, 'button'))[i].click()
    # 注意此处和我的发票界面不相同
    _invoiceType = (By.ID, 'itembillTypeInvoice')
    def click_invoiceType(self):
        self.click(*self._invoiceType)
    # ——————————————————————————————


    # —————————— Boe common抽象方法 ——————————

    # 差旅单选择年月
    def selectYearMonth(self, year, month):

        self.find_element(*self._calendar).find_element(*(By.CLASS_NAME, 'year-month')).find_element(
            *(By.TAG_NAME, 'input')).click()

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


    # 日期输入框输入（老方法，新方式见basePage）
    def input_date(self, date):
        if int(date) > 32 or int(date) < 1:
            raise Exception("请输入正确的日期值")
        flag = False
        for i in range(len(self.find_elements(*(By.XPATH, '/html/body/div')))):
            if flag == True:
                break
            if ('el-date-picker' in self.getElementAttribute('class', *(By.XPATH, '/html/body/div[{}]'.format(i + 1)))) and \
                    ('display: none' not in self.getElementAttribute('style', *(By.XPATH, '/html/body/div[{}]'.format(i + 1)))):
                for x in range(6):
                    if flag == True:
                        break
                    for y in range(7):
                        if self.get_elementText(*(By.XPATH, '/html/body/div[{}]/div[1]/div/div[2]/table[1]/tbody/tr[{}]/td[{}]/div/span'.format(i+1,x+2,y+1))) == date:
                            self.click(*(By.XPATH, '/html/body/div[{}]/div[1]/div/div[2]/table[1]/tbody/tr[{}]/td[{}]/div/span'.format(i+1,x+2,y+1)))
                            flag = True
                            break
                        else:
                            pass
        if flag != True:
            logger.error('日期框选择日期失败，请检查配置')
            raise Exception('日期框选择日期失败，请检查配置')
        else:
            logger.info("当前日期框填写的日期值为：{}号".format(date))
