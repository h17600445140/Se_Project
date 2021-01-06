# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from PageClass.basePage import BasePage


class GroupManagementPageClass(BasePage):

    groupManagement = (By.XPATH, '//*[@id="app"]/section/section/aside/div/div[2]/div[1]/div/ul/li[1]/div/span')
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
        self.click(*self.groupManagement)

    def open_management(self):
        self.click(*self._management)

    def open_role(self):
        self.click(*self._role)

    def open_user(self):
        self.click(*self._user)

class ManagementPageClass(GroupManagementPageClass):

    __groupCname = (By.ID, 'form_name_zh-CN')
    __groupEname = (By.ID, 'form_name_en-US')
    __groupCode = (By.ID, 'form_codeNo')
    __maxUserRegister = (By.ID, 'form_encryptMaxAccount')
    __describeC = (By.ID, 'form_remark_zh-CN')
    __describeE = (By.ID, 'form_remark_en-US')

    __cancel = (By.XPATH, '//*[@id="form"]/div[8]/div/button[1]/span')
    __confirm = (By.XPATH, '//*[@id="form"]/div[8]/div/button[2]/span')

    groupCname_errorBox = (By.XPATH, '//*[@id="form"]/div[1]/div/div[2]')
    groupCode_errorBox = (By.XPATH, '//*[@id="form"]/div[3]/div/div[2]')
    maxUserRegister_errorBox = (By.XPATH, '//*[@id="form"]/div[4]/div/div[2]')

    def __init__(self,driver):
        GroupManagementPageClass.__init__(self,driver)

    def clickAddButton(self):
        self.click(*self._add)

    def clickDeleteButton(self):
        self.click(*self._delete)

    def clickEnableButton(self):
        self.click(*self._enable)

    def clickDisableButton(self):
        self.click(*self._disable)

    def input_groupCname(self, text):
        self.clear(*self.__groupCname)
        self.send_text(text, *self.__groupCname)

    def input_groupEname(self, text):
        self.clear(*self.__groupEname)
        self.send_text(text, *self.__groupEname)

    def input_groupCode(self, text):
        self.clear(*self.__groupCode)
        self.send_text(text, *self.__groupCode)

    def input_maxUserRegister(self, text):
        self.clear(*self.__maxUserRegister)
        self.send_text(text, *self.__maxUserRegister)

    def input_describeC(self, text):
        self.clear(*self.__describeC)
        self.send_text(text, *self.__describeC)

    def input_describeE(self, text):
        self.clear(*self.__describeE)
        self.send_text(text, *self.__describeE)

    def click_cancel(self):
        self.click(*self.__cancel)

    def click_confirm(self):
        self.click(*self.__confirm)

class RolePageClass(GroupManagementPageClass):

    def __init__(self,driver):
        GroupManagementPageClass.__init__(self,driver)

    def clickAddButton(self):
        self.click(*self._add)

class UserPageClass(GroupManagementPageClass):

    def __init__(self,driver):
        GroupManagementPageClass.__init__(self,driver)