# -*- coding:utf-8 -*-
from PageClass.common.boeCommon import BoeCommon
from PageClass.fscIndexPageClass.auditAdjustDirectorPage import AuditAdjustDirectorPage
from PageClass.fscIndexPageClass.myAuditListPage import MyAuditListPage
from Testcases.common.handleTimer import HandleTimer
from Testcases.common.loginDepend import LoginDepend
from Util import logger, config


class SharingCenterApprove():

    def __init__(self, boeNum):
        self.login = LoginDepend('fscHost', 'finance')
        self.boeNum = boeNum
        self._myAuditListPage = MyAuditListPage(self.login.driver)
        self._auditAdjustDirectorPage = AuditAdjustDirectorPage(self.login.driver)
        self._boeCommon = BoeCommon(self.login.driver)

    def sharingCenterApproveChuShen(self):

        self._handleTimer = HandleTimer('共享中心', '共享从中台同步单据', self.login.driver)
        self._handleTimer.runTimer()

        self._myAuditListPage.gotoAuditAdjustDirectorPage()
        self._auditAdjustDirectorPage.input_selectBoeNum(self.boeNum)
        self._auditAdjustDirectorPage.click_selectButton()

        try:
            self._auditAdjustDirectorPage.click_selectResult()
        except:
            logger.info('没有找到单据，{}'.format(self.boeNum))
            logger.info('----- Try again -----')
            self._handleTimer = HandleTimer('共享中心', '共享从中台同步单据', self.login.driver)
            self._handleTimer.runTimer()
            self._auditAdjustDirectorPage.input_selectBoeNum(self.boeNum)
            self._auditAdjustDirectorPage.click_selectButton()
            self._auditAdjustDirectorPage.click_selectResult()

        self._auditAdjustDirectorPage.click_taskTakeToBack()
        self._auditAdjustDirectorPage.click_selectResult()

        # 分配到组
        try:
            self._auditAdjustDirectorPage.choiceGroup(config.getUrlDict()['Approval']['approvalGroupC'])
        except:
            self._auditAdjustDirectorPage.click_selectResult()
            self._auditAdjustDirectorPage.choiceGroup(config.getUrlDict()['Approval']['approvalGroupC'])

        # 分配到人
        self._auditAdjustDirectorPage.click_selectResult()
        try:
            self._auditAdjustDirectorPage.choiceOperatorUser(config.getUrlDict()['Approval']['approvalUserC'])
        except:
            self._auditAdjustDirectorPage.click_selectResult()
            self._auditAdjustDirectorPage.choiceOperatorUser(config.getUrlDict()['Approval']['approvalUserC'])

        self._auditAdjustDirectorPage.gotoAuditList()
        self._myAuditListPage.input_boeNumQuery(self.boeNum)
        self._myAuditListPage.click_boeNumQueryButton()

        self._myAuditListPage.getIntoBoe()
        self._boeCommon.switchWindow()

        self._boeCommon.click_accountMessage()
        self._boeCommon.click_approveButton()
        self._boeCommon.switchWindow()

    def sharingCenterApproveFuShen(self):

        self._myAuditListPage.gotoAuditAdjustDirectorPage()
        self._auditAdjustDirectorPage.input_selectBoeNum(self.boeNum)
        self._auditAdjustDirectorPage.click_selectButton()

        flag = self._auditAdjustDirectorPage.elementExistIsOrNot(*self._auditAdjustDirectorPage.getSelectResult())
        num = 0
        while True:
            if flag == True:
                break
            else:
                self._handleTimer = HandleTimer('共享中心', '生成任务', self.login.driver)
                self._handleTimer.runTimer()
                self._auditAdjustDirectorPage.input_selectBoeNum(self.boeNum)
                self._auditAdjustDirectorPage.click_selectButton()
                flag = self._auditAdjustDirectorPage.elementExistIsOrNot(*self._auditAdjustDirectorPage.getSelectResult())
            if num == 20:
                break
            else:
                num = num + 1

        self._auditAdjustDirectorPage.click_selectResult()
        self._auditAdjustDirectorPage.click_taskTakeToBack()
        self._auditAdjustDirectorPage.click_selectResult()

        # 分配到组
        try:
            self._auditAdjustDirectorPage.choiceGroup(config.getUrlDict()['Approval']['approvalGroupF'])
        except:
            self._auditAdjustDirectorPage.click_selectResult()
            self._auditAdjustDirectorPage.choiceGroup(config.getUrlDict()['Approval']['approvalGroupF'])

        self._auditAdjustDirectorPage.click_selectResult()

        # 分配到人
        try:
            self._auditAdjustDirectorPage.choiceOperatorUser(config.getUrlDict()['Approval']['approvalUserF'])
        except:
            self._auditAdjustDirectorPage.click_selectResult()
            self._auditAdjustDirectorPage.choiceOperatorUser(config.getUrlDict()['Approval']['approvalUserF'])

        self._auditAdjustDirectorPage.gotoAuditList()
        self._myAuditListPage.input_boeNumQuery(self.boeNum)
        self._myAuditListPage.click_boeNumQueryButton()

        self._myAuditListPage.getIntoBoe()
        self._boeCommon.switchWindow()

        self._boeCommon.click_accountMessage()
        self._boeCommon.click_approveButton()
        self._boeCommon.switchWindow()

        self.login.driver.quit()

if __name__ == '__main__':
    a = SharingCenterApprove('hcGroup-BX210125101')
    a.sharingCenterApproveChuShen()
    a.sharingCenterApproveFuShen()

