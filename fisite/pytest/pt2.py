# alist = [1, 2, 3, 4]
# print 'alist[:3]:', alist[:3]
# print 'alist[2:]:', alist[2:]
#
#
# adict = {'host': 'earth', 'port': '80'}
# adict['port'] = 50
# print adict.keys()
# print '------'
# for key in adict:
#    print key, adict[key]
# for k in adict.keys():
#    print k


# list
# squared = [x**2 for x in range(8) if not x % 2]
# print squared
#
# try:
#    filename = raw_input('pls enter a name:')
#    fobj = open(filename, 'r')
#    for eachline in fobj:
#        print eachline
#    fobj.close()
# except IOError, e:
#    print 'file open error:', e


# print 'ok let\'s \
#        go \n ?;'
# print 'otherfile!'


# foolist = [123, 'xba', 342.23, 'abc']
# print foolist[::-1]
#
#
# a = 1.0
# print id(a)
# b = 1.0
# print id(b)
# b = 1
# print id(b)
# foolist = [123, 'xba', 342.23, 'abc']
# print foolist
# print id(foolist)
# foolist[2]='bma'
# print foolist
# print id(foolist)
# c = 1.01
# print id(c)
# d = 1.01
# print id(d)
# print cmp(a, c)
# print cmp(c, d)
# print str(a)
# print repr(a)

# num = 'this is my world'
# print isinstance(num, (int, long, float))
# print 'a number of type:', type(num).__name__

#longint=-999993882983923242342388383994893884L
#print longint**4
print 2<<32
num = 2-2j
print num.real
print num.imag
print num.conjugate()

