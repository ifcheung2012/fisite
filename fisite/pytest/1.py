#
# from time import time
#
# print "4. character's join() replace '+'"
# t = time()
# s = ""
# list = ['a', 'b', 'b', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# for i in range(100000):
#    for substr in list:
#        s += substr
# print "4.1 total run time:"
# print time() - t
#
#
#
#
#


def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        a, b = b, a + b
        n = n + 1

from time import time
s = time()
fab(500)
e = time()
print "use time:", e - s

ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
es = [11, 12, 13, 10]
#for i, j in zip(ls, es):
#    print ('%s %s' % (i, j))
#print sum(ls)
#es.reverse()
#print es
#print ls[0:100:2]
zs = ls.extend(es)
print sorted(es)
print zs
# print type(zs)
# stru = u'hellow orl'
# out = stru.encode('utf-8')
# f = open('unicode.txt', "w")
# f.write(out)
# f.close()
#
# f = open('unicode.txt', "r")
# bytes_in = f.read()
# f.close()
# out_str = bytes_in.decode('utf-8')
# print out_str
#
#
