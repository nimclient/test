#-*- coding: utf-8 -*-

class Hoge(object):
    default_value = 'hogehoge'

    def __init__(self, value=None):
        if value:
            self.value = value
        else:
            self.value = self.default_value

    def get_value(self):
        return self.value

#hoge = Hoge()
hoge = Hoge('test')
print(hoge.get_value())
