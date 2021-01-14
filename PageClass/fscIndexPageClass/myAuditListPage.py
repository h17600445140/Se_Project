# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from PageClass.fscIndexPageClass.fscCommonPage import FscCommonPage



class MyAuditListPage(FscCommonPage):

    def __init__(self,driver):
        FscCommonPage.__init__(self,driver)
