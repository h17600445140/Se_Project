# -*- coding:utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageClass.publicIndexPageClass.groupManagementPage import ManagementPage
from Testcases.common.loginDepend import LoginDepend



class TestManagementPage(object):

    def setup_class(self):
        self.publicLogin = LoginDepend('publicHost', 'user')
        # self.publicLogin.publicLogin('publicHost')
        self.managementPage = ManagementPage(self.publicLogin.driver)

    def teardown_class(self):
        self.managementPage.driver.quit()

    def test_addGroup(self, managementPage_testdata):
        WebDriverWait(self.managementPage.driver, 5).until(
            EC.visibility_of_element_located(self.managementPage.getGroupManagement()))

        self.managementPage.open_groupManagement()
        self.managementPage.open_management()
        self.managementPage.clickAddButton()
        self.managementPage.input_groupCname(managementPage_testdata["groupCname"])
        self.managementPage.input_groupEname(managementPage_testdata["groupEname"])
        self.managementPage.input_groupCode(managementPage_testdata["groupCode"])
        self.managementPage.input_maxUserRegister(managementPage_testdata["maxUserRegister"])
        self.managementPage.input_describeC(managementPage_testdata["describeC"])
        self.managementPage.input_describeE(managementPage_testdata["describeE"])
        self.managementPage.click_confirm()

        WebDriverWait(self.managementPage.driver, 10).until(
            EC.text_to_be_present_in_element(self.managementPage.toastBox, '保存成功'))