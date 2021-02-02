# -*- coding:utf-8 -*-
from PageClass.basIndexPageClass.basIndexPage import BasIndexPage
from PageClass.common.boeCommon import BoeCommon


# 作废/红字发票申请单
class NewObsoleteRedLetterInvoiceApplictationBoePage(BasIndexPage,BoeCommon):

    def __init__(self, driver):
        BasIndexPage.__init__(self, driver)