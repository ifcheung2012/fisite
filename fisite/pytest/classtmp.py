__author__ = 'ifcheung'
class Parrot(object):
    def __init__(self):
        self._voltage = 100000

    @property
    def voltage(self):
        """Get the current voltage."""
        return self._voltage

    @voltage.setter
    def voltage(self, new_value):
        self._voltage = new_value

def makel(n):
    return lambda x,y : (x+y) ** n

if __name__ == "__main__":
# instance
    p = Parrot()
    # similarly invoke "getter" via @property
    print p.voltage
    # update, similarly invoke "setter"
    p.voltage = 12
    print p.voltage
    f = makel(3)
    print f(3,2)

    a = "aAsmffr3idffd4bgs7Dlsf9eAF"
    print set(a),a.count('f')
    l = [(x,a.count(x)) for x in set(a)]
    print l

    l.sort(key = lambda k:k[1],reverse=True)
    print l[0]
    print l[0][0]


