# -*- coding:utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageClass.loginPageClass.publicLoginPage import PublicLoginPage
from Util import driverFactory
from Util.util import get_logger, getNowTime

from Util.util import getPicturePath
from Util import config,logger

import pytest
import allure



@allure.feature("页面登陆模块")
class TestPublicLoginPage(object):

    def setup_class(self):
        self.driver = driverFactory.get_driver('chrome')
        self.publicloginpage = PublicLoginPage(self.driver)
        self.publicloginpage.goto_publicloginpage(config.getUrlDict()['url']['publicHost'])
        logger.info("链接地址为：{}".format(config.getUrlDict()['url']['publicHost']))
        self.driver.implicitly_wait(1)
        logger.info("测试用户登录场景")

    def teardown_class(self):
        self.driver.quit()

    # @pytest.mark.parametrize('account, password, cases',get_jsontestdata(get_datapath(os.path.dirname(__file__))))
    @allure.story("测试登陆时发生的五种场景")
    # @allure.severity('blocker')
    @allure.step("First Function")
    # @allure.description("--------------------测试登陆时不同场景--------------------")
    # @allure.testcase("http://www.baidu.com")
    # @allure.link("https://docs.qameta.io/allure/#_pytest")
    @allure.severity("minor")
    def test_login(self, publciLoginPage_testdata):
        ''' --------------------测试登陆时不同场景-------------------- '''

        logger.info("测试用例名字为：{}".format(publciLoginPage_testdata["casename"]))

        allure.title(publciLoginPage_testdata["casename"])
        with allure.step("第一步，登录页面初始化"):
            self.publicloginpage.refresh()

        with allure.step("第二步，输入账号/密码"):
            self.publicloginpage.input_account(publciLoginPage_testdata["account"])
            logger.debug("输入账户为：{}".format(publciLoginPage_testdata["account"]))
            self.publicloginpage.input_password(publciLoginPage_testdata["password"])
            logger.debug("输入密码为：{}".format(publciLoginPage_testdata["password"]))

        with allure.step("第三步，点击登录按钮"):
            self.publicloginpage.click_loginbutton()

        with allure.step("第四步，判断断言信息"):

            try:

                if (publciLoginPage_testdata["casename"] == '账号密码不匹配') or (publciLoginPage_testdata["casename"] =='当前登录用户名或密码错误'):
                    WebDriverWait(self.publicloginpage.driver, 5).until(
                        EC.visibility_of_element_located(self.publicloginpage.getMessageBox()))
                    msg = self.publicloginpage.get_errortext()
                    assert (publciLoginPage_testdata["casename"] in msg)

                elif publciLoginPage_testdata["casename"] == '请输入账户名称':
                    WebDriverWait(self.publicloginpage.driver, 5).until(
                        EC.text_to_be_present_in_element(self.publicloginpage.getAccountInputErrorBox(),publciLoginPage_testdata["casename"]))
                    msg = self.publicloginpage.get_accounterrortext()
                    assert publciLoginPage_testdata["casename"] == msg

                elif publciLoginPage_testdata["casename"] == '请输入密码':
                    WebDriverWait(self.publicloginpage.driver, 5).until(
                        EC.text_to_be_present_in_element(self.publicloginpage.getPasswordInputErrorBox(),publciLoginPage_testdata["casename"]))
                    msg = self.publicloginpage.get_passworderrortext()
                    assert publciLoginPage_testdata["casename"] == msg

                elif publciLoginPage_testdata["casename"] == '登陆成功':
                    WebDriverWait(self.publicloginpage.driver, 5).until(
                        EC.visibility_of_element_located(self.publicloginpage.getIntoButton()))
                    self.publicloginpage.get_into()
                    self.publicloginpage.driver.refresh()
                    assert 1 == 1

            except Exception as e:

                logger.error("出现异常，异常信息为：{}".format(type(e)))
                code = 'wrong'
                timeNow = getNowTime()
                self.publicloginpage.screenshot(code, timeNow)
                allure.attach.file(getPicturePath(code,timeNow),name=timeNow + code + "screenshot",
                                   attachment_type=allure.attachment_type.PNG)
                assert 1 == 0
            else:

                logger.info("测试用例执行成功")
                code = 'success'
                timeNow = getNowTime()
                self.publicloginpage.screenshot(code, timeNow)
                allure.attach.file(getPicturePath(code, timeNow), name=timeNow + code + "screenshot",
                                   attachment_type=allure.attachment_type.PNG)



if __name__ == '__main__':
    # pytest.main(['-sv','test_publciLoginPage.py'])
    print(getPicturePath('success', getNowTime()))