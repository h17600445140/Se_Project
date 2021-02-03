# -*- coding:utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageClass.loginPageClass.loginPage import LoginPage
from PageClass.loginPageClass.publicLoginPage import PublicLoginPage

from Util import config, driverFactory, logger



class LoginDepend(object):

    def __init__(self, host, user):
        self.driver = driverFactory.get_driver("chrome")
        if host in ['baseHost', 'easHost', 'fscHost', 'cmsHost', 'basHost', 'ledgerHost']:
            self.login = LoginPage(self.driver)
            self._login(host, user)

        elif host == 'publicHost':
            self.publicLoginPage = PublicLoginPage(self.driver)
            self._publicLogin('publicHost')

    def _publicLogin(self, host):
        self.publicLoginPage.goto_publicloginpage(config.getUrlDict()['url'][host])
        self.driver.implicitly_wait(1)
        self.publicLoginPage.input_account(config.getUrlDict()['user']['account'])
        self.publicLoginPage.input_password(config.getUrlDict()['user']['password'])
        self.publicLoginPage.click_loginbutton()
        try:
            WebDriverWait(self.publicLoginPage.driver, 5).until(
                EC.visibility_of_element_located(self.publicLoginPage.getIntoButton()))
        except:
            pass
        else:
            self.publicLoginPage.get_into()

    def _login(self, host, user):
        self.login.goto_loginpage(config.getUrlDict()['url'][host])
        self.driver.implicitly_wait(1)
        self.login.input_account(config.getUrlDict()[user]['account'])
        self.login.input_password(config.getUrlDict()[user]['password'])
        self.login.click_loginbutton()
        try:
            WebDriverWait(self.login.driver, 3).until(
                EC.visibility_of_element_located(self.login.getIntoButton()))
        except:
            pass
        else:
            self.login.get_into()
        logger.info('成功登录界面：{}'.format(host))

