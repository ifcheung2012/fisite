# -*- coding: utf-8 -*-
__author__ = 'ifcheung'
import ConfigParser

class atmconfigparser(object):
    def __init__(self,configfile="config.ini"):
        self.cfg = ConfigParser.ConfigParser()
        self.cfgfile = configfile

    def getcreditlimit(self):
        self.cfg.readfp(open(self.cfgfile))
        return self.cfg.get("atm","creditlimit")

    def getservicecharge(self):
        self.cfg.readfp(open(self.cfgfile))
        return self.cfg.get("atm","servicecharge")



if __name__ == '__main__':
    pass