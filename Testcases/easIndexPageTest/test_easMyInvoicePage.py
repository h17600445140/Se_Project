# -*- coding:utf-8 -*-
from time import sleep

from PageClass.easIndexPageClass.easIndexPage import EasIndexPage
from PageClass.easIndexPageClass.easMyInvoicePage import EasMyInvoiceIndexPage
from PageClass.ipoolIndexPageClass.invoiceQueryPage import InvoiceQueryPage
from Testcases.common.loginDepend import LoginDepend
from Util import logger


class TestEasMyInvoicePage(object):

    def setup_class(self):
        self.login = LoginDepend('easHost', 'user')
        self.easIndexPage = EasIndexPage(self.login.driver)
        self.easIndexPage.open_menuMyInvoice()
        self.easMyInvoiceIndexPage = EasMyInvoiceIndexPage(self.login.driver)

        self.invoiceQueryPage = InvoiceQueryPage(self.login.driver)

    def teardown_class(self):
        pass

    def test_addInvoice(self):

        logger.info("当前窗口为：{}".format(self.easIndexPage.getCurrentWindowHandle()))
        windowsList = self.easIndexPage.getWindowHandles()
        self.easIndexPage.switchToWin(windowsList[1])
        logger.info("当前窗口为：{}".format(self.easIndexPage.getCurrentWindowHandle()))

        self.easMyInvoiceIndexPage.open_manualInvoiceEntry()
        self.easMyInvoiceIndexPage.click_invoiceType()

        sleep(1)
        self.easMyInvoiceIndexPage.open_addInvoiceWindow('增值税普通发票')

        self.easMyInvoiceIndexPage.input_invoiceNo('810000000006')
        self.easMyInvoiceIndexPage.input_invoiceCode('81000006')
        self.easMyInvoiceIndexPage.selectInvoiceDate()


        self.easMyInvoiceIndexPage.input_feeTotal('100.10')
        self.easMyInvoiceIndexPage.input_tax('10.10')
        self.easMyInvoiceIndexPage.input_checkCode('123456')

        self.easMyInvoiceIndexPage.click_invoiceSubmitButton()

        self.easMyInvoiceIndexPage.input_billingCode('81000006')
        self.easMyInvoiceIndexPage.click_myInvoiceQueryButton()

        sleep(1)
        assert self.easMyInvoiceIndexPage.invoiceQueryResult == True

        self.easMyInvoiceIndexPage.gotoInvoiceQueryPage()

        self.invoiceQueryPage.open_invoiceQueryTab()

        sleep(3)
        self.invoiceQueryPage.open_subInvoiceQueryTab('增值税普票')
        self.invoiceQueryPage.input_billingNoQuery('810000000006')
        self.invoiceQueryPage.input_billingCodeQuery('81000006')
        self.invoiceQueryPage.click_invoiceQueryButton()


        print(self.invoiceQueryPage.invoiceQueryResult())
