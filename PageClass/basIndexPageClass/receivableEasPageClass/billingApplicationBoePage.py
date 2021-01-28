# -*- coding:utf-8 -*-
from PageClass.basIndexPageClass.basIndexPage import BasIndexPage
from PageClass.common.boeCommon import BoeCommon



# 开票申请单
class BillingApplicationBoePage(BasIndexPage,BoeCommon):

    def __init__(self, driver):
        BasIndexPage.__init__(self, driver)


