import pytest, sys, os
from time import sleep
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))

from public_module.tools import xlsx_read

list = []


def prisoner_leave(page):
    # 生成上账模板
    global list
    list = xlsx_read('./tmp_file/import.xlsx', '出狱')

    page.driver.find_element_by_link_text('资金业务管理').click()

    # for i in range(0, len(list)):
    #     page.driver.find_element_by_link_text('出所结算').click()
    #     page.driver.switch_to_frame(1)
    #     page.money_manage_leave
    #     sleep(5)
    #     page.money_manage_leave.click()
    #     sleep(2)
    #     page.money_manage_leave.send_keys(list[i][0])
    #     sleep(1)
    #     page.btn_search.click()
    #     sleep(1)
    #     page.driver.find_element_by_link_text('出所结算').click()
    #     page.money_manage_leave_cont.send_keys("出狱测试")
    #     page.money_manage_leave_submit.click()
    #     res = page.dialog_h2.text
    #
    #     if "出所结算完成" in res:
    #         assert "完成" in res
    #     else:
    #         assert "成功" in res
    #
    #     page.driver.switch_to.default_content()
    #     page.win_min_close.click()
    #     sleep(1)

    prisoner_leave_cancel(page)


def prisoner_leave_cancel(page):
    global list
    for i in range(0, len(list)):
        page.driver.find_element_by_link_text('出所结算').click()
        page.driver.switch_to_frame(1)
        page.money_manage_leave
        sleep(5)
        page.money_manage_leave.click()
        sleep(2)
        page.money_manage_leave.send_keys(list[i][0])
        sleep(1)
        page.btn_search.click()
        sleep(2)
        page.driver.find_element_by_link_text('撤销出所').click()
        sleep(0.5)
        page.money_manage_leave_cancel_submit.click()
        res = page.dialog_h2.text
        assert '成功' in res

        page.win_min_close.click()
        page.driver.switch_to.default_content()
        sleep(1)
