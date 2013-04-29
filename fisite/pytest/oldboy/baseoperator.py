# -*- coding: gbk -*-
from txtdboperator import txtdboperator
import linecache
from atmconfig import atmconfigparser
import datetime
import string

class trans(object):
    def __init__(self,name,key):
        self.name=name
        self.key= key


    def getusertrans(self, cardnumber,sortby,startdate,enddate):
        db = "db/transmission.txt"
        opera = txtdboperator(db)
        col = linecache.getline(db,1).split()
        rels = opera.select(cardnumber=cardnumber)
        ls = []
        for item in rels:
            item[5] = item[5][-4:]     #only display last 4 number
            if item[0] >= startdate and item[0] <= enddate:
                ls.append(item)
        ls.sort(key= lambda obj:obj[col.index(sortby)])  #todo :cant sortby numberic compare
        return ls

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

    def rollbacktrans(self,**linevalue):
        db = "db/transmission.txt"
        opera = txtdboperator(db)
        return opera.delete(**linevalue)

    def counttransamount(self,ccolname,startdate,enddate,**condition):
        db = "db/transmission.txt"
        opera = txtdboperator(db)
        rels = opera.select(**condition)
        col = linecache.getline(db,1).split()
        ls,ls2 =[],[]
        for item in rels:
            if item[0] >= startdate and item[0] <= enddate:
                ls.append(item)
        for k in ls:
            ls2.append(string.atof(k[col.index(ccolname)]))
        return sum(ls2)

    def getusercurrentinfo(self,cardnumber):      #本期应还金额 = （上上期应还额+上期开支金额）  - 上期还款金额 + （本期消费金额-本期还款额） -本期调整金额 + 循环利息
        checkdate = datetime.datetime.now().strftime('%Y-%m-%d')

        thismonthfirstday = datetime.date(datetime.date.today().year,datetime.date.today().month,1)
        lastmonthlastday = (thismonthfirstday  -datetime.timedelta(1)).strftime('%Y-%m-%d')

        lastmonthfirstday = datetime.date(datetime.date.today().year,datetime.date.today().month-1,1)
        last2monthlastday = (lastmonthfirstday - datetime.timedelta(1)).strftime('%Y-%m-%d')

        newbalance,balanceBF,payment,newcharges,adjustment,interest=0,0,0,0,0,0

        balanceBF = self.counttransamount('amount','1901-01-01',last2monthlastday,cardnumber=cardnumber) \
                    + self.counttransamount('amount',last2monthlastday,lastmonthlastday,cardnumber=cardnumber,ispayment='0')
        payment  = - self.counttransamount('amount',last2monthlastday,lastmonthlastday,cardnumber=cardnumber,ispayment='1')
        newcharges = self.counttransamount('amount',thismonthfirstday.strftime('%Y-%m-%d'),checkdate,cardnumber=cardnumber,ispayment='0') \
                     + self.counttransamount('amount',thismonthfirstday.strftime('%Y-%m-%d'),checkdate,cardnumber=cardnumber,ispayment='1')

        newbalance = balanceBF -payment + newcharges - adjustment + interest

        return [newbalance,balanceBF,payment,newcharges,adjustment,interest]

    def accountreduce(self,currency,amount,cardnumber,area,descriptioin,ispayment='0'):
        msg = ('errorfound201','succeed','notenoughcredit')
        cfgs = atmconfigparser()
        creditlimit = string.atof(cfgs.getcreditlimit())

        acc = creditlimit - self.getusercurrentinfo(cardnumber)[0]
        if acc >= string.atof(amount):
            date = datetime.datetime.now().strftime('%Y-%m-%d')
            time = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
            try:
                self.appendtrans(date_trans=date,date_post=date,
                                 descriptioin=descriptioin,currency=currency,amount=amount,
                                 cardnumber=cardnumber,area_trans=area,transamount=amount,time=time,ispayment=ispayment)  #its not recommended to rollback by time;id column is prefer
                return msg[1]
            except Exception:
                self.rollbacktrans(time=time)
                return msg[0]
        else:
            return msg[2]+':left:'+str(acc)

    def withdrawcash(self,currency,amount,cardnumber,area):
        msg = ('errorfound202','succeed')
        cfgs = atmconfigparser()
        servicecharge = str(string.atof(cfgs.getservicecharge())*string.atoi(amount))
        time = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')        #maybe a bug,this time ==time in reducefunc?
        try:
            self.accountreduce(currency,amount,cardnumber,area,'withdraw-cash','0')
            self.accountreduce(currency,amount,cardnumber,area,'withdraw-cashservice-charge','0')
            return msg[1]
        except Exception:
            self.rollbacktrans(time=time)
            return msg[0]

    def payment(self,currency,amount,cardnumber,area):   #todo : not considered the currency and its exchange rate
        msg = ('errorfound203','succeed')
        cfgs = atmconfigparser()
        time = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')        #maybe a bug,this time ==time in reducefunc?
        try:
            self.accountreduce(currency,str(-string.atof(amount)),cardnumber,area,'payment','1')   #todo:not consider the rate if payment > creditlimmt
            return msg[1]
        except Exception:
            self.rollbacktrans(time=time)
            return msg[0]

if __name__ == '__main__':
    trans = trans('if','1256')
    #trans.withdrawcash('USD','50','687382738748334456','NANJING')
    #all input must be in string format
    # ls = trans.getusertrans('687382738748334456','date_trans','2012-02-01','2014-09-09')
    # for k in ls:
    #     print k
    # print '------------'
    # ls2 = trans.getuserleft('687382738748334456')
    # for k in ls2:
    #     print k
    #
    # date = datetime.datetime.now()
    print trans.getusercurrentinfo('687382738748334456')
    print trans.payment('RMB','5000','687382738748334456','nanjing')
    #print trans.accountreduce('RMB','5000','687382738748334456','nanjing','xiaofei')

