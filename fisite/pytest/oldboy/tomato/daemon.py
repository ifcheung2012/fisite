# -*- coding: utf-8 -*-
__author__ = 'ifcheung'
from optparse import OptionParser

import commands


def addcru(crualia, interval, checkscript):
    cmd = 'cru l | grep ' + crualia + ' | wc -l'
    crucheck = 'cru a ' + crualia + ' \"*/$' + str(interval) + ' * * * * ' + checkscript + '\"'
    (status, output) = commands.getstatusoutput(cmd)
    if not status:
        if int(output) > 0:
            pass
        else:
            (s, o) = commands.getstatusoutput(crucheck)


def delcru(crualia):
    delcmd = 'cru d ' + crualia + ''   #this cmd return none,so var output get None
    (status, output) = commands.getstatusoutput(delcmd)
    if not status:
        print 'success del task from cru list'


def check(psalia, runscript):
    psexistcmd = 'ps w | grep '+ psalia +' | wc -l'
    psrestartcmd = runscript
    (status, output) = commands.getstatusoutput(psexistcmd)
    if not status:
        if int(output) > 1:
            print 'logger no need to restarting...'
        else:
            print 'restarting.......'
            import os
            os.system(psrestartcmd)



def fstrun(runlist):
    interval = '15'
    for ps in runlist:
        delcru(ps[0])
        addcru(ps[0],interval,'/opt/scripts/daemon.py -c '+ps[1])
        check(ps[1],ps[2])

runlist = [
    ('e2kinside','mlnet','nohup sh /opt/scripts/S57mlnet start &'),
    ('ftpdown','ftp.py','nohup python2 /opt/scripts/ftp.py &'),
    ('fwcheck','proxy.py','nohup /opt/bin/python2.7 /opt/goagent/proxy.py &'),
    ('btinside','transmission','nohup sh /opt/scripts/start_transmission.sh &')
]

usage = 'usage: %prog [options] arg'
parser = OptionParser(usage=usage)
parser.add_option("-c","--check",action="store",type="string",dest="checkps",help="enter the name of proccess..")
(options,args)=parser.parse_args()
if options.checkps:
    for ps in runlist:
        if ps[1]==options.checkps:
            check(options.checkps,ps[2])
else:
    fstrun(runlist)



if __name__ == '__main__':
    # runlist = [
    #     ('e2kinside','mlnet','nohup sh /opt/scripts/S57mlnet start &'),
    #     ('ftpdown','ftp.py','nohup python2 /opt/scripts/seniorftp.py &'),
    #     ('fwcheck','proxy.py','nohup /opt/bin/python2.7 /opt/goagent/proxy.py &'),
    #     ('btinside','transmission','nohup sh /opt/scripts/start_transmission.sh &')
    # ]
    # fstrun(runlist)
    # usage = 'usage: %prog [options] arg'
    # parser = OptionParser(usage=usage)
    # parser.add_option("-c","--check",action="store",type="string",dest="checkps",help="enter the name of proccess..")
    # (options,args)=parser.parse_args()
    # if options.checkps:
    #     for ps in runlist:
    #         if ps[1]==options.checkps:
    #             check(options.checkps,ps[2])
    pass