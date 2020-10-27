from selenium.webdriver.common.by import By
from PageClass.basePage import BasePage


class PublicLoginPage(BasePage):

    __account_input = (By.ID, 'loginKey')
    __password_input = (By.ID, 'password')
    __login_button = (By.ID, 'login')
    getInto_button = (By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div[2]/p[2]')
    getMessage_box = (By.CLASS_NAME, 'el-message__content')
    accountInputError_box = (By.XPATH, '//*[@id="app"]/div/div[1]/div/form/div[1]/div/div')
    passwordInputError_box = (By.XPATH, '//*[@id="app"]/div/div[1]/div/form/div[2]/div/div')

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def goto_publicloginpage(self,url):
        self.driver.get(url)
        self.driver.maximize_window()

    def input_account(self, account):
        self.clear(*self.__account_input)
        self.send_text(account, *self.__account_input)

    def input_password(self, password):
        self.clear(*self.__password_input)
        self.send_text(password, *self.__password_input)

    def click_loginbutton(self):
        self.click(*self.__login_button)

    def get_into(self):
        self.click(*self.getInto_button)

    def get_errortext(self):
        return self.find_element(*self.getMessage_box).text

    def get_accounterrortext(self):
        return self.find_element(*self.accountInputError_box).text

    def get_passworderrortext(self):
        return self.find_element(*self.passwordInputError_box).text