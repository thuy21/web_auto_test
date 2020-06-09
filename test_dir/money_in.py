import sys, os
from time import sleep
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from public_module.tools import xls_update
from public_module.tools import xlsx_read


def money_in(page, flag):
    # 生成上账模板
    list = xlsx_read('./tmp_file/import.xlsx', '上下账')
    xls_update('./tmp_file/资金上账模板.xls', list, 1)

    page.driver.find_element_by_link_text('资金业务管理').click()
    page.driver.find_element_by_link_text('资金上账').click()

    page.driver.switch_to_frame(1)
    page.money_manage_in_add.click()
    page.driver.switch_to.default_content()
    page.driver.switch_to_frame(2)

    page.money_manage_in_add_class.click()
    page.money_manage_in_add_class_check.click()

    page.money_manage_in_add_type.click()
    page.money_manage_in_add_type_check.click()

    #  上传文件
    page.money_manage_in_file_upload.click()
    page.input_file_upload.send_keys(os.path.abspath('./')+'/tmp_file/资金上账模板.xls')
    sleep(2)
    # 点击开始上传
    page.money_manage_in_file_submit.click()
    page.money_manage_in_cont.send_keys('测试上账thuu')
    page.btn_next.click()
    js = 'window.scrollTo(0,1000);'
    page.driver.execute_script(js)
    page.btn_next.click()
    page.money_manage_in_close.click()  # 上账完成

    page.driver.switch_to.default_content()
    page.driver.switch_to_frame(1)
    page.win_refresh.click()
    # sleep(1)
    # # 审核上账
    # if flag == '0':
    #     page.money_manage_in_check.click()
    #     page.money_manage_in_check_cont.send_keys('测试上账thuu')
    #     page.money_manage_in_check_submit.click()
    #     page.win_prisoner_confirm.click()
    #     sleep(1)
    #
    # page.money_manage_in_submit.click()
    # sleep(1)
    # res = page.dialog_h2.text
    # page.win_prisoner_confirm.click()
    # sleep(3)
    res2 = ""
    # while True:
    #     res2 = page.dialog_h2.text
    #     if res2 != res:
    #         break
    #     else:
    #         sleep(1)

    # page.driver.switch_to.default_content()
    # page.win_min_close.click()
    # sleep(1)
    # page.driver.find_element_by_link_text('资金业务管理').click()

    return res2
