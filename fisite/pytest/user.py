from libtest import lib_func
import inspect
import sys
import os.path
print (inspect.getargspec(lib_func))
print sys.path
path = '/home/ifcheung/Desktop/workspace/fisite/'
print (os.path.exists(path))
