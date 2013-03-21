filepath = 'record.txt'
scores = []
try:
    f = file(filepath)
    while True:
        line = f.readline()
        if len(line)==0 :
            break
        if line.startswith('#'):
            continue
        temp = line.split(',')
        if temp[2] < 60:
            print temp[0] + 'less than 60 points'
        if temp[0].startswith('l'):
            print temp[0] + ' name startswith l'
        if int(temp[2])< 60 :
            scores.append(int(temp[2]))
except :
    print 'error'

print  sum(scores)
