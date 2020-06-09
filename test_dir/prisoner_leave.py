import pytest, sys, os
from time import sleep
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))

from public_module.tools import xlsx_read


def prisoner_leave(page):
    # 生成上账模板
    list = xlsx_read('./tmp_file/import.xlsx', '添加新犯')

    page.driver.find_element_by_link_text('资金业务管理').click()
    page.driver.find_element_by_link_text('出所结算').click()
    page.driver.switch_to_frame(1)
    page.money_manage_leave
    sleep(5)
    page.money_manage_leave.click()
    sleep(2)
    page.money_manage_leave.send_keys(list[2])
    sleep(1)
    # page.money_manage_leave_prisoner.click()
    page.btn_search.click()
    sleep(1)
    page.driver.find_element_by_link_text('出所结算').click()
    page.money_manage_leave_cont.send_keys("出狱测试")
    page.money_manage_leave_submit.click()
    res = page.dialog_h2.text
    return res
