#!/usr/bin/env python
# -*- coding: utf-8 -*-


def decorator(func):
    print('decorate')
    return func


# "main = decorator(main)" と等価
@decorator
def main():
    pass

if __name__ == '__main__':
    pass  # Python 処理系が解釈する時点で効果を発揮するので呼び出される必要はない
