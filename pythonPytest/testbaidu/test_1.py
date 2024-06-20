import requests

BAIDU_URL = "https://baidu.com/s"


def test_empty():
    response = requests.get(BAIDU_URL)
    assert "https://baidu.com/s" in response.url