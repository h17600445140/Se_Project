from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageClass.loginPageClass.publicLoginPage import PublicLoginPage
from Util.util import get_jsontestdata, get_datapath, get_urldict
from Util.util import get_logger

import pytest
import allure


@allure.feature("页面登陆模块")
class TestPublicLoginPage(object):

    def setup_class(self):
        self.logger = get_logger()
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(1)
        self.publicloginpage = PublicLoginPage(self.driver)
        self.publicloginpage.goto_publicloginpage(get_urldict()['url']['host'])
        self.logger.info("测试用户登录")

    def teardown_class(self):
        self.driver.quit()

    # @pytest.mark.parametrize('account, password, cases',get_jsontestdata(get_datapath(os.path.dirname(__file__))))
    @allure.story("测试登陆时发生的五种场景")
    @allure.severity('blocker')
    @allure.step("First Function")
    # @allure.description("--------------------测试登陆时不同场景--------------------")
    # @allure.testcase("http://www.baidu.com")
    # @allure.link("https://docs.qameta.io/allure/#_pytest")
    def test_login(self, json_testdata):
        ''' --------------------测试登陆时不同场景-------------------- '''
        allure.title(json_testdata[2])
        self.logger.error("-------------------------------------------------")
        with allure.step("第一步，登录页面初始化"):
            self.publicloginpage.driver.refresh()
            self.logger.info("页面刷新")
            print("页面刷新")
        with allure.step("第二步，输入账号/密码"):
            self.publicloginpage.input_account(json_testdata[0])
            self.logger.debug("输入账户为：{}".format(json_testdata[0]))
            self.publicloginpage.input_password(json_testdata[1])
            self.logger.debug("输入密码为：{}".format(json_testdata[1]))
        with allure.step("第三步，点击登录按钮"):
            self.publicloginpage.click_loginbutton()
            self.logger.debug("点击登录")
        with allure.step("第四步，判断断言信息"):

            if (json_testdata[2] == '账号密码不匹配') or (json_testdata[2] =='当前登录用户名或密码错误'):
                WebDriverWait(self.publicloginpage.driver, 1).until(
                    EC.visibility_of_element_located(self.publicloginpage.getMessage_box))
                msg = self.publicloginpage.get_errortext()
                assert (json_testdata[2] in msg)

            elif json_testdata[2] == '请输入账户名称':
                WebDriverWait(self.publicloginpage.driver, 1).until(
                    EC.text_to_be_present_in_element(self.publicloginpage.accountInputError_box,json_testdata[2]))
                msg = self.publicloginpage.get_accounterrortext()
                assert json_testdata[2] == msg

            elif json_testdata[2] == '请输入密码':
                WebDriverWait(self.publicloginpage.driver, 1).until(
                    EC.text_to_be_present_in_element(self.publicloginpage.passwordInputError_box,json_testdata[2]))
                msg = self.publicloginpage.get_passworderrortext()
                assert json_testdata[2] == msg

            elif json_testdata[2] == '登陆成功':
                WebDriverWait(self.publicloginpage.driver, 1).until(
                    EC.visibility_of_element_located(self.publicloginpage.getInto_button))
                self.publicloginpage.get_into()
                self.publicloginpage.driver.refresh()
                assert 1 == 1

if __name__ == '__main__':
    pytest.main(['-sv','test_publciLoginPage.py'])