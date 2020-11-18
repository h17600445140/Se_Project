from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageClass.publicIndexPageClass.groupManagementPageClass import ManagementPageClass
from Testcases.loginDepend import TestLoginDepend

from Util.util import get_logger



class TestManagementPageClass(object):

    def setup_class(self):
        self.logger = get_logger()
        self.publicLogin = TestLoginDepend()
        self.managementPageClass = ManagementPageClass(self.publicLogin.driver)

    def teardown_class(self):
        self.managementPageClass.driver.quit()

    def test_addGroup(self, managementPageClass_testdata):
        WebDriverWait(self.managementPageClass.driver, 2).until(
            EC.visibility_of_element_located(self.managementPageClass.groupManagement))

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

        WebDriverWait(self.managementPageClass, 1).until(
            EC.text_to_be_present_in_element(self.managementPageClass.toastBox, '保存成功'))






