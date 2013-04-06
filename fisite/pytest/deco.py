#def deco_functionNeedDoc(func):
#    """docstring for deco_functionNeedDoc"""
#    # TODO: write code...
#    if func.__doc__ == None:
#        print func, "has no __doc__,it's a bad habit"
#
#    else:
#        print func, ':', func.__doc__, '.'
#    return func
#@deco_functionNeedDoc
#def f():
#    print 'f() Do something'
#
#@deco_functionNeedDoc
#def g():
#    'i hava a __doc__'
#    print 'g() Do something'
#
#f()
#g()


#import time
#from functools import wraps
#
#def timeit(func):
#
#
#    def wrapper():
#
#        start = time.clock()
#        func()
#        end = time.clock()
#        print 'used:', end - start
#
#    return wrapper
#
#@timeit
#def foo():
#    print 'in foo()'
#
#foo()
#
#print foo.__name__
#
#g = lambda x,y,z:(x-y)*z
#print g(5,3,4)


def fib(num):
    if num < 2:
        print 'num is :', num
        return 1
    print 'num is :', num
    return fib(num-1)+fib(num-2)
print fib(4)
