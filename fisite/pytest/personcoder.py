import json


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return 'person object name :%s , age : %d' % (self.name, self.age)

# if __name__ == '__main__':
#    p = Person('peter',22)
#    print p
p = Person('petr', 21)
print json.dumps(p)

# class MyEncoder(json.JSONEncoder):
#    def default(self, obj):
#        d = {}
#        d['__class__'] = obj.__class__.__name__
#        d['__module__'] = obj.__module__
#        d.update(obj.__dict__)
#        return d
#
#
# class MyDecoder(json.JSONDecoder):
#    def __init__(self):
#        json.JSONDecoder.__init__(self, object__hook=self.dict2object)
#
#    def dict2object(self, d):
#        if '__class__' in d:
#            class_name = d.pop('__class__')
#            module_name = d.pop('__module__')
#            module = __import__(module_name)
#
#            class_ = getattr(module, class_name)
#            args = dict((key.encode(
#                'ascii'), value) for key, value in d.items())
#            inst = class_(**args)
#        else:
#            inst = d
#        return inst
# d = MyEncoder().encode(p)
# o = MyDecoder().decode(d)
#
# print d
#
# print type(o), o
