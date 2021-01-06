# -*- coding:utf-8 -*-
from selenium import webdriver


class Browser():

    driver = None

    def __init__(self):
        pass


    def getDriver(self):
        return self.driver


class Chrome(Browser):

    def __init__(self):
        super(Browser).__init__()
        self.driver = webdriver.Chrome()


class Firefox(Browser):

    def __init__(self):
        super(Browser).__init__()
        self.driver = webdriver.Firefox()


class DriverFactory():

    def get_driver(self, browser):
        if browser == "chrome":
            return Chrome().getDriver()
        elif browser == "firefox":
            return Firefox().getDriver()
        else:
            raise Exception("please input 'chrome' or 'firefox'")


driverFactory = DriverFactory()

if __name__ == '__main__':

    driver = DriverFactory().get_driver('chrome')
    print(driver)
    driver.get("https://www.baidu.com")
    driver.quit()







