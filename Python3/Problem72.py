import math

def prime_check(x):
    for f in range(2,math.ceil(x**0.5)+1):
        if x % f == 0 and x != f:
            return False
    return True
pd = {}
for a in range(2,1000000):
    tmp = a
    div = 1
    plist = []
    while tmp == a:
        div += 1
        if tmp % div == 0:
            plist.append(div)
    plist.append(pd[tmp])
    pd[a] = plist
print(pd)

'''
count = 999999
for x in range(2,1000000):
    pdem = 1000000-x
    print(x)
    if prime_check(x):
        tmp = set()
        for a in range(2*x,1000001,x):
            tmp.add(a)
        pd[x] = tmp
        count += 1000000-len(tmp)
    else:
        plist = prime_factors(x)
        numset = set(a for a in range(0,1000001))
        mainset = pd[plist[0]]
        for a in plist[1:]:
            mainset = mainset.union(pd[a])
        count += 1000000-x-len(mainset.intersection(numset))
print(count)
'''
