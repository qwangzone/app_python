from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
#from selenium import webdriver
import time

desire_caps = {'platformName':'Android',
               'deviceName':'MAX',
               'automationName':'Appium',
               'platformVersion':'7.0',
               'appPackage':'com.meizu.mzbbs',
               'appActivity':'.ui.LoadingActivity',
               'noReset':True}
driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',desired_capabilities=desire_caps)
# driver.find_element_by_android_uiautomator("text(\"1\")").click()
# driver.find_element_by_android_uiautomator("text(\"5\")").click()
# driver.find_element_by_android_uiautomator("text(\"9\")").click()
# driver.find_element_by_android_uiautomator("text(\"del\")").click()
# driver.find_element_by_android_uiautomator("text(\"+\")").click()
# driver.find_element_by_android_uiautomator("text(\"6\")").click()
# driver.find_element_by_android_uiautomator("text(\"=\")").click()
# time.sleep(3)
# result = driver.find_element_by_id('com.android.calculator2:id/formula').text
# print(result)
# wq = driver.find_elements_by_class_name('android.widget.Button')
# print(len(wq))
# for i in wq:
#     print(i.text)
time.sleep(5)
# a = driver.find_element_by_xpath("//android.widget.LinearLayout/android.support.v7.app.a.c[1]/"
#                                   "android.widget.TextView").text
# print(a)
# driver.find_element_by_xpath("//android.widget.LinearLayout/android.widget.LinearLayout[2]/"
#                              "android.view.ViewGroup/android.widget.RadioButton").click()
#driver.find_element_by_id("com.cubic.autohome:id/tv_cardbox_title").click()
buttons = driver.find_elements_by_id("com.meizu.mzbbs:id/ha")

print(len(buttons))
contexts = driver.contexts
print(contexts)

title = driver.find_element_by_xpath("//android.support.v7.app.a.c[2]/android.widget.TextView").text
print(title)
#driver.find_element_by_xpath("//android.support.v7.app.a.c[2]/android.widget.TextView").click()
action = TouchAction(driver)
#action.press(274,1283).release().perform()
action.tap(buttons[1]).perform()
time.sleep(3)
buttons[1].click()
time.sleep(3)
buttons[2].click()
time.sleep(3)
buttons[3].click()
time.sleep(3)
#driver.find_element_by_android_uiautomator("text(\"论坛\")").click()
#time.sleep(20)
#driver.close_app()