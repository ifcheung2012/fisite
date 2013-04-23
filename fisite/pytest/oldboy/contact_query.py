#!/usr/bin/env python
# this content comes from oldboy trainning.
# e_mail:31333741@qq.com
# qqinfo:49000448
# function: python tab config.
# version:1.1
################################################
# oldboy trainning info.
# QQ 1986787350 70271111
# site:http://www.etiantian.org
# blog:http://oldboy.blog.51cto.com
# oldboy trainning QQ group: 208160987 45039636
################################################
while True:
    input = raw_input("Please input your username:")
    if input == 'Alex':
        password = raw_input("please input your pass:")
        p = '123'
        while password != p:
            password = raw_input("Wrong passwd,input again:")
        else:
            print 'Welcome login to TriAquae!\n'
            while True:
                #match ='NO'
                match_yes = 0
                input = raw_input("\033[32mPlease input the name whom you want to search:\033[0m")
                contact_file = file('contact_list.txt')
                while True:
                    line = contact_file.readline()
                    if len(line) == 0: break
                    if input in line:
                        print 'Match item: \033[36;1m%s\033[0m' % line
                        match_yes = 1
                    #match = 'YES'
                    else:
                        pass
                        #match = 'NO'
                        #print 'No match item found.'
                    #if match != 'YES':
                #		print 'Mo match item found'
                if match_yes == 0: print 'No match item found.'

    else:
        print "Sorry, user %s not found" % input

