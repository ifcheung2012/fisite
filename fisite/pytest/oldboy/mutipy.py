# -*- coding: utf-8 -*-
__author__ = 'ifcheung'
import os
from multiprocessing import *
import threading

def test():
    while True:
        65533+3774


if __name__ == '__main__':
    multi = True
    if multi:
        print 'multi ...'
        for n in xrange(5):
            print "proc(%d) start ..." % n
            p = Process(target=test,args=[])
            p.start()
    else:
        print 'single ...'
        for n in xrange(5):
            print "proc(%d) start ..." % n
            p = threading.Thread(target=test,args=())
            p.start()



