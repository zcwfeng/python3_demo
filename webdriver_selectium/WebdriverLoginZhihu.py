import time
import requests
from selenium import webdriver
chromePath = r'/Users/zcw/dev/python/hack_chromedriver/chromedriver'
wd = webdriver.Chrome(executable_path= chromePath)
wd.get()
time.sleep(45)#设定45秒睡眠，期间进行手动登陆。十分关键，下面有解释。
cookies = wd.get_cookies()#调出Cookies
req = requests.Session()
for cookie in cookies:
    req.cookies.set(cookie['name'],cookie['value'])
req.headers.clear()

print(cookies)
# test = req.get('待测试的链接')
