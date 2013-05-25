#!/usr/bin/env python
# -*- coding: utf8 -*-
from baseoperator import trans
import datetime


def validate(username, key):
    transm = trans(username, key)
    return transm.validuser(username, key)


def printmainmenu():
    print '-------------------BEGIN  MENU----------------------'
    print '     1. Withdraw Cash ,PRESS \'w\''
    print '     2. Credit Card Payment,PRESS \'b\''
    print '     3. Check Credit Card Transaction,PRESS \'t\''
    print '     4. Change Password,PRESS \'p\''
    print '     5. Exit,PRESS \'x\''
    print '---------------------END MENU-----------------------'


def payment(username, key):
    transm = trans(username, key)
    account = transm.getuseraccount()
    payback = raw_input('pleas input your payment amount:')
    res = transm.payment('RMB', payback, account, 'NANJING')
    print res


def withdrawcash(username, key):
    transm = trans(username, key)
    account = transm.getuseraccount()
    amount = raw_input('please input amount in numberic:')
    result = transm.withdrawcash('RMB', amount, account, 'NANJING')
    print result
    print 'ok,success withdraw!'


def printaccount(username, key):
    transm = trans(username, key)
    account = transm.getuseraccount()

    thismonthfirstday = datetime.date(datetime.date.today().year, datetime.date.today().month, 1)
    sortby, begin, end = 'date_trans', str(thismonthfirstday), str(datetime.date.today)
    dictres = transm.getusercurrentinfo(account)
    print '------your account tranmissions in this month------'
    print str(dictres)[1:-1]
    print "still payback total:"
    print "本期应还金额 = 上期账单金额 - 上期还款金额 + 本期账单金额 -本期调整金额 + 循环利息"
    print dictres["newbalance"], '=', dictres["balanceBF"], '-', dictres["payment"], '+', dictres["newcharges"], '-',
    dictres["adjustment"], \
        '+', dictres["interest"]
    ls = transm.getusertrans(account, sortby, begin, end)
    print 'date_trans', 'date_post', 'descriptioin', 'currency', 'amount', 'cardnumber', 'area', 'trans', 'transamount', 'time', 'ispayment'
    for k in ls:
        print str(k[:2])[1:-1], str(k[2]).decode('gbk'), str(k[3:])[1:-1]
    print '-----------------end trans logs-------------------------'


def changepasswd(username, key):
    transm = trans(username, key)
    newpass = raw_input('pleas input your passwd:')
    print transm.changepasswd(newpass)


menu = {'w': withdrawcash, 't': printaccount, 'p': changepasswd, 'b': payment}


def mainfunc():
    username = raw_input('please input your name:')
    key = raw_input('please input your password:')
    if not validate(username, key):
        username = raw_input('please input your name:')
        key = raw_input('please input your password:')
    while True:
        printmainmenu()
        choice = raw_input("please make a choice:")
        if choice == 'x':
            import sys

            sys.exit()
        if menu.has_key(choice):
            menu[choice](username, key)
        else:
            print 'please make a valide choice:'
            pass


if __name__ == '__main__':
    mainfunc()
