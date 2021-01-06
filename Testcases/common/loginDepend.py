# -*- coding:utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageClass.loginPageClass.publicLoginPage import PublicLoginPage
from selenium import webdriver

from Util import config



class LoginDepend(object):

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.publicLoginPage = PublicLoginPage(self.driver)

    def publicLogin(self):
        self.publicLoginPage.goto_publicloginpage(config.getUrlDict()['url']['host'])
        self.driver.implicitly_wait(1)
        self.publicLoginPage.input_account(config.getUrlDict()['url']['account'])
        self.publicLoginPage.input_password(config.getUrlDict()['url']['password'])
        self.publicLoginPage.click_loginbutton()
        WebDriverWait(self.publicLoginPage.driver, 10).until(
            EC.visibility_of_element_located(self.publicLoginPage.getInto_button))
        self.publicLoginPage.get_into()

