from selenium import webdriver
from time import sleep

# 无界面模式
# opt = webdriver.ChromeOptions()
# opt.set_headless()
# chrome = webdriver.Chrome(options=opt)

chrome = webdriver.Chrome()
chrome.get('https://mail.163.com/')
sleep(1)

# 点击密码登录，切换到
chrome.find_element_by_id('switchAccountLogin').click()
# 用户名
user = input('请输入账号：')
# 密码
pwd = input('请输入密码：')

# 需先跳转到iframe框架
chrome.switch_to.frame(0)

sleep(2)
# 填写

chrome.find_element_by_xpath("//input[@name='email']").send_keys(user)
sleep(2)
chrome.find_element_by_xpath("//input[@name='password']").send_keys(pwd)
sleep(2)
# 点击登录
chrome.find_element_by_id('dologin').click()

# 打印信息
print(chrome.page_source)
sleep(3)

# 登录后截图
chrome.save_screenshot('./登录后页面.png')
sleep(2)
chrome.close()
chrome.quit()
