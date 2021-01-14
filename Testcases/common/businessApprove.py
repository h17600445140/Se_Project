# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageClass.easIndexPageClass.easIndexPage import EasIndexPage
from Testcases.common.loginDepend import LoginDepend



class BusinessApprove():

    def __init__(self, boeNum):
        self.boeNum = boeNum
        self.login = LoginDepend('easHost', 'leader')
        self.easIndexPage = EasIndexPage(self.login.driver)

    def boeBusinessApprove(self):

        self.easIndexPage.click_myWaitApprove()
        self.easIndexPage.click_moreButton()

        windowsList = self.easIndexPage.getWindowHandles()
        self.easIndexPage.switchToWin(windowsList[1])

        WebDriverWait(self.easIndexPage.driver, 5).until(
            EC.visibility_of_element_located(self.easIndexPage.getBoeNo()))

        self.easIndexPage.input_boeNo(self.boeNum)
        sleep(1)
        self.easIndexPage.click_boeNoSelectButton()
        self.easIndexPage.click_boeBusinessApprove()
        sleep(1)
        self.easIndexPage.click_boeBusinessTipConfirm()

        if self.easIndexPage.getToastBoxText() == '操作成功':
            content = '审批成功'
            return content
        else:
            content = '审批失败'
            return content


if __name__ == '__main__':
    a = BusinessApprove('hcGroup-BX2012210004')
    a.boeBusinessApprove()