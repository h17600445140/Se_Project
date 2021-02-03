# -*- coding:utf-8 -*-
import allure
import pytest

from PageClass.basIndexPageClass.purchaseEasPageClass.costEstimateBoePage import CostEstimateBoePage
from Testcases.common.boeBusinessApprove import BusinessApprove
from Testcases.common.boeSharingCenterApprove import SharingCenterApprove
from Testcases.common.loginDepend import LoginDepend
from Util import logger


@allure.feature("成本暂估单（旧）流程")
class TestCostEstimateBoe():

    boeNum = globals()

    def setup_class(self):
        self.login = LoginDepend('basHost', 'user')
        self.costEstimateBoePage = CostEstimateBoePage(self.login.driver)

    def teardown_class(self):
        # self.costEstimateBoePage.driver.quit()
        pass

    @allure.story("成本暂估单（旧）业务报账界面单据提交")
    @allure.step("成本暂估单（旧）业务报账界面单据提交步骤")
    @allure.severity("blocker")
    @pytest.mark.dependency(name='submit')
    def test_costEstimateBoe(self):

        logger.info(" ----- 单据提交流程开始 ----- ")

        with allure.step("点击选择采购付款页面"):
            self.costEstimateBoePage.selectTabType('采购付款')
        with allure.step("进入成本暂估单（旧）单据提交页面"):
            self.costEstimateBoePage.boeRntry('成本暂估（旧）')

        global boeNum
        boeNum = self.costEstimateBoePage.getBoeNum()

        with allure.step("选择业务类型"):
            self.costEstimateBoePage.input_operationType('成本暂估')
        with allure.step("输入备注"):
            self.costEstimateBoePage.input_boeAbstract('测试成本暂估单（旧）')

        with allure.step("选择供应商"):
            self.costEstimateBoePage.selectVendor('hcGYS1', vendorName='hc供应商1')
        with allure.step("选择关联合同"):
            self.costEstimateBoePage.selectContract('hc00000020')

        with allure.step("输入订单编号"):
            self.costEstimateBoePage.input_costOrderNumber('hcOrder001')
        with allure.step("选择业务小类"):
            self.costEstimateBoePage.input_costOperationSubType('暂估1')
        with allure.step("输入总金额"):
            self.costEstimateBoePage.input_costExpenseAmount('100.10')
        with allure.step("选择责任部门"):
            self.costEstimateBoePage.selectCc('AD', 'A部门')
        with allure.step("选择项目"):
            self.costEstimateBoePage.input_costProject('hc项目1')
        with allure.step("输入备注"):
            self.costEstimateBoePage.input_costRemark('测试成本暂估单（旧）')

        with allure.step("点击单据提交"):
            self.costEstimateBoePage.click_boeSubmitButton()
        with allure.step("点击单据关闭按钮"):
            self.costEstimateBoePage.click_close()

        with allure.step("进行单据生成校验"):
            self.costEstimateBoePage.click_more()
            self.costEstimateBoePage.input_boeNumQuery(boeNum)
            self.costEstimateBoePage.click_queryButton()

        with allure.step("断言结果：{}".format(self.costEstimateBoePage.checkBoeNumExistIsOrNot(boeNum))):
            assert self.costEstimateBoePage.checkBoeNumExistIsOrNot(boeNum) == True


    @allure.story("成本暂估单（旧）费用报销界面业务审批")
    @allure.step("成本暂估单（旧）费用报销界面业务审批步骤")
    @pytest.mark.dependency(depends=["submit"] )
    def test_businessApprove(self):
        logger.info(" ----- 单据业务审批开始 ----- ")
        global boeNum
        self.businessApprove = BusinessApprove(boeNum)
        content = self.businessApprove.boeBusinessApprove()
        logger.info(" ----- 单据业务审批开始 ----- ")
        assert content == '审批成功'


    @allure.story("成本暂估单（旧）共享中心界面财务审批")
    @allure.step("成本暂估单（旧）共享中心界面财务审批步骤")
    @pytest.mark.dependency(depends=["submit"])
    def test_sharingCenterApprove(self):
        logger.info(" ----- 单据财务审批开始 ----- ")
        global boeNum
        self.sharingCenterApprove = SharingCenterApprove(boeNum)
        self.sharingCenterApprove.sharingCenterApproveChuShen()
        self.sharingCenterApprove.sharingCenterApproveFuShen()
        logger.info(" ----- 单据财务审批结束 ----- ")







