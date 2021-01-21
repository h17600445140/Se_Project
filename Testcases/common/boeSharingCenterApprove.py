# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageClass.boeApplyPageClass.comFeeApplyBoePage import ComFeeApplyBoePage
from PageClass.fscIndexPageClass.auditAdjustDirectorPage import AuditAdjustDirectorPage
from PageClass.fscIndexPageClass.myAuditListPage import MyAuditListPage
from Testcases.common.handleTimer import HandleTimer
from Testcases.common.loginDepend import LoginDepend



class SharingCenterApprove():

    def __init__(self, boeNum):
        self.login = LoginDepend('fscHost', 'finance')
        self.boeNum = boeNum
        self.myAuditListPage = MyAuditListPage(self.login.driver)
        self._auditAdjustDirectorPage = AuditAdjustDirectorPage(self.login.driver)

    def sharingCenterApproveChuShen(self):
        self.handleTimer = HandleTimer('共享中心', '共享从中台同步单据', self.login.driver)
        self.handleTimer.runTimer()

        self.myAuditListPage.click_taskHandle()
        sleep(1)
        self.myAuditListPage.click_auditAdjustDirector()

        sleep(1)
        self._auditAdjustDirectorPage.input_selectBoeNum(self.boeNum)
        self._auditAdjustDirectorPage.click_selectButton()
        self._auditAdjustDirectorPage.click_selectResult()
        self._auditAdjustDirectorPage.click_taskTakeToBack()
        sleep(1)
        self._auditAdjustDirectorPage.click_selectResult()
        self._auditAdjustDirectorPage.click_distributeToGroup()
        self._auditAdjustDirectorPage.click_selectGroup()
        self._auditAdjustDirectorPage.click_selectFirstGroup()
        self._auditAdjustDirectorPage.click_selectGroupSubmit()
        sleep(1)
        self._auditAdjustDirectorPage.click_selectResult()
        self._auditAdjustDirectorPage.click_distributeToStaff()
        self._auditAdjustDirectorPage.click_selectOperatorUser()
        self._auditAdjustDirectorPage.click_selectFirstOperatorUser()
        self._auditAdjustDirectorPage.click_selectOperatorUserSubmit()
        self._auditAdjustDirectorPage.click_taskHandle()

        WebDriverWait(self._auditAdjustDirectorPage.driver, 5).until(
            EC.visibility_of_element_located(self._auditAdjustDirectorPage.getAuditList()))
        self._auditAdjustDirectorPage.click_auditList()

        self.myAuditListPage.input_boeNumQuery(self.boeNum)
        self.myAuditListPage.click_boeNumQueryButton()
        self.myAuditListPage.getIntoBoe()

        # 待测试
        self.comFeeApplyBoePage = ComFeeApplyBoePage(self.login.driver)
        windowsList = self.comFeeApplyBoePage.getWindowHandles()
        self.comFeeApplyBoePage.switchToWin(windowsList[1])
        self.comFeeApplyBoePage.click_accountMessage()
        self.comFeeApplyBoePage.click_approveButton()
        sleep(3)
        windowsList = self.comFeeApplyBoePage.getWindowHandles()
        self.comFeeApplyBoePage.switchToWin(windowsList[0])

    def sharingCenterApproveFuShen(self):

        self.myAuditListPage.click_taskHandle()
        sleep(1)
        self.myAuditListPage.click_auditAdjustDirector()
        sleep(1)
        self._auditAdjustDirectorPage.input_selectBoeNum(self.boeNum)
        self._auditAdjustDirectorPage.click_selectButton()
        sleep(1)
        flag = self._auditAdjustDirectorPage.elementExistIsOrNot(*self._auditAdjustDirectorPage.getSelectResult())
        sleep(1)
        print('第一次flag:{}'.format(flag))
        while True:
            if flag == True:
                break
            else:
                self.handleTimer = HandleTimer('共享中心', '生成任务', self.login.driver)
                self.handleTimer.runTimer()
                self._auditAdjustDirectorPage.input_selectBoeNum(self.boeNum)
                sleep(1)
                self._auditAdjustDirectorPage.click_selectButton()
                sleep(1)
                flag = self._auditAdjustDirectorPage.elementExistIsOrNot(*self._auditAdjustDirectorPage.getSelectResult())

        self._auditAdjustDirectorPage.click_selectResult()
        self._auditAdjustDirectorPage.click_taskTakeToBack()
        sleep(1)
        self._auditAdjustDirectorPage.click_selectResult()
        self._auditAdjustDirectorPage.click_distributeToGroup()
        self._auditAdjustDirectorPage.click_selectGroup()
        self._auditAdjustDirectorPage.click_selectFirstGroup()
        self._auditAdjustDirectorPage.click_selectGroupSubmit()
        sleep(1)
        self._auditAdjustDirectorPage.click_selectResult()
        self._auditAdjustDirectorPage.click_distributeToStaff()
        self._auditAdjustDirectorPage.click_selectOperatorUser()
        self._auditAdjustDirectorPage.click_selectFirstOperatorUser()
        self._auditAdjustDirectorPage.click_selectOperatorUserSubmit()
        self._auditAdjustDirectorPage.click_taskHandle()

        WebDriverWait(self._auditAdjustDirectorPage.driver, 5).until(
            EC.visibility_of_element_located(self._auditAdjustDirectorPage.getAuditList()))
        self._auditAdjustDirectorPage.click_auditList()

        self.myAuditListPage.input_boeNumQuery(self.boeNum)
        self.myAuditListPage.click_boeNumQueryButton()
        self.myAuditListPage.getIntoBoe()

        # 待测试
        self.comFeeApplyBoePage = ComFeeApplyBoePage(self.login.driver)
        windowsList = self.comFeeApplyBoePage.getWindowHandles()
        self.comFeeApplyBoePage.switchToWin(windowsList[1])
        self.comFeeApplyBoePage.click_accountMessage()
        self.comFeeApplyBoePage.click_approveButton()
        sleep(3)
        windowsList = self.comFeeApplyBoePage.getWindowHandles()
        self.comFeeApplyBoePage.switchToWin(windowsList[0])

        self.login.driver.quit()

if __name__ == '__main__':
    a = SharingCenterApprove('hcGroup-BX210108158')
    a.sharingCenterApproveChuShen()
    a.sharingCenterApproveFuShen()

