#打开百度网页
import time

from prompt_toolkit.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.baidu.com")
#窗口最大化
driver.maximize_window()
#定位搜索框元素

#element = driver.find_element(By.ID,"kw")
#输入搜索的关键字
#element.send_keys('小米')
driver.find_element(By.ID,"kw").send_keys('小米')
#定位“百度一下”按钮元素
#button = driver.find_element(By.ID,"su")
#点击
#button.click()
driver.find_element(By.ID,"su").click()
time.sleep(3)
driver.close()
