# -*- encoding: utf-8 -*-
__author__ = 'ifcheung'
from ftplib import FTP
import os
import socket


host = 'ftp.etiantian.org'
ftp = FTP(host)
username = 'stu389'
password = 'b9fb364fc2bc00f3'
ftp.login(username,password)
dirs = []
ftp.dir('.',dirs.append)
files = [f.split(None,8)[-1] for f in dirs if f.startswith('-')]
dirses = [f.split(None,8)[-1] for f in dirs if f.startswith('d')]

for f in files:
    outf = open(f,'wb')
    ftp.retrbinary('RETR %s' % f,outf.write)
    outf.close()

ftp.quit()






if __name__ == '__main__':
    pass