import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

url = "https://www.baidu.com"

@pytest.fixture
def driver():
    # 初始化浏览器
    driver = webdriver.Chrome()
    yield driver
    # 测试完成后关闭浏览器
    driver.close()

@pytest.mark.parametrize("special_string", [
    ("123456"*3),
    ("as>df1fg"*2),
    ("as>df<fg"*2),
    ("as>df<fg"*3),
])

def test_characters(driver,special_string):
    # 打开百度首页,窗口最大化
    driver.get(url)
    driver.maximize_window()

    # 定位百度搜索框，输入
    search_box = driver.find_element(By.ID,"kw")
    search_box.send_keys(special_string)

    '''search_text1 = search_box.get_attribute("value")
    print(len(search_text1))'''

    # 点击“百度一下”按钮
    search_button = driver.find_element(By.ID,"su")
    search_button.click()

    sleep(2)
    # 获取实际的搜索关键词
    search_text = search_box.get_attribute("value")

    # 获取预期
    expected_result = special_string[:100].replace("<", "").replace(">", "")[:20]

    # 看是否符合预期
    assert search_text == expected_result

