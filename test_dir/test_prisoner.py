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
from public_module.login import init_browser
from data_helper.mysql_util import *


class Test_base_prisoner:
    page = ""
    js_ver = ""
    sys_config = ""
    test_id = 0

    def test_a_init(self, browser, base_url, config_data):
        global page, js_ver, sys_config

        page = init_browser(browser, base_url)
        sys_config = config_data

    @pytest.mark.skip()
    def test_b_prisonser_add(self):
        """ 导入罪犯 """
        self.test_id = 1
        res = prisoner_add(page)
        assert '失败0个' in res

    @pytest.mark.skip()
    def test_c_money_in(self):
        self.test_id = 2
        res = money_in(page, str(sys_config['上下账自动审核']))
        # assert "成功" in res

    @pytest.mark.skip()
    def test_d_money_out(self):
        test_id = 3
        res = money_out(page, str(sys_config['上下账自动审核']))
        assert "成功" in res

    @pytest.mark.skip()
    def test_e_sell(self):
        test_id = 4
        res = goods_sell(page)
        assert "成功" in res

    @pytest.mark.skip()
    def test_f_prisoner_leave(self):
        test_id = 5
        res = prisoner_leave(page)
        assert "成功" in res

    @pytest.mark.skip()
    def test_g_prisoner_switch_area(self):
        res = prisoner_switch_area(page, 0)
        assert "失败" not in res

    def test_h_prisoner_switch_level(self):
        prisoner_switch_level(page)
        self.test_id = 2

    def teardown_method(self):
        page.driver.switch_to.default_content()

        if self.test_id == 2:
            sleep(120)
            page.win_min_close.click()
            sleep(1)
            page.driver.find_element_by_link_text('资金业务管理').click()
            sleep(1)


if __name__ == "__main__":
    pytest.main(['-v', '-s', 'test_prisoner.py'])
