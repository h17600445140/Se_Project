# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By
from Util import logger
from PageClass.common.boeCommon import BoeCommon
from PageClass.easIndexPageClass.easIndexPage import EasIndexPage



# 差旅报账单（国际）实例
class InternationalTravelBoePage(EasIndexPage,BoeCommon):

    def __init__(self, driver):
        EasIndexPage.__init__(self, driver)

    # 选择币种
    def selectCurrency(self, currencyType):
        self.send_text(currencyType, *(By.ID, 'itemCURRENCY_CODE'))
        self.click(*(By.XPATH, '/html/body//form/div[3]/div/button[1]'))
        sleep(1)
        self.click(*(By.XPATH, '/html/body//table/tbody/tr/td[1]/div/label/span'))
        self.click(*(By.XPATH, '/html/body//div[3]/span/button[2]'))

    # —————————— 城市间交通费区 ——————————

    # 城市间交通费新增按钮
    _cityTrafficExpenseAddButton = (By.XPATH, '/html/body/div/div/div[2]/div[3]/div[2]/div[3]/button')
    def click_cityTrafficExpenseAddButton(self):
        self.click(*self._cityTrafficExpenseAddButton)

    # 是否国内行程
    _isDomesticItineraryTraffic = (By.ID, 'travel.0.isDomesticItinerary')
    def select_isDomesticItineraryTraffic(self, option):
        self.select_option(option, *self._isDomesticItineraryTraffic)

    # 业务小类
    _operationSubTypeIdTraffic = (By.ID, 'travel.0.operationSubTypeId')
    def input_operationSubTypeIdTraffic(self, text):
        self.click(*self._operationSubTypeIdTraffic)
        self.send_text(text, *self._operationSubTypeIdTraffic)

    # 出行人
    _travelerEmpIdTraffic = (By.ID, 'travel.0.travelerEmpId')
    def select_travelerEmpIdTraffic(self):
        pass

    # 行程日期
    _beginDateStrTraffic = (By.ID, 'travel.0.beginDateStr')
    def click_beginDateStrTraffic(self):
        self.click(*self._beginDateStrTraffic)
    # 输入行程日期
    def input_beginDateStrTraffic(self, date):
        self.click_beginDateStrTraffic()
        self.input_date(date)

    # 出发城市
    _fromCityTraffic = (By.XPATH, '//*[@id="travel.0.fromSiteName"]/div/div/div[1]/input')
    # 输入出发城市
    def input_fromCityTraffic(self, text):
        self.click(*self._fromCityTraffic)
        self.send_text(text, *self._fromCityTraffic)

    # 到达城市
    _toCityTraffic = (By.XPATH, '//*[@id="travel.0.toSiteName"]/div/div/div[1]/input')
    # 输入到达城市
    def input_toCityTraffic(self, text):
        self.click(*self._toCityTraffic)
        self.send_text(text, *self._toCityTraffic)

    # 交通工具
    _transportationTraffic = (By.ID, 'travel.0.transportation')
    def select_transportationTraffic(self, option):
        self.select_option(option, *self._transportationTraffic)

    # 发生币种
    _useCurrencyCodeTraffic = (By.ID, 'travel.0.useCurrencyCode')
    def select_useCurrencyCodeTraffic(self, currencyType):
        self.click(*self._useCurrencyCodeTraffic)
        self.selectCurrency(currencyType)

    # 发生金额
    _useCurrencyAmountTraffic = (By.ID, 'travel.0.useCurrencyAmount')
    def input_useCurrencyAmountTraffic(self, amount):
        self.input_amount(amount, *self._useCurrencyAmountTraffic)

    # 汇率
    _rateValueTraffic = (By.XPATH, '//*[@id="travel.0.rateValue"]/div/input')
    def input_rateValueTraffic(self, text):
        self.clear(*self._rateValueTraffic)
        self.send_text(text, *self._rateValueTraffic)

    # 其他税费
    _totalPriceTraffic = (By.ID, 'travel.0.totalPrice')
    def input_totalPriceTraffic(self, amount):
        self.input_amount(amount, *self._totalPriceTraffic)

    # 民航发展基金
    _fuelSurchargeTraffic = (By.ID, 'travel.0.fuelSurcharge')
    def input_fuelSurchargeTraffic(self, amount):
        self.input_amount(amount, *self._fuelSurchargeTraffic)

    # 税种
    _taxRateIdTraffic = (By.ID, 'travel.0.taxRateId')
    def input_taxRateIdTraffic(self, text):
        self.click(*self._taxRateIdTraffic)
        sleep(1)
        self.send_text(text, *self._taxRateIdTraffic)

    # 可抵扣税额
    _taxAmountTraffic = (By.ID, 'travel.0.taxAmount')
    def input_taxAmountTraffic(self, amount):
        self.input_amount(amount, *self._taxAmountTraffic)

    _totalAmountTraffic = (By.XPATH, '/html/body/div[1]/div/div[2]/div[3]/div[2]/div[1]/div/div/form/div[11]/div/div')
    def get_totalAmountTraffic(self):
        amount = self.getElementAttribute('title', *self._totalAmountTraffic)
        return amount

    # —————————— 住宿费 ——————————

    # 住宿费新增按钮
    _hotelExpenseAddButton = (By.XPATH, '/html/body/div/div/div[2]/div[4]/div[2]/div[3]/button')
    def click_hotelExpenseAddButton(self):
        self.click(*self._hotelExpenseAddButton)

    # 业务小类
    _operationSubTypeIdHotel = (By.ID, 'stay.0.operationSubTypeId')
    def input_operationSubTypeIdHotel(self, text):
        self.click(*self._operationSubTypeIdHotel)
        self.send_text(text, *self._operationSubTypeIdHotel)

    # 入住日期
    _beginDateStrHotel = (By.ID, 'stay.0.beginDateStr')
    def click_beginDateStrHotel(self):
        self.click(*self._beginDateStrHotel)
    # 输入入住日期
    def input_beginDateStrHotel(self, date):
        self.click_beginDateStrHotel()
        self.input_date(date)

    # 离店日期
    _endDateStrHotel = (By.ID, 'stay.0.endDateStr')
    def click_endDateStrHotel(self):
        self.click(*self._endDateStrHotel)
    # 输入离店日期
    def input_endDateStrHotel(self, date):
        self.click_endDateStrHotel()
        self.input_date(date)

    # 住宿地点
    _sitePlaceHotel = (By.XPATH, '//*[@id="stay.0.fromSiteName"]/div/div/div[1]/input')
    # 输入住宿城市
    def input_sitePlaceHotel(self, text):
        self.click(*self._sitePlaceHotel)
        self.send_text(text, *self._sitePlaceHotel)

    # 住宿天数
    _hotelDayHotel = (By.XPATH, '//*[@id="stay.0.hotelDay"]/div/input')
    # 输入住宿天数
    def input_hotelDayHotel(self, text):
        self.clear(*self._hotelDayHotel)
        self.send_text(text, *self._hotelDayHotel)

    # 发生币种
    _useCurrencyCodeHotel = (By.ID, 'stay.0.useCurrencyCode')
    def select_useCurrencyCodeHotel(self, currencyType):
        self.click(*self._useCurrencyCodeHotel)
        self.selectCurrency(currencyType)

    # 发生金额
    _useCurrencyAmountHotel = (By.ID, 'stay.0.useCurrencyAmount')
    def input_useCurrencyAmountHotel(self, amount):
        self.input_amount(amount, *self._useCurrencyAmountHotel)

    # 汇率
    _rateValueHotel = (By.XPATH, '//*[@id="stay.0.rateValue"]/div/input')
    def input_rateValueHotel(self, text):
        self.clear(*self._rateValueHotel)
        self.send_text(text, *self._rateValueHotel)

    # 税种
    _taxRateIdHotel = (By.ID, 'stay.0.taxRateId')
    def input_taxRateIdHotel(self, text):
        self.click(*self._taxRateIdHotel)
        sleep(1)
        self.send_text(text, *self._taxRateIdHotel)

    # 可抵扣税额
    _taxAmountHotel = (By.ID, 'stay.0.taxAmount')
    def input_taxAmountHotel(self, amount):
        self.input_amount(amount, *self._taxAmountHotel)

    _totalAmountHotel = (By.XPATH, '/html/body/div[1]/div/div[2]/div[4]/div[2]/div[1]/div/div/form/div[9]/div/div')
    def get_totalAmountHotel(self):
        amount = self.getElementAttribute('title', *self._totalAmountHotel)
        return amount

    # —————————— 补贴 ——————————

    # 业务小类
    _operationSubTypeIdSubsidy = (By.ID, 'subsidy.0.operationSubTypeId')
    def input_operationSubTypeIdSubsidy(self, text):
        self.click(*self._operationSubTypeIdSubsidy)
        self.send_text(text, *self._operationSubTypeIdSubsidy)

    # 补贴天数
    _subsidyDaySubsidy = (By.XPATH, '//*[@id="subsidy.0.subsidyDay"]/div/input')
    # 输入补贴天数
    def input_subsidyDaySubsidy(self, text):
        self.clear(*self._subsidyDaySubsidy)
        self.send_text(text, *self._subsidyDaySubsidy)

    # 地点
    _sitePlaceSubsidy = (By.XPATH, '//*[@id="subsidy.0.fromSiteName"]/div/div/div[1]/input')
    # 输入地点
    def input_sitePlaceSubsidy(self, text):
        self.click(*self._sitePlaceSubsidy)
        self.send_text(text, *self._sitePlaceSubsidy)

    # 补贴币种
    _useCurrencyCodeSubsidy = (By.ID, 'subsidy.0.useCurrencyCode')
    def select_useCurrencyCodeSubsidy(self, currencyType):
        self.click(*self._useCurrencyCodeSubsidy)
        self.selectCurrency(currencyType)

    # 补贴金额
    _useCurrencyAmountSubsidy = (By.ID, 'subsidy.0.useCurrencyAmount')
    def input_useCurrencyAmountSubsidy(self, amount):
        self.input_amount(amount, *self._useCurrencyAmountSubsidy)

    # 汇率
    _rateValueSubsidy = (By.XPATH, '//*[@id="subsidy.0.rateValue"]/div/input')
    def input_rateValueSubsidy(self, text):
        self.clear(*self._rateValueSubsidy)
        self.send_text(text, *self._rateValueSubsidy)

    _totalAmountSubsidy = (By.XPATH, '/html/body/div[1]/div/div[2]/div[5]/div[2]/div[1]/div/div/form/div[7]/div/div')
    def get_totalAmountSubsidy(self):
        amount = self.getElementAttribute('title', *self._totalAmountSubsidy)
        return amount

    # —————————— 其他 ——————————

    # 业务小类
    _operationSubTypeIdOther = (By.ID, 'other.0.operationSubTypeId')

    def input_operationSubTypeIdOther(self, text):
        self.click(*self._operationSubTypeIdOther)
        self.send_text(text, *self._operationSubTypeIdOther)

    # 发生币种
    _useCurrencyCodeOther = (By.ID, 'other.0.useCurrencyCode')
    def select_useCurrencyCodeOther(self, currencyType):
        self.click(*self._useCurrencyCodeOther)
        self.selectCurrency(currencyType)

    # 发生金额
    _useCurrencyAmountOther = (By.ID, 'other.0.useCurrencyAmount')
    def input_useCurrencyAmountOther(self, amount):
        self.input_amount(amount, *self._useCurrencyAmountOther)

    # 汇率
    _rateValueOther = (By.XPATH, '//*[@id="other.0.rateValue"]/div/input')
    def input_rateValueOther(self, text):
        self.clear(*self._rateValueOther)
        self.send_text(text, *self._rateValueOther)

    # 税种
    _taxRateIdOther = (By.ID, 'other.0.taxRateId')
    def input_taxRateIdOther(self, text):
        self.click(*self._taxRateIdOther)
        sleep(1)
        self.send_text(text, *self._taxRateIdOther)

    # 可抵扣税额
    _taxAmountOther = (By.ID, 'other.0.taxAmount')
    def input_taxAmountOther(self, amount):
        self.input_amount(amount, *self._taxAmountOther)

    # 备注
    _remarkOther = (By.ID, 'other.0.remark')
    def input_remarkOther(self, text):
        self.input_amount(text, *self._remarkOther)

    _totalAmountOther = (By.XPATH, '/html/body/div[1]/div/div[2]/div[6]/div[2]/div[1]/div/div/form/div[5]/div/div')
    def get_totalAmountOther(self):
        amount = self.getElementAttribute('title', *self._totalAmountOther)
        return amount
