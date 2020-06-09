from time import sleep

res = ""

def result_success(page):
    global res
    try:
        page.driver.switch_to.default_content()
        res = page.base_prisoner_add_submit_result.text
        #sleep(1)
        #page.base_prisoner_add_submit_result_confirm.click()
    except:
        pass


def result_faild(page):
    global res
    try:
        page.driver.switch_to_frame(2)
        res = page.win_error.text
    except:
        pass
