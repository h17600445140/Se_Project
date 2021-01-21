# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageClass.basePage import BasePage
from Util import logger,DC



class BoeCommen(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    # 获取 boeNum 号码
    _boeNum = (By.XPATH, '//*[@id="top"]/span[3]')
    def getBoeNum(self):
        return self.get_elementText(*self._boeNum)

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
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self._close))
        self.click(*self._close)

    # ---------- 审批 ----------
    # 会记信息Tab
    _accountMessage = (By.ID, 'tab-accounting')
    def click_accountMessage(self):
        self.click(*self._accountMessage)

    # 同意
    _approveButton = (By.XPATH, '//*[@id="pane-accounting"]//div[2]/div[4]/button[1]')
    def click_approveButton(self):
        try:
            self.click(*self._approveButton)
        except:
            raise Exception('没有找到同意按钮')

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
        self.clear(*self._operationTypeId)
        self.send_text(text, *self._operationTypeId)

    def input_boeAbstract(self, text):
        self.clear(*self._boeAbstract)
        self.send_text(text, *self._boeAbstract)

    # ——————————————————————————————

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
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located( (By.XPATH, '/html/body//table/tbody/tr[1]') ))
        self.click(*(By.XPATH, '/html/body//table/tbody/tr[1]'))
        self.click(*(By.XPATH, '/html/body//div[3]/span/button[2]'))

    def input_projectId(self, text):
        self.click(*self._projectId)
        self.send_text(text, *self._projectId)

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

    _invoiceType = (By.ID, 'itembillTypeInvoice')
    def click_invoiceType(self):
        self.click(*self._invoiceType)
    # ——————————————————————————————


    # —————————— Boe common抽象方法 ——————————
    # 金额输入框输入
    def input_amount(self, text, *loc):
        self.click(*loc)
        element = self.find_element(*loc)
        ActionChains(self.driver).send_keys_to_element(element, Keys.BACKSPACE).perform()
        ActionChains(self.driver).send_keys_to_element(element, text).perform()

    # 系统编码下拉选择框选择
    def select_option(self, option, *loc):
        self.click(*loc)
        sleep(1)
        for i in range(30):
            if i == 29:
                logger.error('没有找到对应配置项，请检查配置')
                raise Exception('没有找到对应配置项，请检查配置')
            if self.get_elementText(*(loc[0], (loc[1] + '.option.{}').format(i))) == option:
                self.moveToclick(*(loc[0], (loc[1] + '.option.{}').format(i)))
                break
        logger.info('选择的数据为：{}'.format(option))

    # 浮动下拉框选择
    def select_item(self, type):
        for i in range(len(self.find_elements(*(By.CLASS_NAME, 'el-select-dropdown__item')))):
            if self.find_elements(*(By.CLASS_NAME, 'el-select-dropdown__item'))[i].text == type:
                element = self.find_elements(*(By.CLASS_NAME, 'el-select-dropdown__item'))[i]
                ActionChains(self.driver).move_to_element(element).perform()
                element.click()

    # 操作日期面板

    _calendar = (By.CLASS_NAME, 'calendar')
    # 日期控件选择年月日
    def select_date(self, year, month, day):

        dateHeaderPanel = self.find_element(*(By.CLASS_NAME, 'el-date-picker__header'))
        dateContentPanel = self.find_element(*(By.CLASS_NAME, 'el-picker-panel__content'))

        # 操作年份
        selectedY = dateHeaderPanel.find_elements(*(By.TAG_NAME, 'span'))[0].text
        selectedYear = selectedY.split(' ')[0]
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
        selectedM = dateHeaderPanel.find_elements(*(By.TAG_NAME, 'span'))[1].text
        selectedMonth = selectedM.split(' ')[0]
        if month > selectedMonth:
            num = int(month) - int(selectedMonth)
            for i in range(num):
                dateHeaderPanel.find_elements(*(By.TAG_NAME, 'button'))[3].click()
        elif month < selectedMonth:
            num = int(selectedMonth) - int(month)
            for i in range(num):
                dateHeaderPanel.find_elements(*(By.TAG_NAME, 'button'))[1].click()
        elif month == selectedMonth:
            pass

        # 操作日
        dayTable = dateContentPanel.find_element(*(By.CLASS_NAME, 'el-date-table'))
        for i in range(len(dayTable.find_elements(*(By.TAG_NAME, 'span')))):
            if dayTable.find_elements(*(By.TAG_NAME, 'span'))[i].text == day:
                dayTable.find_elements(*(By.TAG_NAME, 'span'))[i].click()

        if 'display: none' not in self.find_element(*(By.CLASS_NAME, 'el-picker-panel__footer')).get_attribute('style'):
            self.find_element(*(By.CLASS_NAME, 'el-picker-panel__footer')).find_elements(*(By.TAG_NAME, 'button'))[1].click()


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


    # 日期输入框输入
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
