# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from PageClass.basePage import BasePage



class ReimbursementBasisPageClass(BasePage):

    _reimbursementBasis = (By.CSS_SELECTOR, '#app > section > section > aside > div > div.menu-sroll.el-scrollbar > div.el-scrollbar__wrap > div > ul > li:nth-child(5) > div > span')
    _businessType = (By.CSS_SELECTOR, '#app > section > section > aside > div > div.menu-sroll.el-scrollbar > div.el-scrollbar__wrap > div > ul > li.el-submenu.is-opened > ul > li:nth-child(2) > span')

    def open_reimbursementBasis(self):
        self.click(*self._reimbursementBasis)

    def getReimbursementBasis(self):
        return self._reimbursementBasis

    def open_businessType(self):
        self.click(*self._businessType)

    def __init__(self, driver):
        BasePage.__init__(self, driver)

class BusinessTypePageClass(ReimbursementBasisPageClass):

    _filterBox = (By.XPATH, '//*[@id="app"]/section/section/section/main/div/div/div[1]/div[1]/input')
    _businessOpen = (By.XPATH, '//*[@id="app"]/section/section/section/main/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/span[1]')

    _totalBusinessType = (By.XPATH, '//*[@id="app"]/section/section/section/main/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/span[2]/span')
    _businessTypeBig = (By.XPATH, '//*[@id="app"]/section/section/section/main/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/span[2]/span')

    _addBusinessCategoryBigButton = (By.XPATH, '//*[@id="pane-default"]/div/button/span')

    _businessTypeCodeBox = (By.ID, 'form_code')
    _businessTypeNameCBox = (By.ID, 'form_name_zh-CN')
    _businessTypeNameEBox = (By.ID, 'form_name_en-US')
    _businessTypeNumBox = (By.ID, 'form_orderNum')
    _icon = (By.XPATH, '//*[@id="form"]/div[5]/div/div/div/div/div/div/input')
    _appDisplayOrNot = (By.ID, 'form_appShow')
    _appDisplayNameCBox = (By.ID, 'form_appName_zh-CN')
    _appDisplayNameEBox = (By.ID, 'form_appName_en-US')
    _auditPointsCBox = (By.ID, 'form_auditPoints_zh-CN')
    _auditPointsEBox = (By.ID, 'form_auditPoints_en-US')
    _remarkCBox = (By.ID, 'form_remark_zh-CN')
    _remarkEBox = (By.ID, 'form_remark_en-US')
    _attribute  = (By.ID, 'form_attribute')
    _statisticalDimension = (By.ID, 'form_statisticalDimensionId')

    _cancelButton = (By.XPATH, '//*[@id="form"]/div[15]/div/button[1]/span')
    _submitButton = (By.XPATH, '//*[@id="form"]/div[15]/div/button[2]/span')

    _editButton = (By.XPATH, '//*[@id="pane-default"]/div[1]/button[2]/span')
    _deleteButton = (By.XPATH, '//*[@id="pane-default"]/div[1]/span/button/span')
    _deleteSubmitButton = (By.XPATH, '//body/div[2]/div/button[2]')

    def __init__(self, driver):
        ReimbursementBasisPageClass.__init__(self, driver)

    def input_filterBox(self, text):
        self.clear(*self._filterBox)
        self.send_text(text, *self._filterBox)

    def click_businessOpen(self):
        self.click(*self._businessOpen)

    def click_totalBusinessType(self):
        self.click(*self._totalBusinessType)

    def getTotalBusinessType(self):
        return self._totalBusinessType

    def click_businessTypeBig(self):
        self.click(*self._businessTypeBig)

    def getBusinessTypeBig(self):
        return self._businessTypeBig

    def click_addBusinessCategoryBigButton(self):
        self.click(*self._addBusinessCategoryBigButton)

    def input_businessTypeCodeBox(self, text):
        self.clear(*self._businessTypeCodeBox)
        self.send_text(text, *self._businessTypeCodeBox)

    def input_businessTypeNameCBox(self, text):
        self.clear(*self._businessTypeNameCBox)
        self.send_text(text, *self._businessTypeNameCBox)

    def input_businessTypeNameEBox(self, text):
        self.clear(*self._businessTypeNameEBox)
        self.send_text(text, *self._businessTypeNameEBox)

    def input_businessTypeNumBox(self, text):
        self.clear(*self._businessTypeNumBox)
        self.send_text(text, *self._businessTypeNumBox)

    def icon(self):
        pass

    def appDisplayOrNot(self):
        pass

    def input_appDisplayNameCBox(self, text):
        self.clear(*self._appDisplayNameCBox)
        self.send_text(text, *self._appDisplayNameCBox)

    def input_appDisplayNameEBox(self, text):
        self.clear(*self._appDisplayNameEBox)
        self.send_text(text, *self._appDisplayNameEBox)

    def input_auditPointsCBox(self, text):
        self.clear(*self._auditPointsCBox)
        self.send_text(text, *self._auditPointsCBox)

    def input_auditPointsEBox(self, text):
        self.clear(*self._auditPointsEBox)
        self.send_text(text, *self._auditPointsEBox)

    def input_remarkCBox(self, text):
        self.clear(*self._remarkCBox)
        self.send_text(text, *self._remarkCBox)

    def input_remarkEBox(self, text):
        self.clear(*self._remarkEBox)
        self.send_text(text, *self._remarkEBox)

    def click_submitButton(self):
        self.click(*self._submitButton)

    def click_deleteButton(self):
        self.click(*self._deleteButton)

    def click_deleteSubmitButton(self):
        self.click(*self._deleteSubmitButton)

    def click_editButton(self):
        self.click(*self._editButton)
