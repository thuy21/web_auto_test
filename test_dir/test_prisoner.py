import sys
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from test_dir.prisoner_update import *
from test_dir.money_in import *
from test_dir.money_out import *
from test_dir.goods_sell import *
from test_dir.prisoner_leave import *
from test_dir.prisoner_switch_area import *
from test_dir.prisoner_switch_level import *
from test_dir.goods_sell_return import *
from public_module.login import init_browser
from data_helper.mysql_util import *


class Test_base_prisoner:
    page = ""
    js_ver = ""
    sys_config = ""
    num = 0
    text = ""
    is_confirm = [False]

    def test_a_init(self, browser, base_url, config_data):
        global page, js_ver, sys_config
        page = init_browser(browser, base_url)
        sys_config = config_data

    @pytest.mark.skip()
    def test_b_prisonser_add(self):
        """ 导入罪犯 """
        self.num = 2
        self.text = '基础信息管理'
        res = prisoner_add(page)

        assert '失败0个' in res

    @pytest.mark.skip()
    def test_c_money_in(self):
        self.num = 2
        self.text = '资金业务管理'
        money_in(page, str(sys_config['上下账自动审核']))
        # assert "成功" in res

    @pytest.mark.skip()
    def test_d_money_out(self):
        self.num = 2
        self.text = '资金业务管理'
        res = money_out(page, str(sys_config['上下账自动审核']))
        assert "成功" in res

    @pytest.mark.skip()
    def test_e_sell(self):
        self.num = 1
        self.text = '销售业务管理'
        goods_sell(page, self.is_confirm, sys_config['销售审核'])

    @pytest.mark.skip()
    def test_f_prisoner_switch_area(self):
        self.num = 2
        self.text = '基础信息管理'
        res = prisoner_switch_area(page)
        assert "失败" not in res

    @pytest.mark.skip()
    def test_g_prisoner_switch_level(self):
        self.num = 2
        self.text = '基础信息管理'
        prisoner_switch_level(page)

    def test_h_goods_sell_return(self):
        self.num = 2
        self.text = '销售业务管理'
        goods_sell_return(page)

    @pytest.mark.skip()
    def test_i_prisoner_leave(self):
        self.num = 1
        self.text = '资金业务管理'
        prisoner_leave(page)

    def teardown_method(self):
        page.driver.switch_to.default_content()
        bol = False
        if self.is_confirm[0]:
            page.sell_center_submit_result_confirm.click()
            sleep(1)

        for i in range(0, self.num):
            try:
                page.win_min_close.click()
            except:
                pass
            bol = True
            sleep(0.5)

        if bol:
            page.driver.find_element_by_link_text(self.text).click()
            sleep(10)


if __name__ == "__main__":
    pytest.main(['-v', '-s', 'test_prisoner.py'])
