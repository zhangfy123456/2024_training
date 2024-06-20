#打开bilibili网页
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.bilibili.com")
#1.找到输入框位置，输入小米
driver.find_element(By.CLASS_NAME,'nav-search-input').send_keys("小米")
#2.找到搜索框位置，点击搜索
driver.find_element(By.CLASS_NAME,'nav-search-btn').click()
time.sleep(3)
driver.close()
