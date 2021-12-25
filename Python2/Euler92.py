import itertools
hm = int(raw_input())
ensy = 0
lisref = []
lisy = []
lisc = []
for y in xrange(1,hm + 1):
    test1 = []
    if len(str(y)) != 1:
        for g in xrange(1,len(str(y))):
            if int(str(y)[g]) >= int(str(y)[g-1]):
                test1.append(1)
    if len(test1) == len(str(y))-1 or len(str(y)) == 1:
        lisref.append(len(set(itertools.permutations(str((10**(7-len(str(y))))*y)))))
        lisy.append(y)
        lisc.append(y)
while reduce(lambda x,y:x*y,filter(lambda j: j != 89,lisy) + [1]) != 1:
    ensy += len(filter(lambda y: y==1,lisy))
    lisy = filter(lambda u:u!=0,[reduce(lambda y,a: y+a,filter(lambda h: h !=0,[int(str(y)[a])**2 for a in xrange(len(str(y)))])) for y in map(lambda x: 85 if x == 89 else x,lisy)])
    print reduce(lambda x,y:x*y,filter(lambda j: j != 89,lisy) + [1])%10
total = 0
for k in xrange(0,len(lisy)):
    if lisy[k] == 89:
        total += lisref[k]
print total

