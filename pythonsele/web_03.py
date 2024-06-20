#打开bilibili网页
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.bilibili.com")
#唯一一个
#driver.find_element(By.CLASS_NAME,'nav-search-input').send_keys("小米")
#多个 运行第一个
#driver.find_element(By.CLASS_NAME,'channel-link').click()
#多个 下标取
#driver.find_elements(By.CLASS_NAME,'channel-link')[4].click() #综艺
for ele in driver.find_elements(By.CLASS_NAME,'channel-link'):
    print(ele.text)
time.sleep(3)
driver.close()
