from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

from PageClass.publicIndexPageClass.groupManagementPageClass import ManagementPageClass
from Testcases.loginDepend import TestLoginDepend

from Util.util import get_logger



class TestManagementPageClass(object):

    def setup_class(self):
        self.logger = get_logger()
        self.publicLogin = TestLoginDepend()
        self.managementPageClass = ManagementPageClass(self.publicLogin.driver)

    def teardown_class(self):
        # self.driver.quit()
        pass

    def test_addGroup(self, managementPageClass_testdata):

        self.managementPageClass.open_groupManagement()
        sleep(1)
        self.managementPageClass.open_management()
        sleep(1)
        self.managementPageClass.clickAddButton()
        sleep(1)
        self.managementPageClass.input_groupCname(managementPageClass_testdata["groupCname"])
        self.managementPageClass.input_groupEname(managementPageClass_testdata["groupEname"])
        self.managementPageClass.input_groupCode(managementPageClass_testdata["groupCode"])
        self.managementPageClass.input_maxUserRegister(managementPageClass_testdata["maxUserRegister"])
        self.managementPageClass.input_describeC(managementPageClass_testdata["describeC"])
        self.managementPageClass.input_describeE(managementPageClass_testdata["describeE"])
        self.managementPageClass.click_confirm()

        WebDriverWait(self.managementPageClass, 5).until(
            EC.text_to_be_present_in_element(self.managementPageClass.successBox, '保存成功'))






