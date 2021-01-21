# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageClass.basePage import BasePage
from PageClass.common.boeCommon import BoeCommen
from Util import logger, config



class EasMyInvoiceIndexPage(BoeCommen):

    _reimbursementState = (By.ID, 'undefined_reimbursementState')
    _billTypeInvoice = (By.ID, 'undefined_billTypeInvoice')
    _billingCode = (By.ID, 'undefined_billingCode')

    _myInvoiceQueryButton = (By.XPATH, '//*[@id="app"]/section/main/div[2]/div/div[1]/div[1]/form/div[10]/div/button[1]')
    _invoiceQueryResult = (By.XPATH, '//*[@id="app"]/section/main/div[2]/div/div[1]/div[4]/div/div[1]/div/div[2]/div[1]')

    _manualInvoiceEntry = (By.XPATH, '//*[@id="app"]/section/main/div[2]/div/div[1]/div[2]/button[1]')

    _invoiceType = (By.ID, 'form_billTypeInvoice')

    # ----- 发票公用 -----
    # 发票代码
    _invoiceNo = (By.ID, 'form_billingNo')
    # 发票号码
    _invoiceCode = (By.ID, 'form_billingCode')
    # 日期
    _invoiceDate = (By.ID, 'form_billingTime')
    # 校验码
    _checkCode = (By.ID, 'form_checkCode')
    # 总金额
    _feeTotal = (By.ID, 'form_fee')
    # 税前金额
    _preFee = (By.ID, 'form_feeWithoutTax')
    # 税额
    _tax = (By.ID, 'form_tax')

    _personRemark = (By.ID, 'form_personnelAttribution')
    _personName = (By.ID, 'form_passengerName')
    _tripDate = (By.ID, 'form_tripDate')
    _ticketPrice = (By.ID, 'form_fee')


    _seatLevel = (By.ID, 'form_seatLevel')
    _startOffCityName = (By.XPATH, '//*[@id="form_startOffCityName"]/div[2]/div/div[1]/input')
    _arriveCityName = (By.XPATH, '//*[@id="form_arriveCityName"]/div/div/div[1]/input')

    # 发票新增提交动作
    def click_invoiceSubmitButton(self):
        for i in range(len(self.find_element(By.CLASS_NAME, 'zte-form').find_elements(By.TAG_NAME, 'button'))):
            if self.find_element(By.CLASS_NAME, 'zte-form').find_elements(By.TAG_NAME, 'button')[i].text == '提交':
                self.find_element(By.CLASS_NAME, 'zte-form').find_elements(By.TAG_NAME, 'button')[i].click()

    # ---------- 火车票 ----------
    # 人员标记
    _itempersonnelAttribution = (By.ID, 'itempersonnelAttribution')
    def select_itempersonnelAttribution(self, type):
        self.click(*self._itempersonnelAttribution)
        self.select_item(type)

    _itemtripDate = (By.ID, 'itemtripDate')
    def select_itemtripDate(self, year, month, day):
        self.click(*self._itemtripDate)
        self.select_date(year, month, day)

    # 乘客人名称
    _itempassengerName = (By.ID, 'itempassengerName')
    def input_itempassengerName(self, name):
        self.send_text(name, *self._itempassengerName)

    # 上车车站
    _itemstartOffCityName = (By.XPATH, '//*[@id="itemstartOffCityName"]/div/div/div[1]/input')
    def input_itemstartOffCityName(self, cityName):
        self.click(*self._itemstartOffCityName)
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self._itemstartOffCityName))
        self.send_text(cityName, *self._itemstartOffCityName)
        sleep(0.5)

    # 下车车站
    _itemarriveCityName = (By.XPATH, '//*[@id="itemarriveCityName"]/div/div/div[1]/input')
    def input_itemarriveCityName(self, cityName):
        self.click(*self._itemarriveCityName)
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self._itemarriveCityName))
        self.send_text(cityName, *self._itemarriveCityName)
        sleep(0.5)

    # 座位级别
    _itemseatLevel = (By.ID, 'itemseatLevel')
    def select_itemseatLevel(self, type):
        self.click(*self._itemseatLevel)
        self.select_item(type)

    # 总金额
    _itemfee = (By.ID, 'itemfee')
    def input_itemfee(self, amount):
        self.input_amount(amount, *self._itemfee)

    # 是否补票
    _itemisReplacementTicket = (By.ID, 'itemisReplacementTicket')
    def select_itemisReplacementTicket(self, type):
        self.click(*self._itemisReplacementTicket)
        self.select_item(type)

    # ---------------------------

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def input_billingCode(self, text):
        self.send_text(text, *self._billingCode)

    def click_myInvoiceQueryButton(self):
        self.click(*self._myInvoiceQueryButton)

    def open_manualInvoiceEntry(self):
        self.click(*self._manualInvoiceEntry)

    def click_invoiceType(self):
        self.click(*self._invoiceType)

    # 打开对应发票新增窗口
    def open_addInvoiceWindow(self, type):
        self.select_item(type)

    def input_invoiceNo(self, text):
        self.send_text(text, *self._invoiceNo)

    def input_invoiceCode(self, text):
        self.send_text(text, *self._invoiceCode)

    def selectInvoiceDate(self):
        self.click(*self._invoiceDate)
        sleep(1)
        self.click(*(By.XPATH, '/html/body/div[4]/div[1]/div/div[2]/table[1]/tbody/tr[5]/td[4]/div/span'))

    def input_feeTotal(self, text):
        self.click(*self._feeTotal)
        element = self.find_element(*self._feeTotal)
        ActionChains(self.driver).send_keys_to_element(element, Keys.BACKSPACE).perform()
        ActionChains(self.driver).send_keys_to_element(element, text).perform()

    def input_tax(self, text):
        self.click(*self._tax)
        element = self.find_element(*self._tax)
        ActionChains(self.driver).send_keys_to_element(element, Keys.BACKSPACE).perform()
        ActionChains(self.driver).send_keys_to_element(element, text).perform()

    def input_checkCode(self, text):
        self.send_text(text, *self._checkCode)



    @property
    def invoiceQueryResult(self):
        return self.elementExistIsOrNot(*self._invoiceQueryResult)

    def gotoInvoiceQueryPage(self):
        self.driver.get(config.getUrlDict()['url']['invoiceIpoolHost'])
