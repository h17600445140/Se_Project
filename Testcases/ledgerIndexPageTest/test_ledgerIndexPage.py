# -*- coding:utf-8 -*-
from PageClass.ledgerIndexPageClass.ledgerIndexPage import LedgerIndexPage
from Testcases.common.loginDepend import LoginDepend



class TestLedgerIndexPage(object):

    def setup_class(self):
        self.login = LoginDepend('ledgerHost', 'user')
        self.LedgerIndexPage = LedgerIndexPage(self.login.driver)

    def teardown_class(self):
        pass


    def test_getInLedger(self):

        self.LedgerIndexPage.getInLedger('验收单台账')

        self.LedgerIndexPage.click_ledgerDetail()

        self.LedgerIndexPage.clickTargetButton('新增')