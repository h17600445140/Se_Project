from selenium.webdriver.common.by import By
from PageClass.basePage import BasePage


class PublicLoginPage(BasePage):

    account_input = (By.ID, 'loginKey')
    password_input = (By.ID, 'password')
    login_button = (By.ID, 'login')
    getInto_button = (By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div[2]/p[2]')

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def goto_publicloginpage(self,url):
        self.driver.get(url)
        self.driver.maximize_window()

    def input_account(self, account):
        self.clear(*self.account_input)
        self.send_text(account, *self.account_input)

    def input_password(self, password):
        self.clear(*self.password_input)
        self.send_text(password, *self.password_input)

    def click_loginbutton(self):
        self.click(*self.login_button)

    def get_into(self):
        self.click(*self.getInto_button)