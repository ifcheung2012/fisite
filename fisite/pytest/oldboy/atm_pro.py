#!/usr/bin/env python
# -*- coding: cp936 -*-
from baseoperator import trans


def validate(username,key):
    transm = trans(username,key)
    return  transm.validuser(username,key)

def printmainmenu():
    print '1. Withdraw Cash ,PRESS \'w\''
    print '2. Credit Card Payment,PRESS \'b\''
    print '3. Check Credit Card Transaction,PRESS \'t\''
    print '4. Change Password,PRESS \'p\''
def payment(username,key):
    transm = trans(username,key)
    account = transm.getuseraccount()
    payback = raw_input('pleas input your payment amount:')
    res = transm.payment('RMB',payback,account,'NANJING')
    print res

def withdrawcash(username,key):
    transm = trans(username,key)
    account = transm.getuseraccount()
    amount = raw_input('please input amount in numberic:')
    result = transm.withdrawcash('RMB',amount,account,'NANJING')
    print result
    print 'ok,success withdraw!'

def printaccount(username,key):
    transm = trans(username,key)
    account = transm.getuseraccount()
    dictres = transm.getusercurrentinfo(account)

    print str(dictres)[1:-1]
    print "still payback total:",dictres["newbalance"],'=',dictres["balanceBF"],'-',dictres["payment"],'+',dictres["newcharges"],'-',dictres["adjustment"], \
        '+',dictres["interest"]
    ls = transm.getusertrans('687382738748334456','date_trans','2012-02-01','2014-09-09')
    for k in ls:
        print k
    print '------------'

def changepasswd(username,key):
    transm = trans(username,key)
    newpass = raw_input('pleas input your passwd:')
    return transm.changepasswd(newpass)

menu = {'w':withdrawcash,'t':printaccount,'p':changepasswd,'b':payment}

def mainfunc():
    username = raw_input('please input your name:')
    key = raw_input('please input your password:')
    if not validate(username,key):
        username = raw_input('please input your name:')
        key = raw_input('please input your password:')
    while True:
        printmainmenu()
        choice = raw_input("please make a choice:")
        if choice=='x':
            import sys
            sys.exit(0)
        if menu.has_key(choice):
            menu[choice](username,key)
        else:
            print 'please make a valide choice:'
            pass


# a = 2
def deco(a=1):
    def bf_f(f):
        def decorator():
            if a == 1:
                print "before\n"
                f()
                print "after \n"
            else:
                return None
        return decorator
    return bf_f

@deco(a=2)
def hello_world():
    print ('helloworld!\n')

if __name__ == '__main__':
    mainfunc()
