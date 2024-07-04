from exec.exe3 import Bunch


class Catch:
    @classmethod
    def catch(cls, id):
        Bunch.bunch(id)
        print(f"我的幸运数字是{id}")
        return id * 2

    @classmethod
    def update(cls, id):
        i = id + 5
        # print(f"我的幸运数字是{i}")
        return i * 3 + 1
