import itertools
class Test(object):
    def __iter__(self):
        self.a=1
        print(self.a)
        return  self
    def dl(a):
        print("说我是")

    def __init__(self):
        self._data_list = []

    def add_data(self,data=[]):
         self._data_list.append(data)

    def build(self):
        for item in itertools.product(*self._data_list):
            print(item)