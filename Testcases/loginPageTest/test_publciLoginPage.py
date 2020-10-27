from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageClass.loginPageClass.publicLoginPage import PublicLoginPage
import pytest
import allure

from Util.util import get_jsontestdata, get_datapath
import os

@allure.feature("登陆模块")
class TestPublicLoginPage(object):

    def setup_class(self):
        with allure.step("第一步，初始化"):
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(2)
            self.publicloginpage = PublicLoginPage(self.driver)

    # @pytest.mark.parametrize('account, password, cases',get_jsontestdata(get_datapath(os.path.dirname(__file__))))
    @allure.story("测试登陆时发生的四种场景")
    # @allure.title("登陆测试")
    @allure.severity('blocker')
    @allure.description("登陆成功 失败 成功")
    # @allure.testcase("http://www.baidu.com")
    # @allure.link("https://docs.qameta.io/allure/#_pytest")
    def test_login(self, json_testdata, env):
        allure.title(json_testdata[2])
        ''' 登录测试开始 '''
        self.publicloginpage.goto_publicloginpage(env['url']['host'])
        with allure.step("第三步，输入账号/密码"):
            self.publicloginpage.input_account(json_testdata[0])
            self.publicloginpage.input_password(json_testdata[1])
        self.publicloginpage.click_loginbutton()

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