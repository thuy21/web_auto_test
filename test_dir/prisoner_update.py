import sys, os, threading
from time import sleep
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from public_module.tools import xlsx_read
from public_module.tools import xls_update
from test_dir.thread.prisoner_upate_result import *


def t1est_b_query(page):
    """罪犯信息查询"""
    page.driver.find_element_by_link_text('戒毒人员信息管理').click()
    page.driver.switch_to_frame(1)
    page.base_prisoner_status.click()
    page.base_prisoner_status_select.click()
    page.base_prisoner_card_status.click()
    page.base_prisoner_card_status_select.click()

    page.base_prisoner_minBlance.send_keys('100')
    page.base_prisoner_search.click()

    sleep(1000)


def prisoner_add(page):
    """罪犯信息导入"""
    # 生成模板
    list = xlsx_read('./tmp_file/import.xlsx', '添加新犯')
    xls_update('./tmp_file/新学员导入模板.xls', list, 2)

    file_path = os.path.abspath('./')

    page.driver.find_element_by_link_text('基础信息管理').click()
    page.driver.find_element_by_link_text('戒毒人员信息管理').click()
    page.driver.switch_to_frame(1)
    page.fun_btn_nth5.click()

    page.driver.switch_to.default_content()
    page.driver.switch_to_frame(2)
    page.btn_file_upload.click()

    page.input_file_upload.send_keys(file_path + '/tmp_file/新学员导入模板.xls')
    sleep(1)
    page.base_prisoner_file_upload_submit.click()
    sleep(2)
    result = page.base_prisoner_file_upload_result
    for item in result:
        assert "有误" not in item.text

    page.base_prisoner_add_submit.click()
    sleep(1)
    try:
        page.driver.switch_to.default_content()
        result = page.base_prisoner_add_submit_result.text
    except:
        page.driver.switch_to_frame(2)
        result = page.win_error.text

    return result


def tessqt_d_prisoner_status_query(page):
    page.driver.find_element_by_link_text('戒毒人员信息管理').click()
    page.driver.switch_to_frame(1)
    page.btn_search.click()
    sleep(3)
    res = page.base_prisoner_account_status.text
    if '待开户' in res:
        sleep(5)
        page.btn_search.click()
        sleep(3)
        res = page.base_prisoner_account_status.text
        if '待开户' in res:
            sleep(5)
            page.driver.switch_to.default_content()
            page.driver.find_element_by_link_text('基础信息管理').click()
            sleep(1)
            page.driver.find_element_by_link_text('银行业务管理').click()
            sleep(1)
            page.driver.find_element_by_link_text('戒毒人员银行账户').click()
            sleep(1)
            page.driver.switch_to_frame(2)
            page.blance_prisoner_reg.click()
            page.blance_prisoner_reg_status.click()
            page.btn_search.click()
            sleep(3)
            page.driver.find_element_by_link_text('戒毒人员开户').click()
            page.blance_prisoner_reg_name.send_keys('小小2')
            sleep(1)
            page.blance_prisoner_reg_name_select.click()
            sleep(0.5)
            page.blance_prisoner_reg_submit.click()
            sleep(1)
            res = page.dialog_h2.text
            assert "成功" in res
            sleep(120)
