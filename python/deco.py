def deco(func):
    import functools
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print 'start'
        func()
        print 'end'
    return wrapper
 
@deco
def test():
    print 'Hello Decolater'
 
test()
