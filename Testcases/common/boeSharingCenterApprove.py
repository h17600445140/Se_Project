# -*- coding:utf-8 -*-
from time import sleep

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

    def sharingCenterApproveChuShen(self, modify=False, **kwargs):

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
            sleep(1)
            self._auditAdjustDirectorPage.click_selectResult()
            sleep(1)
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

        try:
            self._myAuditListPage.getIntoBoe()
        except:
            sleep(1)
            self._myAuditListPage.getIntoBoe()
        self._boeCommon.switchWindow()

        parameterList = [i for i in kwargs.keys()]
        logger.info('参数列表为：{}'.format(parameterList))

        if modify == True:

            sleep(3)
            if 'checkCode' in parameterList:
                self._boeCommon.input_dtosCheckCode(kwargs['checkCode'])

            if 'invoiceTypeCode' in parameterList:
                self._boeCommon.input_dtosInvoiceTypeCode(kwargs['invoiceTypeCode'])

            if 'invoiceNo' in parameterList:
                self._boeCommon.input_dtosInvoiceNo(kwargs['invoiceNo'])

            if 'invoiceCode' in parameterList:
                self._boeCommon.input_dtosInvoiceCode(kwargs['invoiceCode'])

            if 'invoiceDate' in parameterList:
                self._boeCommon.input_dtosInvoiceDate(kwargs['invoiceDate'])

            if 'invoiceFee' in parameterList:
                self._boeCommon.input_dtosInvoiceFee(kwargs['invoiceFee'])

            if 'invoiceTax' in parameterList:
                self._boeCommon.input_dtosInvoiceTax(kwargs['invoiceTax'])

            if 'invoiceRemark' in parameterList:
                self._boeCommon.input_dtosInvoiceRemark(kwargs['invoiceRemark'])

            self._boeCommon.click_saveButton()

        self._boeCommon.click_accountMessage()
        self._boeCommon.click_approveButton()

        try:
            if self._boeCommon.getToastBoxText() != '审批成功':
                logger.info('弹窗信息为：{}'.format(self._boeCommon.getToastBoxText()))
                raise Exception('审批不成功')
            else:
                logger.info('弹窗信息为：{}'.format(self._boeCommon.getToastBoxText()))
                logger.info('单据财务审批成功')
        except:
            sleep(1)
            if self._boeCommon.getToastBoxText() != '审批成功':
                logger.info('弹窗信息为：{}'.format(self._boeCommon.getToastBoxText()))
                try:
                    logger.error(self._boeCommon.getBoxMessage())
                except:
                    pass
                finally:
                    raise Exception('审批不成功')
            else:
                logger.info('弹窗信息为：{}'.format(self._boeCommon.getToastBoxText()))
                logger.info('单据财务审批成功')

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
            if num == 50:
                break
            else:
                num = num + 1

        sleep(0.5)
        self._auditAdjustDirectorPage.click_selectResult()
        sleep(0.5)
        self._auditAdjustDirectorPage.click_taskTakeToBack()
        sleep(0.5)
        self._auditAdjustDirectorPage.click_selectResult()

        sleep(1)
        # 分配到组
        try:
            self._auditAdjustDirectorPage.choiceGroup(config.getUrlDict()['Approval']['approvalGroupF'])
        except:
            sleep(1)
            self._auditAdjustDirectorPage.click_selectResult()
            sleep(1)
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

        try:
            self._myAuditListPage.getIntoBoe()
        except:
            sleep(1)
            self._myAuditListPage.getIntoBoe()
        self._boeCommon.switchWindow()

        self._boeCommon.click_accountMessage()
        self._boeCommon.click_approveButton()
        self._boeCommon.switchWindow()

        self.login.driver.quit()

if __name__ == '__main__':
    a = SharingCenterApprove('LMJT-BX2102180140')
    # dict = {'invoiceNo':'880000000007', 'invoiceCode':'88000007', 'invoiceDate':'2020-1-1', 'invoiceFee':'1000.00', 'invoiceTax':'47.62', 'invoiceRemark':'测试开票申请单'}
    # a.sharingCenterApproveChuShen(modify=True, **dict)
    a.sharingCenterApproveChuShen()
    a.sharingCenterApproveFuShen()


