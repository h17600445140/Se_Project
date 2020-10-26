from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageClass.loginPageClass.publicLoginPage import PublicLoginPage

import pytest

class TestPublicLoginPage(object):

    login_data = [
        ('hctest', '123456', '账号密码不匹配'),
        ('admin', 'zfs123456', '登陆成功')
    ]

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(1)
        self.publicloginpage = PublicLoginPage(self.driver)

    def test_login(self, json_testdata, env):
        self.publicloginpage.goto_publicloginpage(env['url']['host'])
        self.publicloginpage.input_account(json_testdata[0])
        self.publicloginpage.input_password(json_testdata[1])
        self.publicloginpage.click_loginbutton()

        if json_testdata[2] == '账号密码不匹配':
            WebDriverWait(self.publicloginpage.driver, 1).until(EC.visibility_of_element_located(self.publicloginpage.getMessage_box))
            msg = self.publicloginpage.get_errortext()
            assert msg == "账号密码不匹配"
        elif json_testdata[2] == '登陆成功':
            WebDriverWait(self.publicloginpage.driver, 1).until(EC.visibility_of_element_located(self.publicloginpage.getInto_button))
            self.publicloginpage.get_into()
            self.publicloginpage.driver.refresh()
            assert 1 == 1

if __name__ == '__main__':
    pytest.main(['-sv','test_publciLoginPage.py'])