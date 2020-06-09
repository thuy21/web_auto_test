import sys
from time import sleep
from os.path import dirname,abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from public_module.tools import xlsx_read


def goods_sell(page):
    """ 供应站销售 """
    list = xlsx_read('./tmp_file/import.xlsx', '上下账')
    js = 'window.scrollTo(0,1000);'
    page.driver.find_element_by_link_text('销售业务管理').click()
    page.driver.find_element_by_link_text('供应站销售').click()
    page.driver.switch_to_frame(1)

    page.sell_center_prisoner.click()
    sleep(1)
    page.sell_center_prisoner.send_keys(list[0])
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
    page.sell_center_submit_result_confirm.click()
    sleep(1)
    page.win_min_close.click()

    page.driver.find_element_by_link_text('销售业务管理').click()
    return res
