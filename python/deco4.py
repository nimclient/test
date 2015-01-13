# -*- coding: utf-8 -*-

def deco(f):

    def deco2(*args, **kwargs):
        print '0'
        print args
        f(*args, **kwargs)
        print kwargs
        print '1'

    return deco2


@deco
def test_no_arg():
    print 'test'


test_no_arg()
print '----------'

@deco
def test_arg(a, b, c, d=1):
    print a, b, c


test_arg(1, 3, 5)
