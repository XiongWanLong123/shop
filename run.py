from classes import web_hanshu             #导入函数文件
from web_test_data import test_data        #导入测试数据文件
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
#调用函数
url = test_data.url["url"]                    #取值url
user = test_data.login_date["username"]       #取登录用户名
pwd = test_data.login_date["password"]        #取登录密码
key = test_data.key["key"]
#函数的调用  传参
#给函数定义了一个返回值，调用的时候用一个变量来接收返回值
result = web_hanshu.search_key(driver=driver,url=url,username=user,password=pwd,key=key)

if key in result:
    print("搜索结果是正确的！")
else:
    print("用例测试不通过！")

