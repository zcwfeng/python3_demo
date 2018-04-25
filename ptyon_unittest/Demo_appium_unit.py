# pip3 install Appium-Python-Client

import unittest
import io
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
desired_caps = {}
desired_caps['platformName'] = 'iOS'
desired_caps['platformVersion'] = '11.3'
desired_caps['deviceName'] = 'iPhone X'
desired_caps['bundleId'] = 'com.howtoname.englishlearner'
# desired_caps['udid'] = '43b9c210056155d04651099442a7dc6d15117e42'
desired_caps['app'] = '/Users/zcw/Library/Developer/Xcode/DerivedData/EnglishLearner-bydjgmykbzlcuvhhczzfyjwllcmu/Build/Products/Debug-iphoneos/EnglishLearner.app' # 必须先将项目打包ipa，此处传入ipa 路径
driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
el = driver.find_element_by_name('tableView').click() # Button 是通过appium 采集到的对应按钮的id
# action = TouchAction(driver)
# action.tap(el).perform() # 执行点击事件
driver.sleep(5)

driver.quit()
