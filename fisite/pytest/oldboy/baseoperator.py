# -*- coding: gbk -*-
from txtdboperator import txtdboperator
import linecache

class trans(object):
    def __init__(self,name,key):
        self.name=name
        self.key= key

    def getusertrans(self, cardnumber,sortby,startdate,enddate):
        db = "db/transmission.txt"
        opera = txtdboperator(db)
        col = linecache.getline(db,1).split()
        rels = opera.select(cardnumber=cardnumber)
        rels.sort(key= lambda obj:obj[col.index(sortby)])  #todo :cant sortby numberic compare

        return rels

    def validuser(self):
        db = "db/userinfo.txt"
        opera = txtdboperator(db)
        return len(opera.select(username=self.name, passwd=self.key, status='1')) > 0


    def changepasswd(self, newkey):
        db = "db/userinfo.txt"
        opera = txtdboperator(db)
        setvdict = {'passwd': newkey}
        return opera.update(setvdict, username=self.name, passwd=self.key,status='1')

    def appendtrans(self,**linevalue):
        db = "db/transmission.txt"
        opera = txtdboperator(db)
        return opera.insert(**linevalue)

    def accountreduce(self,subtractor):
        pass
if __name__ == '__main__':
    trans = trans('if','1256')
    #lss = trans.getusertrans('5566','date_trans')
    # for v in lss:
    #     print v
    # print  trans.validuser('if', '1256')
    # trans.changepasswd('if','1256','1256')
    #print trans.appendtrans(date_trans='2013-04-05',date_post='2013-04-06',descriptioin='AAA',currency='RMB',amount='234',cardnumber='4456',area_trans='NANJING',transamount='1932')

    start,end = '2013-04-05','2012-04-05'
    print start > end
    print end > '2012-04-06'
