#打开百度网页
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#窗口最大化
driver.maximize_window()
driver.get("https://www.baidu.com")
'''#id定位
driver.find_element(By.CSS_SELECTOR,"#kw").send_keys("小米")
driver.find_element(By.CSS_SELECTOR,"#su").click()'''



time.sleep(3)
driver.close()
