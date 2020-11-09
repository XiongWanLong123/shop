#web自动化基础
# from selenium import webdriver              #从selenium工具里导入webdriver库
# import time                                 #导入time模块 --- python自带的
# driver = webdriver.Chrome()                 #选择Chrome这个浏览器，初始化
# driver.get("http://120.78.128.25:8765")     #打开一个网址
# driver.maximize_window()                    #浏览器窗口最大化
# time.sleep(2)                               #等待，单位默认“秒”
# driver.get("http://erp.lemfix.com")         #打开新页面
# time.sleep(2)
# driver.back()         #退回到上一个页面
# time.sleep(2)
# driver.forward()      #前进到下一个页面
# time.sleep(2)
# driver.refresh()      #刷新页面
# driver.quit()         #关闭驱动  会话关闭
# driver.close()        #关闭当前窗口，不会退出会话
#元素的定位
# from selenium import webdriver              #从selenium工具里导入webdriver库
# driver = webdriver.Chrome()                 #选择Chrome这个浏览器，初始化
# driver.get("http://erp.lemfix.com")         #打开一个网址
# # driver.maximize_window()                    #浏览器窗口最大化
# driver.find_element_by_id("username").send_keys("test123")     #找到有username这个id的元素，进行点击或输入内容
# driver.find_element_by_id("password").send_keys("123456")
# driver.find_element_by_id("btnSubmit").click()
#相对路径定位元素
# driver.find_element_by_xpath("//input[@id='username']").send_keys("test123")
# #层级定位
# page_text = driver.find_element_by_xpath("//div[@class='login-logo']//b").text    #找到元素位置后获取文本，赋值给变量
# print(page_text)
# #文本属性定位
# page_text02 = driver.find_element_by_xpath("//b[text()='柠檬ERP']").text
# print(page_text02)
# #包含属性值定位元素
# page_text03 = driver.find_element_by_xpath("//b[contains(text(),'柠檬')] ").text
# print(page_text03)
#包含属性值contains后面是属性名则有@，如果后面跟的是text则是text()
# text11 = driver.find_element_by_xpath("//label[contains(@title,'公共场所')]").text
# print(text11)
# page_text = driver.find_element_by_xpath("//div[@class='pull-left info']//p").text
#等待方式-智能等待
# from selenium import webdriver
# driver = webdriver.Chrome()
# import time
# driver.implicitly_wait(10)            #隐式等待，最多等待10s，提前出现就不继续等待
# driver.get("http://erp.lemfix.com")
# driver.find_element_by_id("username").send_keys("test123")
# driver.find_element_by_id("password").send_keys("123456")
# driver.find_element_by_id("btnSubmit").click()
# page_title = driver.title             #获取页面的标题，用的比较少
# print("这个页面的标题是：{}".format(page_title))
# login_user = driver.find_element_by_xpath("//div[@class='pull-left info']//p").text
# if login_user == "测试用户":                       #用例--验证登录后，获取页面用户名与预期是否一致
#     print("这个登录的用户是：{}".format(login_user))
# else:
#     print("这条测试用例不通过！")
# #点击零售出库
# driver.find_element_by_xpath("//span[text()='零售出库']").click()
#
# #切换iframe
# #通过找到元素，获取id属性(get.attribute)
# up_id = driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute("id")
# F_id = up_id + "-frame"
# #通过id进行iframe切换
# driver.switch_to.frame(F_id)
# driver.find_element_by_id("searchNumber").send_keys("4257")
# #通过元素定位(xpath)来切换iframe
# driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='{}']".format(F_id)))
# driver.find_element_by_id("searchNumber").send_keys("4257")
# #通过iframe下标切换
# driver.switch_to.frame(1)
# driver.find_element_by_id("searchNumber").send_keys("4257")
# #点击查询按钮(按钮是有区域的，所以说不是只能找“查询”这两个字，如下所示，第二种方法也可以)
# driver.find_element_by_xpath('//span[text()="查询"]').click()
# #或者  driver.find_element_by_id("searchBtn").click()
# #找到单据编号，并核对编号是否一致
# time.sleep(1)
# num = driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']//td[@field='number']/div").text
# if "4257" in num:
#     print("搜索结果是正确的！")
# else:
#     print("用例测试不通过！")
