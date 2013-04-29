# -*- coding: gbk -*-
__author__ = 'ifcheung'


from os import path
import linecache

#only operate one line
class txtdboperator(object):
    def __init__(self, dbfile):
        self.db = dbfile

    def validatedb(self):   #1,line endwith '\n' <== EOF, 2,valid colum and value ; 3, remove empty line
        return  False

    #not only get  line matched,but also let in matched column
    def lineincondition(self, list, dict):
        dict2 = {}
        for item in list:
            for k in dict:
                if item == dict[k]:
                    colindex = list.index(item)
                    col = linecache.getline(self.db, 1).split()

                    if col[colindex] == k:
                        dict2[k] = dict[k]
        return cmp(dict2, dict)

    def select(self, **condition):
        ls = []
        if path.exists(self.db):
            fileobj = open(self.db, 'r')
            try:
                for line in fileobj:        #todo : use regex grep excluded lines .
                    lineinfo = line.split()
                    cmp = self.lineincondition(lineinfo, condition)
                    if cmp == 0:
                        ls.append(lineinfo)
            finally:
                fileobj.close()
        return ls


    def update(self, setvdict, **condition):     #support sql injection ,security? wow
        recode = ('nomatched', ('matched', 'succeed update'), 'errorsfound101')
        msg = ''
        existrecode = -1
        if path.exists(self.db):

            try:
                fileobj = open(self.db, 'r+')
                tmp = []
                for line in fileobj:
                    lineinfo = line.split()
                    cmp = self.lineincondition(lineinfo, condition)
                    if cmp == 0:
                        existrecode = 0
                        col = linecache.getline(self.db, 1).split()
                        for k in setvdict:
                            lineinfo[col.index(k)] = setvdict[k]
                    tmp.append('    '.join(lineinfo))
                fileobj.truncate(0)
                fileobj.close()

                wfileobj = open(self.db, 'w')
                wfileobj.write('\n'.join(tmp) + '\n')
                msg = ' and '.join(recode[1]) if existrecode == 0 else recode[0]
            except Exception:
                msg = recode[2]
            finally:
                wfileobj.close()

        return msg


    def insert(self,**linevalue):
        recode = ('errorfound102', 'succeed','lessvalueerror')
        msg = recode[1]
        if path.exists(self.db):
            try:
                col = linecache.getline(self.db,1).split()
                lsoutput = [x for x in xrange(len(col))]
                if len(col)!= len(linevalue):
                    return recode[2]
                for k in linevalue:
                    lsoutput[col.index(k)] = linevalue[k]     #automatic insert in autoformat order.done!<== ls.append operating cant be in order!but y?-_-
                fileobj = open(self.db, 'a')
                fileobj.write('    '.join(lsoutput) + '\n')  #dbfile must end with '\n',otherwise you  know it!            except Exception:
                msg = recode[1]
            finally:
                fileobj.close()

        return msg


    def delete(self,**condition):
        col = linecache.getline(self.db, 1).split()
        dic = {}.fromkeys(col,'')              #second param cant be None,otherwise fileobj writeerrors
        return self.update(dic, **condition)

if __name__ == '__main__':

    # db = "userinfo1.txt"
    db = "db/userinfo.txt"
    opera = txtdboperator(db)

    #select
    # opera.select(currency='USD',expirydate='2999-09-19')
    #print opera.select(sex="female")

    #insert
    # msg = "USD   		1.0000		2999-09-99"
    # opera.insert(msg)

    #delete
    # opera.delete(currency='DE')

    #update
    # setvdict = {'expirydate': '2999-08-19', 'currency': 'RMB'}
    # opera.update(setvdict, currency='USD')


