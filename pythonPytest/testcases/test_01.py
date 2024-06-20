# pytest用例风格一般使用函数或者方法进行调用

# 函数形式

def test_login01():
    print("现在去登录01")


# 方法形式
class TestLogin:
    def test_login02(self):
        print("现在去登录02")
