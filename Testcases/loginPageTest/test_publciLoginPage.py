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

    getMessage_box = (By.CLASS_NAME, 'el-message__content')

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(1)
        self.publicloginpage = PublicLoginPage(self.driver)

    @pytest.mark.parametrize('account,password,casename', login_data)
    def test_login(self, account, password, casename, env):
        self.publicloginpage.goto_publicloginpage(env['url']['host'])
        self.publicloginpage.input_account(account)
        self.publicloginpage.input_password(password)
        self.publicloginpage.click_loginbutton()

        if casename == '账号密码不匹配':
            WebDriverWait(self.publicloginpage.driver, 1).until(EC.visibility_of_element_located(self.getMessage_box))
            msg = self.publicloginpage.get_errortext()
            assert msg == "账号密码不匹配"
        elif casename == '登陆成功':
            WebDriverWait(self.publicloginpage.driver, 1).until(EC.visibility_of_element_located(self.publicloginpage.getInto_button))
            self.publicloginpage.get_into()
            assert 1 == 1

if __name__ == '__main__':
    pytest.main(['-sv','test_publciLoginPage.py'])