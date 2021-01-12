# -*- coding:utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageClass.publicIndexPageClass.groupManagementPageClass import ManagementPageClass
from Testcases.common.loginDepend import LoginDepend



class TestManagementPageClass(object):

    def setup_class(self):
        self.publicLogin = LoginDepend('publicHost')
        # self.publicLogin.publicLogin('publicHost')
        self.managementPageClass = ManagementPageClass(self.publicLogin.driver)

    def teardown_class(self):
        self.managementPageClass.driver.quit()

    def test_addGroup(self, managementPageClass_testdata):
        WebDriverWait(self.managementPageClass.driver, 5).until(
            EC.visibility_of_element_located(self.managementPageClass.getGroupManagement()))

        self.managementPageClass.open_groupManagement()
        self.managementPageClass.open_management()
        self.managementPageClass.clickAddButton()
        self.managementPageClass.input_groupCname(managementPageClass_testdata["groupCname"])
        self.managementPageClass.input_groupEname(managementPageClass_testdata["groupEname"])
        self.managementPageClass.input_groupCode(managementPageClass_testdata["groupCode"])
        self.managementPageClass.input_maxUserRegister(managementPageClass_testdata["maxUserRegister"])
        self.managementPageClass.input_describeC(managementPageClass_testdata["describeC"])
        self.managementPageClass.input_describeE(managementPageClass_testdata["describeE"])
        self.managementPageClass.click_confirm()

        WebDriverWait(self.managementPageClass, 10).until(
            EC.text_to_be_present_in_element(self.managementPageClass.toastBox, '保存成功'))






