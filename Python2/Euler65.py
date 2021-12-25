bufn = 0
bufd = 0
buf = 0
term = int(raw_input())
def computeHCF(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in xrange(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf
def sum_digits(z):
    lis = []
    for b in xrange(len(str(z))):
        lis.append(int(str(z)[b]))
    return sum(lis)
for k in xrange(term,0,-1):
    if k == 1:
        bufn += bufd*2
    elif k == term:
        if term % 3 == 0:
            bufn = 1
            bufd = (2*k)/3
        else:
            bufn = 1
            bufd = 1
    elif k % 3 == 0:
        bufn += bufd*(2*k)/3
        buf = bufn
        bufn = bufd
        bufd = buf
    else:
        bufn += bufd
        buf = bufn
        bufn = bufd
        bufd = buf
    print k
print bufn,bufd,float(bufn)/float(bufd),sum_digits(bufn)
    
