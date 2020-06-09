import sys, os
from time import sleep
from os.path import dirname, abspath
from public_module.tools import xls_update
from public_module.tools import xlsx_read
from data_helper.mysql_util import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))


def prisoner_switch_level(page):
    # 生成模板
    js_ver = 'window.scrollTo(0,1000);'
    list = xlsx_read('./tmp_file/import.xlsx', '转级')
    xls_update('./tmp_file/批量转级模板.xls', list, 1)

    page.driver.find_element_by_link_text('基础信息管理').click()
    page.driver.find_element_by_link_text('戒毒人员转级管理').click()

    page.driver.switch_to_frame(1)
    page.prisoner_switch_area.click()

    page.driver.switch_to.default_content()
    page.driver.switch_to_frame(2)
    page.prisoner_switch_area_upload.click()

    page.input_file_upload.send_keys(os.path.abspath('./') + '/tmp_file/批量转级模板.xls')
    sleep(2)
    page.prisoner_switch_level_upload_submit.click()
    sleep(2)
    # res = page.prisoner_switch_area_upload_list
    # cursor1 = conn("116.63.68.108", "lecentMysql", "lecentMysql#1234", "gd_9081")
    # bol = True
    # index = 0
    # for item in res:
    #     if bol:
    #         bol = False
    #         continue
    #     text = item.text.split(maxsplit=5)
    #     config_list = query_one(cursor1, "select PrisonAreaName from prisoner where `Code`='{}'".format(list[index][1]))
    #     # 断言监区是否正确
    #     assert str(text[4]) == str(config_list)
    #     index += 1
    # close()
    #
    # page.prisoner_switch_area_cont.send_keys('转监区测试')
    # page.driver.execute_script(js_ver)
    # page.btn_next.click()
    # sleep(1)
    # page.btn_next.click()
    # sleep(1)
    # res = page.prisoner_switch_area_submit_result.text
    #
    # return res
