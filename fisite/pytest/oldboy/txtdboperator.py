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
    def lineincondition(self,line,dict):
        colinfo = linecache.getline(self.db,1).split()
        if line.strip()!='':
            lineinfo = line.split()
            res = []
            for k in dict:
                kindex=colinfo.index(k)
                if lineinfo[kindex]!=dict[k]:
                    break
                else:
                    res.append(k)
            return lineinfo if len(res)==len(dict) else None
        return None


    #not only get  line matched,but also let in matched column
    def select(self, **condition):
        ls = []
        if path.exists(self.db):
            fileobj = open(self.db, 'r')
            try:
                for line in fileobj:
                    lineinfo = self.lineincondition(line,condition)
                    if lineinfo:
                        ls.append(lineinfo)
            finally:
                fileobj.close()
        return ls



    def update(self, setvdict, **condition):     #support sql injection ,security? wow
        recode = ('nomatched', ('matched', 'succeed update'), 'errorsfound101')
        msg = ''
        existrecode = -1
        if path.exists(self.db):
            fileobj = open(self.db, 'r+')
            tmp = []
            colinfo = linecache.getline(self.db,1).split()
            for line in fileobj:
                lineinfo1 = line.split()
                if line.strip()!='':
                    lineinfo = self.lineincondition(line,condition)
                    if lineinfo:
                        existrecode = 0
                        for k in condition:
                            kindex=colinfo.index(k)
                            for vk in setvdict:
                                if k == vk:
                                    lineinfo[kindex]=setvdict[vk]
                        tmp.append('    '.join(lineinfo))
                    else:
                        tmp.append('    '.join(lineinfo1))
            msg = ' and '.join(recode[1]) if existrecode == 0 else recode[0]
            if existrecode == -1:
                fileobj.close()
                return msg
            fileobj.truncate(0)
            fileobj.close()
            wfileobj = open(self.db, 'w')
            wfileobj.write('\n'.join(tmp) + '\n')

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





