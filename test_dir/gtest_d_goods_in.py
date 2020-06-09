import pytest, sys, os
from time import sleep
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from public_module.tools import xls_update
from public_module.login import init_browser


@pytest.mark.skip()
class Test_商品采购:
    """商品采购"""

    def test_商品采购(self, browser, base_url):
        js = 'window.scrollTo(0,1000);'
        page = init_browser(browser, base_url)

        page.win_top_close.click()
        page.driver.find_element_by_link_text('采购业务管理').click()

        page.driver.find_element_by_link_text('商品采购').click()
        page.driver.switch_to_frame(1)
        page.采购_仓库.click()
        page.采购_仓库选择.click()
        page.采购_供应商.click()
        page.采购_供应商选择.click()
        page.purchase_goods_upload.click()

        file_path = os.path.abspath('./')
        page.purchase_goods_upload_select.send_keys(file_path + '/tmp_file/商品采购导入模板.xls')
        page.purchase_goods_upload_submit.click()
        sleep(1)
        res = page.dialog_h2.text
        print(res)
        page.win_prisoner_confirm.click()
        page.driver.execute_script(js)
        sleep(0.5)
        page.purchase_goods_submit.click()
        sleep(1)
        page.win_prisoner_confirm.click()
        sleep(2)

        # 采购审核
        page.driver.switch_to.default_content()
        page.driver.find_element_by_link_text('采购审核').click()
        sleep(1)
        page.driver.switch_to_frame(2)
        sleep(1)
        page.purchase_check_pass.click()
        page.purchase_check_pass_cont.send_keys('同意采购')
        page.purchase_check_pass_submit.click()
        page.driver.switch_to.default_content()
        sleep(1)
        page.win_top_confirm.click()

        # 入库
        page.driver.switch_to.default_content()
        page.driver.switch_to_frame(2)
        sleep(1)
        page.purchase_check_pass.click()
        sleep(1)
        page.win_prisoner_confirm.click()
        sleep(0.5)
        res = page.dialog_h2.text
        assert '成功' in res
        sleep(20)


if __name__ == "__main__":
    pytest.main(['-v', '-s', 'test_d_goods_in.py'])
