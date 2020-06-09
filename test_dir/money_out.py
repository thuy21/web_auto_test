import pytest, sys, os
from time import sleep
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from public_module.tools import xls_update
from public_module.tools import xlsx_read


def money_out(page, flag):
    # 生成上账模板
    list = xlsx_read('./tmp_file/import.xlsx', '上下账')
    xls_update('./tmp_file/资金下账模板.xls', list, 1)
    js = 'window.scrollTo(0,1000);'

    page.driver.find_element_by_link_text('资金业务管理').click()
    page.driver.find_element_by_link_text('资金下账').click()

    page.driver.switch_to_frame(1)
    page.money_manage_in_add.click()

    page.driver.switch_to.default_content()
    page.driver.switch_to_frame(2)

    page.money_manage_out_add_class.click()
    page.money_manage_out_add_class_check.click()

    page.money_manage_out_add_type.click()
    page.money_manage_out_add_type_check.click()

    # 点击 上传文件
    page.money_manage_in_file_upload.click()
    page.money_manage_out_file_check.send_keys(os.path.abspath('./') + '/tmp_file/资金下账模板.xls')
    sleep(2)
    # 点击开始上传
    page.money_manage_out_file_submit.click()
    sleep(3)
    page.money_manage_out_cont.send_keys('测试下账thuu')
    page.driver.execute_script(js)
    page.btn_next.click()
    sleep(1)
    page.driver.execute_script(js)
    page.btn_next.click()
    sleep(1)
    page.money_manage_out_close.click()

    # 审核
    page.driver.switch_to.default_content()
    page.driver.switch_to_frame(1)
    page.win_refresh.click()
    sleep(1)
    # 审核下账
    if flag == '0':
        page.money_manage_out_check.click()
        page.money_manage_out_check_cont.send_keys('审核通过')
        page.money_manage_out_check_submit.click()
        page.win_prisoner_confirm.click()

    # 提交下账
    page.money_manage_out_submit.click()
    sleep(1)
    page.win_prisoner_confirm.click()
    res = ""
    page.win_refresh.click()
    # res = page.money_manage_out_result.text
    while True:
        res = page.money_manage_out_result.text
        sleep(1)
        if "处理中" in res:
            page.win_refresh.click()
        else:
            break
        sleep(2)

    page.driver.switch_to.default_content()
    page.win_min_close.click()
    sleep(1)
    page.driver.find_element_by_link_text('资金业务管理').click()

    return res
