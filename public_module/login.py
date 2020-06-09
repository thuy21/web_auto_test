from time import sleep
from page.capital_page import base_widget



def init_browser(browser, base_url):
    '''初始化浏览器页面'''

    page = base_widget(browser)
    page.get(base_url)
    page.login_user.send_keys('528135')
    page.login_pass.send_keys('lecent123qwe')
    page.login_submit.click()
    page.driver.switch_to_frame(0)
    page.login_done_wait
    page.driver.switch_to.default_content()
    try:
        page.win_top_close.click()
    except:
        pass
    return page


def logout_browser(page):
    '''注销系统'''

    # page.driver.switch_to.default_content()
    page.system_logout.click()
    #page.system_login




