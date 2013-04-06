from time import time
#print "1. replace list with dict"
#t=time()
#list=['a','b','is','python','jason','hello','hill','with','phone','dd','bana']
#list=dict.fromkeys(list,True) ##if uncomment this line,u c slow  action
#print list
#filter =[]
#for i in range(1000000):
#    for  find in ['is','hat','new','list','old','.']:
#        if find not in list:
#            if find not in filter:
#                filter.append(find)
#print "tootal run time:"
#print time()-t
#print filter
#
#print "2. set vs list"
#t=time()
#lista=[1,2,3,4,5,6,7,8,9,13,34,53,52,42,44]
#listb=[2,4,6,7,9,23]
#intersection=[]
##for i in range(1000000):
##    for a in lista:
##        for b in listb:
##            if a==b:
##                intersection.append(a)
##for i in range(1000000):
##    list(set(lista)&set(listb))
#
#print "total run time:        "
#print time()-t

#print "3. lazy if-evaluation"
#t=time()
#abbreviations=['cf.','e.g','ex.','etc.','fig.','i.e.','Mr.']
#for i in range(1000000):
#    for w in ('Mr.','Hat','is','chasing','the','black','cat','.'):
#        if w in abbreviations:
#            pass
#print "3.1 total time 1:"
#print time()-t
#t=time()
#abbreviations=['cf.','e.g','ex.','etc.','fig.','i.e.','Mr.']
#for i in range(1000000):
#    for w in ('Mr.','Hat','is','chasing','the','black','cat','.'):
#        if w[-1] == '.' and w in abbreviations:
#            pass
#print "3.2 total time 2:"
#print time()-t

print "4. character's join() replace '+'"
t = time()
s = ""
list = ['a', 'b', 'b', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
for i in range(100000):
    for substr in list:
        s += substr
print "4.1 total run time:"
print time() - t
t = time()
s = ""
list = ['a', 'b', 'b', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
for i in range(100000):
    for substr in list:
        s = s.join(substr)
print "4.2 total run time:"
print time() - t

print "5. list comprehension and generator expression"
t = time()
list = ['a', 'b', 'b', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
total = []
for i in range(100000):
    for w in list:
        total.append(w)
print "5.1 total run time 1:"
print time() - t

t = time()
list = ['a', 'b', 'b', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
total = []
for i in range(100000):
    total = [w for w in list]
#import pdb; pdb.set_trace()  # XXX BREAKPOINT
print "5.2 total run time 2:"
print time() - t


#import profile
#def profileTest():
#    total=1
#    for i in range(1000):
#        total = total * (i +1)
#    print total
#    return total
#if __name__=="__main__":
#    profile.run("profileTest()")
