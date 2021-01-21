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
        self._easIndexPage = EasIndexPage(self.login.driver)

    def boeBusinessApprove(self):

        self._easIndexPage.click_myWaitApprove()
        self._easIndexPage.click_moreButton()

        windowsList = self._easIndexPage.getWindowHandles()
        self._easIndexPage.switchToWin(windowsList[1])

        WebDriverWait(self._easIndexPage.driver, 5).until(
            EC.visibility_of_element_located(self._easIndexPage.getBoeNo()))

        self._easIndexPage.input_boeNo(self.boeNum)
        sleep(1)
        self._easIndexPage.click_boeNoSelectButton()
        self._easIndexPage.click_boeBusinessApprove()
        sleep(1)
        self._easIndexPage.click_boeBusinessTipConfirm()

        if self._easIndexPage.getToastBoxText() == '操作成功':
            content = '审批成功'
            self.login.driver.quit()
            return content
        else:
            content = '审批失败'
            self.login.driver.quit()
            return content




if __name__ == '__main__':
    a = BusinessApprove('hcGroup-BX2012210004')
    a.boeBusinessApprove()