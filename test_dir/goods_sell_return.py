import sys
from time import sleep
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from public_module.tools import xlsx_read


def goods_sell_return(page):
    """ 销售退货 """
    excel_list = xlsx_read('./tmp_file/import.xlsx', '销售')

    page.driver.find_element_by_link_text('销售业务管理').click()

    for i in range(0, len(excel_list)):
        page.driver.find_element_by_link_text('销售订单退货').click()
        page.driver.switch_to_frame(1)

        page.sell_return_prisoner.click()
        sleep(0.5)
        page.sell_return_prisoner.send_keys(excel_list[i][0])
        sleep(0.5)
        page.btn_search.click()
        sleep(1)
        js = "document.getElementsByClassName('fixed-table-body')[0].scrollLeft=1000"
        page.driver.execute_script(js)
        page.sell_center_return
        page.driver.find_element_by_css_selector('tr:nth-child({}) .fa-reply'.format(i+1)).click()
        page.driver.switch_to.default_content()
        page.driver.switch_to_frame(2)
        page.driver.execute_script('window.scrollTo(0,1000);')
        page.sell_center_return_all.click()
        page.sell_center_return_cont.send_keys('退货测试')

        page.sell_center_return_submit.click()
        page.driver.switch_to.default_content()
        res = page.sell_center_submit_result.text

        assert "处理中" in res

    goods_sell_return_query(page, excel_list)


def goods_sell_return_query(page, excel_list):
    """退货信息查询"""
    for i in range(0, len(excel_list)):
        page.driver.find_element_by_link_text('退货信息查询').click()
        page.driver.switch_to_frame(1)
        page.sell_return_query_prisoner.click()
        sleep(0.5)
        page.sell_return_query_prisoner.send_keys(excel_list[i][0])
        sleep(0.5)
        page.btn_search.click()
        sleep(1)
        result_list = page.sell_return_list
        for item in result_list:
            assert "完成" in item.text

        page.driver.switch_to.default_content()
        page.win_min_close.click()
        sleep(1)
