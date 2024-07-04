class Catch:
    @classmethod
    def catch(cls, id):
        i = id + 1
        print(f"我的幸运数字是{i}")
        return i * 2

    @classmethod
    def update(cls, id):
        i = id + 5
        #print(f"我的幸运数字是{i}")
        return i * 3 + 1