d = 0
for a in xrange(2,1000000):
    c = 0
    for b in xrange(0,len(str(a))):
        c += int(str(a)[b])**5
    if a == c:
        d += a
        print a,d
