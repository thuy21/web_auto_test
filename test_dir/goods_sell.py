import sys
from time import sleep
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from public_module.tools import xlsx_read


def goods_sell(page, is_confirm, is_check):
    """ 供应站销售 """
    list = xlsx_read('./tmp_file/import.xlsx', '上下账')
    js = 'window.scrollTo(0,1000);'

    page.driver.find_element_by_link_text('销售业务管理').click()

    for i in range(0, len(list)):
        page.driver.find_element_by_link_text('供应站销售').click()
        page.driver.switch_to_frame(1)

        page.sell_center_prisoner.click()
        sleep(1)
        page.sell_center_prisoner.send_keys(list[i][0])
        sleep(2)
        page.sell_center_prisoner_select.click()
        sleep(1)
        page.sell_center_store.click()
        page.sell_center_store_select.click()
        page.sell_center_goods.click()

        page.sell_center_goods_select.click()
        sleep(1)
        page.sell_center_submit.click()
        sleep(2)
        page.sell_center_submit_confirm.click()
        sleep(2)
        page.driver.switch_to.default_content()
        page.sell_center_submit_result_confirm
        sleep(0.5)
        res = page.sell_center_submit_result.text
        if "成功" not in res:
            is_confirm[0] = True
        sleep(1)
        assert "成功" in res

        page.sell_center_submit_result_confirm.click()
        sleep(0.5)
        page.win_min_close.click()

    if is_check == '0':
        goods_sell_check(page, 2)


def goods_sell_check(page, count):
    """订单审核"""
    js = 'window.scrollTo(0,1000);'
    # page.driver.find_element_by_link_text('销售业务管理').click()
    sleep(0.5)
    page.driver.find_element_by_link_text('销售订单审核').click()
    sleep(2)
    page.driver.switch_to_frame(1)
    # 拖动div滚动条
    js = "document.getElementsByClassName('fixed-table-body')[0].scrollLeft=1000"
    page.driver.execute_script(js)
    sleep(0.5)

    for i in range(0, count):
        page.driver.find_element_by_link_text('审核').click()
        page.sell_center_check_cont.send_keys('销售审核通过')
        page.sell_center_check_submit.click()
        page.driver.switch_to.default_content()
        res = page.sell_center_check_submit_result.text
        assert "完成" in res
        sleep(1)
        page.driver.find_element_by_link_text('确定').click()
        page.driver.switch_to_frame(1)
        sleep(0.5)
