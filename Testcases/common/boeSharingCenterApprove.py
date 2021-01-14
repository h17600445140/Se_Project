# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Testcases.common.loginDepend import LoginDepend



class SharingCenterApprove():

    def __init__(self):
        self.login = LoginDepend('fscHost', 'finance')
        self.login.driver.get("http://192.168.0.200/ip/timerManage")
        self.login.driver.back()

    def sharingCenterApprove(self):
        pass


if __name__ == '__main__':
    a = SharingCenterApprove()

