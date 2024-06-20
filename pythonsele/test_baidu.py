import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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

def test_search1(driver):
    '''@pytest.fixture(scope="module")
    def db_connection():
        # 连接MySQL数据库
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="pyse"
        )
        yield connection
        connection.close()'''

    # 打开百度首页
    driver.get(url)
    driver.maximize_window()

    # 定位搜索框元素
    search_box = driver.find_element(By.ID,"kw")


    # 输入超过100个字符的测试字符串
    long_string = "abcdefghijklmnopqrstuvwxyz"*4  # 104个字符
    search_box.send_keys(long_string)
    sleep(3)

    # 点击百度一下按钮
    search_button = driver.find_element(By.ID,"su")
    search_button.click()
    sleep(3)

    # 获取实际搜索框内容
    search_text = search_box.get_attribute("value")

    # 断言：搜索框最多只能输入100个字符
    assert len(search_text) == 100

    '''# 断言：点击百度一下后，实际搜索内容只取前20个字符
    expected_search_text = long_string[:20]
    assert search_text == expected_search_text'''

def test_search2(driver):

    driver.get(url)
    driver.maximize_window()

    search_box = driver.find_element(By.ID,"kw")

    long_string = "abcdefghijklmnopqrstuvwxyz"*4  # 104个字符
    search_box.send_keys(long_string)
    sleep(3)

    search_button = driver.find_element(By.ID,"su")
    search_button.click()
    sleep(3)

    search_text = search_box.get_attribute("value")

    # 断言：点击百度一下后，实际搜索内容只取前20个字符
    expected_search_text = long_string[:20]
    assert search_text == expected_search_text

def test_characters(driver):

    driver.get(url)
    driver.maximize_window()

    search_box = driver.find_element(By.ID,"kw")

    special_string = "abc>def<ghi"
    search_box.send_keys(special_string)

    search_button = driver.find_element(By.ID,"su")
    search_button.click()

    sleep(2)

    search_text = search_box.get_attribute("value")

    assert ">" in search_text
    assert "<" in search_text

