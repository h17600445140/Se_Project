# -*- coding:utf-8 -*-
from time import sleep

from PageClass.ledgerIndexPageClass.acceptanceLedgerPage import AcceptanceLedgerPage
from Testcases.common.loginDepend import LoginDepend
from Util import record



class TestAcceptanceLedgerPage():

    def setup_class(self):
        self.login = LoginDepend('ledgerHost', 'user')
        self.acceptanceLedgerPage = AcceptanceLedgerPage(self.login.driver)

    def teardown_class(self):
        pass

    def test_addAcceptanceLedger(self):

        self.acceptanceLedgerPage.getInLedger('验收单台账')

        self.acceptanceLedgerPage.click_ledgerDetail()

        self.acceptanceLedgerPage.clickTargetButton('新增')

        self.acceptanceLedgerPage.input_acceptanceNo('ysd002')

        self.acceptanceLedgerPage.input_acceptOrderNo('dd002')

        self.acceptanceLedgerPage.selectAcceptVendor('hc供应商1')

        self.acceptanceLedgerPage.selectAcceptContract('hc00000020', contractName='hc合同020')

        self.acceptanceLedgerPage.selectAcceptProject('hcXM1', projectName='hc项目1')

        self.acceptanceLedgerPage.selectAcceptReceivingUnit('AD', deptName='A部门')

        self.acceptanceLedgerPage.selectAcceptAgent('1', agentName='1hc')

        self.acceptanceLedgerPage.input_acceptanceDate('2021-2-2')

        self.acceptanceLedgerPage.click_acceptSubmitButton()

        assert self.acceptanceLedgerPage.getToastBoxText() == '保存成功'

        self.acceptanceLedgerPage.input_acceptanceNoQuery('ysd002')

        self.acceptanceLedgerPage.click_acceptanceQueryButton()

        assert self.acceptanceLedgerPage.get_acceptanceNoResult() == 'ysd002'


    def test_editAcceptanceLedgerDetail(self):

        self.acceptanceLedgerPage.input_acceptanceNoQuery('ysd002')

        self.acceptanceLedgerPage.click_acceptanceQueryButton()

        self.acceptanceLedgerPage.click_acceptanceEditButoon()

        self.acceptanceLedgerPage.click_addDetailButton()

        self.acceptanceLedgerPage.input_detailName('hcProduct')

        self.acceptanceLedgerPage.input_detailSpecification('大')

        self.acceptanceLedgerPage.input_detailUnit('个')

        self.acceptanceLedgerPage.input_detailNum('1')

        self.acceptanceLedgerPage.input_detailPrice('100.00')

        self.acceptanceLedgerPage.input_detailTaxAmount('100.00')

        self.acceptanceLedgerPage.input_detailTaxRate('1')

        self.acceptanceLedgerPage.input_detailTax('1.00')

        self.acceptanceLedgerPage.click_detailSubmit()

        assert self.acceptanceLedgerPage.getToastBoxText() == '保存成功'

        record.writeDataToRecord({'acceptanceNo':'ysd002'}, type='acceptanceLedgerData')



