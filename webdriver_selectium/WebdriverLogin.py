from selenium import webdriver
import requests

# https://npm.taobao.org/mirrors/chromedriver/2.37/
# 下载最新 https://npm.taobao.org/mirrors/chromedriver/
#sudo python -m pip install selenium
chromePath = r'/Users/xxxxxx/xxxx/python/hack_chromedriver/chromedriver'

wd = webdriver.Chrome(executable_path= chromePath)

loginUrl = 'https://weibo.com/login.php'
wd.get(loginUrl) #进入登陆界面
wd.find_element_by_xpath('//*[@id="loginname"]').send_keys('xxxxxxxx') #输入用户名
wd.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input').send_keys('xxxxxxxx') #输入密码
wd.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click() #点击登陆

print(wd.session_id)
req = requests.Session() #构建Session
cookies = wd.get_cookies() #导出cookie
for cookie in cookies:
    req.cookies.set(cookie['name'],cookie['value']) #转换cookies

# test = req.get('your logined url request test')
# print(test)



# wd.close()


#session="9593f313e629618e74e52661fa809a8b", element="0.34697422054588056-1"
#session="49c97f0fef2fdd5f420ed527ec6a72a3", element="0.011029381734686705-1"
