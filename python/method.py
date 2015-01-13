#!/usr/bin/env python
#-*- coding: utf-8 -*-


class Foo(object):
    @classmethod
    def clsmethod(cls, arg):
        print arg
        pass

    def insmethod(self, arg):
        print arg
        pass

    @staticmethod
    def stamethod(arg):
        print arg
        pass

if __name__ == "__main__":
    # class method
    Foo().clsmethod("c")
    Foo.clsmethod("c")

    # instance method
#    Foo().insmethod("c") # エラー
#    Foo.insmethod("c")   # エラー
    f = Foo()
    f.insmethod("i")

    # static method
    sf = Foo()
    Foo().stamethod("s")
    Foo.stamethod("s")
    sf = Foo()
    sf.stamethod("s")
