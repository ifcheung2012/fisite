info =None
with open('record.txt','rb') as fs:
    info = [eachline.strip('\n').split(',') for eachline in fs if not eachline.startswith('#')]
print [item[0] for item in info if int(item[2])<60]
print sum(int(item[2]) for item in info if int(item[2])<60)
