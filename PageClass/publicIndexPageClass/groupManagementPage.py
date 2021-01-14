# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from PageClass.basePage import BasePage



class GroupManagementPage(BasePage):

    _groupManagement = (By.XPATH, '//*[@id="app"]/section/section/aside/div/div[2]/div[1]/div/ul/li[1]/div/span')
    _management = (By.XPATH, '//*[@id="app"]/section/section/aside/div/div[2]/div[1]/div/ul/li[1]/ul/li[1]/span')
    _role = (By.XPATH, '//*[@id="app"]/section/section/aside/div/div[2]/div[1]/div/ul/li[1]/ul/li[2]/span')
    _user = (By.XPATH, '//*[@id="app"]/section/section/aside/div/div[2]/div[1]/div/ul/li[1]/ul/li[3]/span')

    _add = (By.XPATH, '//*[@id="app"]/section/section/section/main/div/div/div/div[2]/button[1]/span')
    _delete = (By.XPATH, '//*[@id="app"]/section/section/section/main/div/div/div/div[2]/button[2]/span')
    _enable = (By.XPATH, '//*[@id="app"]/section/section/section/main/div/div/div/div[2]/button[3]/span')
    _disable = (By.XPATH, '//*[@id="app"]/section/section/section/main/div/div/div/div[2]/button[4]/span')

    _select = (By.XPATH, '//*[@id="app"]/section/section/section/main/div/div/div/div[1]/form/div[2]/div/button[1]/span')
    _reset = (By.XPATH, '//*[@id="app"]/section/section/section/main/div/div/div/div[1]/form/div[2]/div/button[2]/span')

    toastBox = (By.XPATH, '/html/body/div[2]/p')

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def open_groupManagement(self):
        self.click(*self._groupManagement)

    def getGroupManagement(self):
        return self._groupManagement

    def open_management(self):
        self.click(*self._management)

    def open_role(self):
        self.click(*self._role)

    def open_user(self):
        self.click(*self._user)

class ManagementPage(GroupManagementPage):

    _groupCname = (By.ID, 'form_name_zh-CN')
    _groupEname = (By.ID, 'form_name_en-US')
    _groupCode = (By.ID, 'form_codeNo')
    _maxUserRegister = (By.ID, 'form_encryptMaxAccount')
    _describeC = (By.ID, 'form_remark_zh-CN')
    _describeE = (By.ID, 'form_remark_en-US')

    _cancel = (By.XPATH, '//*[@id="form"]/div[8]/div/button[1]/span')
    _confirm = (By.XPATH, '//*[@id="form"]/div[8]/div/button[2]/span')

    groupCname_errorBox = (By.XPATH, '//*[@id="form"]/div[1]/div/div[2]')
    groupCode_errorBox = (By.XPATH, '//*[@id="form"]/div[3]/div/div[2]')
    maxUserRegister_errorBox = (By.XPATH, '//*[@id="form"]/div[4]/div/div[2]')

    def __init__(self,driver):
        GroupManagementPage.__init__(self,driver)

    def clickAddButton(self):
        self.click(*self._add)

    def clickDeleteButton(self):
        self.click(*self._delete)

    def clickEnableButton(self):
        self.click(*self._enable)

    def clickDisableButton(self):
        self.click(*self._disable)

    def input_groupCname(self, text):
        self.clear(*self._groupCname)
        self.send_text(text, *self._groupCname)

    def input_groupEname(self, text):
        self.clear(*self._groupEname)
        self.send_text(text, *self._groupEname)

    def input_groupCode(self, text):
        self.clear(*self._groupCode)
        self.send_text(text, *self._groupCode)

    def input_maxUserRegister(self, text):
        self.clear(*self._maxUserRegister)
        self.send_text(text, *self._maxUserRegister)

    def input_describeC(self, text):
        self.clear(*self._describeC)
        self.send_text(text, *self._describeC)

    def input_describeE(self, text):
        self.clear(*self._describeE)
        self.send_text(text, *self._describeE)

    def click_cancel(self):
        self.click(*self._cancel)

    def click_confirm(self):
        self.click(*self._confirm)

class RolePage(GroupManagementPage):

    def __init__(self,driver):
        GroupManagementPage.__init__(self,driver)

    def clickAddButton(self):
        self.click(*self._add)

class UserPage(GroupManagementPage):

    def __init__(self,driver):
        GroupManagementPage.__init__(self,driver)