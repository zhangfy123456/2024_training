#打开百度网页
import time

from prompt_toolkit.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.baidu.com")
#窗口最大化
driver.maximize_window()

#driver.find_element(By.LINK_TEXT,"新闻").click()
#driver.find_elements(By.LINK_TEXT,"新闻")[0].click()
driver.find_elements(By.PARTIAL_LINK_TEXT,"闻")[0].click()
time.sleep(3)
driver.close()
