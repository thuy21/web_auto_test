import pytest,sys,os
from time import sleep
from os.path import dirname,abspath
from selenium.webdriver.common.by import By

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.capital_page import base_widget
from public_module.tools import xls_replace
from public_module.login import init_browser

class Test_capit:
    def test_capit_in(self,browser,base_url):

        #生成上账模板
        xls_replace('NNYY0TX0TXW0TX9TXWTX208','	邬兴贵','10')

        page = init_browser(browser,base_url)

        page.close_top.click()
        page.money_manager.click()
        page.money_manage_in.click()


        page.driver.switch_to_frame(1)
        page.money_manage_add.click()

        page.driver.switch_to.default_content()
        page.driver.switch_to_frame(2)

        page.money_manage_add_class.click()
        page.money_manage_add_class_check.click()

        page.money_manage_add_type.click()
        page.money_manage_add_type_check.click()

        #点击 上传文件
        page.btn_upload.click()
		#获取 选择文件 按钮，并直接发送文件
        file_path= os.path.abspath('./')
        page.btn_upload_get.send_keys(file_path+'/tmp_file/资金上账模板.xls')
        sleep(2)
		#点击开始上传
        page.btn_upload_start.click()

        page.money_manage_in_cont.send_keys('测试上账thuu')
        page.btn_next.click()
        js = 'window.scrollTo(0,1000);'
        page.driver.execute_script(js)
        page.btn_next.click()
        page.money_manage_in_close.click() #上账完成

        page.driver.switch_to.default_content()
        page.driver.switch_to_frame(1)
        page.win_refresh.click()
        sleep(1)
        page.money_manage_in_check.click()
        page.money_manage_in_check_cont.send_keys('测试上账thuu')
        page.money_manage_in_check_submit.click()
        page.win_prisoner_confirm.click()
        sleep(1)
        page.money_manage_in_submit.click()
        sleep(0.5)
        page.win_prisoner_confirm.click()
        sleep(1)
        res = page.dialog_h2.text
        assert '成功' in res


if __name__ == "__main__":
    pytest.main(['-v','-s','test_tmp.py'])