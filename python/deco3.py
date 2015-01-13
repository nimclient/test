# -*- coding: utf-8 -*-

def deco(f):

    def deco2():
        print '0'
        f()
        print '1'

    return deco2


@deco
def test():
    print 'test'


test()

