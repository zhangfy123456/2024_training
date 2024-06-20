#打开百度网页
import time

from prompt_toolkit.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.baidu.com")
#窗口最大化
driver.maximize_window()

#driver.find_element(By.NAME,"wd").send_keys("小米")
driver.find_elements(By.NAME,"wd")[0].send_keys("武汉")
time.sleep(3)
driver.close()
