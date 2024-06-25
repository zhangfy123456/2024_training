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

@pytest.mark.parametrize("special_string,expected_result", [
    ("小米武汉"*10,"小米武汉"*10),
    ("12345"*18,"12345"*18),
    ("abcde"*20,"abcde"*20),
    ("小米公司"*26,"小米公司"*20),
    ("1234567890"*11,"1234567890"*10),
])

def test_characters(driver,special_string,expected_result):
    # 打开百度首页,窗口最大化
    driver.get(url)
    driver.maximize_window()

    # 定位百度搜索框，输入
    search_box = driver.find_element(By.ID,"kw")
    search_box.send_keys(special_string)

    sleep(2)
    # 获取输入框的文本内容
    search_text = search_box.get_attribute("value")

    # 验证是否符合预期
    assert search_text == expected_result
