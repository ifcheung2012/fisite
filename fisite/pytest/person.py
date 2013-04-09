class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self):
        return 'person object name :%s , age : %d' % (self.name,self.age)

if __name__ == '__main__':
    p = Person('peter',22)
    print p
