a = 1
d = 1
for b in xrange(3,1002,2):
    for c in xrange(0,4):
        a += (b+1)-2
        d += a
        print a,d,(b+1)-2
print d
