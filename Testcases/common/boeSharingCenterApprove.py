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

    def sharingCenterApproveChuShen(self):
        self.handleTimer = HandleTimer('共享中心', '共享从中台同步数据', self.login.driver)
        self.handleTimer.runTimer()

        self.myAuditListPage = MyAuditListPage(self.login.driver)
        self.myAuditListPage.click_taskHandle()
        sleep(1)
        self.myAuditListPage.click_auditAdjustDirector()

        sleep(1)
        self.auditAdjustDirectorPage = AuditAdjustDirectorPage(self.login.driver)
        self.auditAdjustDirectorPage.input_selectBoeNum(self.boeNum)
        self.auditAdjustDirectorPage.click_selectButton()
        self.auditAdjustDirectorPage.click_selectResult()
        self.auditAdjustDirectorPage.click_taskTakeToBack()
        sleep(1)
        self.auditAdjustDirectorPage.click_selectResult()
        self.auditAdjustDirectorPage.click_distributeToGroup()
        self.auditAdjustDirectorPage.click_selectGroup()
        self.auditAdjustDirectorPage.click_selectFirstGroup()
        self.auditAdjustDirectorPage.click_selectGroupSubmit()
        sleep(1)
        self.auditAdjustDirectorPage.click_selectResult()
        self.auditAdjustDirectorPage.click_distributeToStaff()
        self.auditAdjustDirectorPage.click_selectOperatorUser()
        self.auditAdjustDirectorPage.click_selectFirstOperatorUser()
        self.auditAdjustDirectorPage.click_selectOperatorUserSubmit()
        self.auditAdjustDirectorPage.click_taskHandle()
        sleep(1)
        self.auditAdjustDirectorPage.click_auditList()

        self.myAuditListPage.input_boeNumQuery(self.boeNum)
        self.myAuditListPage.click_boeNumQueryButton()
        self.myAuditListPage.getIntoBoe()

        # 待测试
        self.comFeeApplyBoePage = ComFeeApplyBoePage(self.login.driver)
        windowsList = self.comFeeApplyBoePage.getWindowHandles()
        self.comFeeApplyBoePage.switchToWin(windowsList[1])
        self.comFeeApplyBoePage.click_accountMessage()
        self.comFeeApplyBoePage.click_approveButton()
        windowsList = self.comFeeApplyBoePage.getWindowHandles()
        self.comFeeApplyBoePage.switchToWin(windowsList[0])

    def sharingCenterApproveFShen(self):
        pass





if __name__ == '__main__':
    a = SharingCenterApprove('hcGroup-BX210114146')
    a.sharingCenterApproveChuShen()

