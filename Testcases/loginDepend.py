from time import sleep
from PageClass.loginPageClass.publicLoginPage import PublicLoginPage
from selenium import webdriver

from Util.util import get_urldict

class TestLoginDepend(object):

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.publicLoginPage = PublicLoginPage(self.driver)

    def test_publicLogin(self):
        self.publicLoginPage.goto_publicloginpage(get_urldict()['url']['host'])
        sleep(1)
        self.publicLoginPage.input_account("admin")
        self.publicLoginPage.input_password("zfs123456")
        sleep(1)
        self.publicLoginPage.click_loginbutton()
        sleep(2)
        self.publicLoginPage.get_into()
        sleep(2)
