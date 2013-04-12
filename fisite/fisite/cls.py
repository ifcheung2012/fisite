import decimal

class Website(object):
    curl ="ok"
    def __init__(self,url ):
        curl = url




import json
str = "[{'example':'ok','temp':'rong'},{'example2':'ok2','temp2':'rong2'}]"
res = json.loads(str)
print res[0]
# json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))

