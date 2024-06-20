#打开bilibili网页
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.bilibili.com")

driver.find_element(By.TAG_NAME,'input').send_keys("小米")
driver.find_elements(By.TAG_NAME,'a').send_keys("小米") #不推荐
time.sleep(3)
driver.close()
