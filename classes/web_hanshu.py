import time
def login_page(username,password,driver):
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("btnSubmit").click()

def open_url(url,driver):
    driver.get(url)
    driver.maximize_window()

def search_key(url,driver,username,password,key):
    open_url(url,driver)
    login_page(username,password,driver)
    driver.find_element_by_xpath("//span[text()='零售出库']").click()
    up_id = driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute("id")
    F_id = up_id + "-frame"
    driver.switch_to.frame(1)
    driver.find_element_by_id("searchNumber").send_keys(key)
    driver.find_element_by_xpath('//span[text()="查询"]').click()
    time.sleep(1)
    num = driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']//td[@field='number']/div").text
    return num