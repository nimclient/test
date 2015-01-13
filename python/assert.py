#!/usr/bin/env python
#-*- coding: utf-8 -*-

def f(n):
    assert n > 0, 'n must be positive'
    return "|" + str(n) + "| = " + str(n)

def g(n):
    if not n > 0:
        raise AssertionError('n must be positive')

    return "|" + str(n) + "| = " + str(n)

if __name__ == "__main__":
    print f(0)
