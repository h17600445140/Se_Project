from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageClass.loginPageClass.publicLoginPage import PublicLoginPage

import pytest

class TestPublicLoginPage(object):

    login_data = [
        ('admin', 'zfs123456')
    ]

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.publicloginpage = PublicLoginPage(self.driver)

    @pytest.mark.parametrize('account,password', login_data)
    def test_login(self, account, password, env):
        self.publicloginpage.goto_publicloginpage(env['url']['host'])
        self.publicloginpage.input_account(account)
        self.publicloginpage.input_password(password)
        self.publicloginpage.click_loginbutton()
        if WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(self.publicloginpage.getInto_button)):
            self.publicloginpage.get_into()
        else:
            print("错误")

if __name__ == '__main__':
    pytest.main(['-sv','test_publciLoginPage.py'])