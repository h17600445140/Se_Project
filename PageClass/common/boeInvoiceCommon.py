# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from PageClass.common.boeCommon import BoeCommon
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class BoeInvoiceCommon(BoeCommon):

    def __init__(self, driver):
        BoeCommon.__init__(self, driver)

    # 打开对应发票新增窗口
    def open_addInvoiceWindow(self, type):
        self.select_item(type)

    # 发票新增提交动作
    def click_invoiceSubmitButton(self):
        for i in range(len(self.find_element(By.CLASS_NAME, 'zte-form').find_elements(By.TAG_NAME, 'button'))):
            if self.find_element(By.CLASS_NAME, 'zte-form').find_elements(By.TAG_NAME, 'button')[i].text == '提交':
                self.find_element(By.CLASS_NAME, 'zte-form').find_elements(By.TAG_NAME, 'button')[i].click()

    # ----- 发票公用 -----
    # 发票代码
    _invoiceNo = (By.ID, 'itembillingNo')
    def input_invoiceNo(self, text):
        self.send_text(text, *self._invoiceNo)

    # 发票号码
    _invoiceCode = (By.ID, 'itembillingCode')
    def input_invoiceCode(self, text):
        self.send_text(text, *self._invoiceCode)

    # 日期
    _invoiceDate = (By.ID, 'itembillingTime')
    def selectInvoiceDate(self, year, month, day):
        self.click(*self._invoiceDate)
        self.select_date(year, month, day)

    # 校验码
    _checkCode = (By.ID, 'itemcheckCode')
    def input_checkCode(self, text):
        self.send_text(text, *self._checkCode)

    # 总金额
    _feeTotal = (By.ID, 'itemfee')
    def input_feeTotal(self, text):
        self.click(*self._feeTotal)
        element = self.find_element(*self._feeTotal)
        ActionChains(self.driver).send_keys_to_element(element, Keys.BACKSPACE).perform()
        ActionChains(self.driver).send_keys_to_element(element, text).perform()

    # 税前金额
    _preFee = (By.ID, 'itemfeeWithoutTax')

    # 税额
    _tax = (By.ID, 'itemtax')
    def input_tax(self, text):
        self.click(*self._tax)
        element = self.find_element(*self._tax)
        ActionChains(self.driver).send_keys_to_element(element, Keys.BACKSPACE).perform()
        ActionChains(self.driver).send_keys_to_element(element, text).perform()

    # ---------------------------

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
        sleep(1)

    # 下车车站
    _itemarriveCityName = (By.XPATH, '//*[@id="itemarriveCityName"]/div/div/div[1]/input')

    def input_itemarriveCityName(self, cityName):
        self.click(*self._itemarriveCityName)
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self._itemarriveCityName))
        self.send_text(cityName, *self._itemarriveCityName)
        sleep(1)

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