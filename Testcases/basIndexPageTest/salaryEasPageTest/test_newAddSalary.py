# -*- coding:utf-8 -*-
import datetime
from time import sleep

import allure
import pytest

from PageClass.basIndexPageClass.salaryEasPageClass.newAddSalaryPage import NewAddSalaryPage
from Testcases.common.loginDepend import LoginDepend
from Util import logger


@allure.feature("新增薪酬流程")
class TestNewAddSalary():

    boeNum = globals()

    def setup_class(self):
        self.publicLogin = LoginDepend('basHost', 'user')
        self.newAddSalaryPage = NewAddSalaryPage(self.publicLogin.driver)

    def teardown_class(self):
        self.newAddSalaryPage.driver.quit()

    @allure.story("新增薪酬业务报账界面流程")
    @allure.step("新增薪酬业务报账界面流程")
    @allure.severity("blocker")
    @pytest.mark.dependency(name='submit')
    def test_newAddSalary(self):

        logger.info(" ----- 新增薪酬流程开始 ----- ")

        with allure.step("点击选择薪酬报账页面"):
            self.newAddSalaryPage.selectTabType('薪酬报账')
        with allure.step("进入薪酬报账新增提交页面"):
            self.newAddSalaryPage.boeRntry('新增薪酬')

        global boeNum
        boeNum = self.newAddSalaryPage.getBoeNum()

        with allure.step("选择薪酬区间"):
            self.newAddSalaryPage.selectSalaryPeriod(datetime.datetime.now().strftime("%Y-%m"))
        with allure.step("选择业务类型"):
            self.newAddSalaryPage.selectSalaryOperationType('UI工资发放')
        with allure.step("输入备注"):
            self.newAddSalaryPage.input_salaryRemark('测试新增薪酬')
        with allure.step("点击保存按钮"):
            self.newAddSalaryPage.click_salarySaveButton()

        assert self.newAddSalaryPage.getToastBoxText() == '保存成功'

        with allure.step("点击明细新增按钮"):
            self.newAddSalaryPage.click_salaryAddButton()
        with allure.step("选择责任部门"):
            self.newAddSalaryPage.selectSalaryDept('UICBZX', deptName='UI成本中心')
        with allure.step("输入薪酬明细"):
            self.newAddSalaryPage.input_JiTiYingFa('100.10')
            self.newAddSalaryPage.input_JiTiKouKuan('10.10')
            self.newAddSalaryPage.input_JiTiShiFa('90.00')
        with allure.step("点击确认按钮"):
            self.newAddSalaryPage.clickTargetButton('确认')

        assert self.newAddSalaryPage.getToastBoxText() == '保存成功'

        with allure.step("点击提交按钮"):
            self.newAddSalaryPage.clickSalarySubmitButton()
        with allure.step("点击确定按钮"):
            self.newAddSalaryPage.click_button('确定')

        assert self.newAddSalaryPage.getToastBoxText() == '保存成功'

        self.newAddSalaryPage.closeCurrentWindows()