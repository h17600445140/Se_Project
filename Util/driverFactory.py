# -*- coding:utf-8 -*-
"""

author      :   huangchao
fileName    :   driverFactory.py

"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

class Browser():

    driver = None

    def __init__(self):
        pass


    def getDriver(self):
        return self.driver


class Chrome(Browser):

    def __init__(self, system):
        super(Browser).__init__()

        if system == "windows":
            self.chrome_options = Options()
            self.chrome_options.add_argument('User-Agent={}'.format(UserAgent().chrome))
            self.driver = webdriver.Chrome(options=self.chrome_options)
        elif system == "linux":
            self.chrome_options = Options()
            self.chrome_options.add_argument('--no-sandbox')
            self.chrome_options.add_argument('--disable-dev-shm-usage')
            self.chrome_options.add_argument('--headless')
            self.chrome_options.add_argument('User-Agent={}'.format(UserAgent().chrome))
            self.driver = webdriver.Chrome(options=self.chrome_options)


class Firefox(Browser):

    def __init__(self, system):
        super(Browser).__init__()
        if system == "windows":
            self.driver = webdriver.Firefox()


class DriverFactory():

    def get_driver(self, browser):
        if browser == "chrome":
            return Chrome("windows").getDriver()
        elif browser == "firefox":
            return Firefox("windows").getDriver()
        else:
            raise Exception("please input 'chrome' or 'firefox'")


driverFactory = DriverFactory()

if __name__ == '__main__':

    driver = DriverFactory().get_driver('chrome')
    print(driver)
    driver.get("https://www.baidu.com")
    driver.quit()







