# -*- coding:utf-8 -*-
import allure
import pytest

from PageClass.basIndexPageClass.purchaseEasPageClass.newCostEstimateBoePage import NewCostEstimateBoePage
from Testcases.common.boeBusinessApprove import BusinessApprove
from Testcases.common.boeSharingCenterApprove import SharingCenterApprove
from Testcases.common.loginDepend import LoginDepend
from Util import logger



@allure.feature("成本暂估单（新）流程")
class TestNewCostEstimateBoe():

    boeNum = globals()

    def setup_class(self):
        self.login = LoginDepend('basHost', 'user')
        self.newCostEstimateBoePage = NewCostEstimateBoePage(self.login.driver)

    def teardown_class(self):
        # self.newCostEstimateBoePage.driver.quit()
        pass

    @allure.story("成本暂估单（新）业务报账界面单据提交")
    @allure.step("成本暂估单（新）业务报账界面单据提交步骤")
    @allure.severity("blocker")
    @pytest.mark.dependency(name='submit')
    def test_newCostEstimateBoe(self):

        logger.info(" ----- 单据提交流程开始 ----- ")

        with allure.step("点击选择采购付款页面"):
            self.newCostEstimateBoePage.selectTabType('采购付款')
        with allure.step("进入成本暂估单（新）单据提交页面"):
            self.newCostEstimateBoePage.boeRntry('成本暂估(新)')

        global boeNum
        boeNum = self.newCostEstimateBoePage.getBoeNum()

        with allure.step("选择业务类型"):
            self.newCostEstimateBoePage.input_operationType('成本暂估')
        with allure.step("输入备注"):
            self.newCostEstimateBoePage.input_boeAbstract('测试成本暂估单(新)')

        with allure.step("选择项目"):
            self.newCostEstimateBoePage.input_project('hc项目1')
        with allure.step("选择供应商"):
            self.newCostEstimateBoePage.selectVendor('hcGYS1', vendorName='hc供应商1')
        with allure.step("选择关联合同"):
            self.newCostEstimateBoePage.selectContract('hc00000020')
        with allure.step("选择成本中心"):
            self.newCostEstimateBoePage.selectCc('hcCBZX', ccName='hc成本中心A部门')

        with allure.step("关联验收单"):
            self.newCostEstimateBoePage.relateAcceptanceLedger('ysd002')

        with allure.step("点击单据提交"):
            self.newCostEstimateBoePage.click_boeSubmitButton()
        with allure.step("点击单据关闭按钮"):
            self.newCostEstimateBoePage.click_close()

        with allure.step("进行单据生成校验"):
            self.newCostEstimateBoePage.click_more()
            self.newCostEstimateBoePage.input_boeNumQuery(boeNum)
            self.newCostEstimateBoePage.click_queryButton()

        with allure.step("断言结果：{}".format(self.newCostEstimateBoePage.checkBoeNumExistIsOrNot(boeNum))):
            assert self.newCostEstimateBoePage.checkBoeNumExistIsOrNot(boeNum) == True


    @allure.story("成本暂估单（新）费用报销界面业务审批")
    @allure.step("成本暂估单（新）费用报销界面业务审批步骤")
    @pytest.mark.dependency(depends=["submit"] )
    def test_businessApprove(self):
        logger.info(" ----- 单据业务审批开始 ----- ")
        global boeNum
        self.businessApprove = BusinessApprove(boeNum)
        content = self.businessApprove.boeBusinessApprove()
        logger.info(" ----- 单据业务审批开始 ----- ")
        assert content == '审批成功'


    @allure.story("成本暂估单（新）共享中心界面财务审批")
    @allure.step("成本暂估单（新）共享中心界面财务审批步骤")
    @pytest.mark.dependency(depends=["submit"])
    def test_sharingCenterApprove(self):
        logger.info(" ----- 单据财务审批开始 ----- ")
        global boeNum
        self.sharingCenterApprove = SharingCenterApprove(boeNum)
        self.sharingCenterApprove.sharingCenterApproveChuShen()
        self.sharingCenterApprove.sharingCenterApproveFuShen()
        logger.info(" ----- 单据财务审批结束 ----- ")
