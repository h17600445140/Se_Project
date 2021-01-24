# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from PageClass.basePage import BasePage
from Util import logger



class LoginPage(BasePage):

    _accountInput = (By.ID, 'loginKey')
    _passwordInput = (By.ID, 'password')
    _loginButton = (By.ID, 'login')
    _IntoButton = (By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div[2]/p[2]')

    _MessageBox = (By.CLASS_NAME, 'el-message__content')
    _accountInputErrorBox = (By.XPATH, '//*[@id="app"]/div/div[1]/div/form/div[1]/div/div')
    _passwordInputErrorBox = (By.XPATH, '//*[@id="app"]/div/div[1]/div/form/div[2]/div/div')

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def goto_loginpage(self,url):
        self.driver.get(url)
        logger.info("请求链接，链接地址为：{}".format(url))
        self.driver.maximize_window()

    def input_account(self, account):
        self.clear(*self._accountInput)
        self.send_text(account, *self._accountInput)
        logger.debug("输入账户，账户为：{}".format(account))

    def input_password(self, password):
        self.clear(*self._passwordInput)
        self.send_text(password, *self._passwordInput)
        logger.debug("输入密码，密码为：{}".format(password))

    def click_loginbutton(self):
        self.click(*self._loginButton)
        logger.info("点击登录按钮")

    def get_into(self):
        self.click(*self._IntoButton)

    def get_errortext(self):
        return self.find_element(*self._MessageBox).text

    def get_accounterrortext(self):
        return self.find_element(*self._accountInputErrorBox).text

    def get_passworderrortext(self):
        return self.find_element(*self._passwordInputErrorBox).text

    def getMessageBox(self):
        return self._MessageBox

    def getAccountInputErrorBox(self):
        return self._accountInputErrorBox

    def getPasswordInputErrorBox(self):
        return self._passwordInputErrorBox

    def getIntoButton(self):
        return self._IntoButton