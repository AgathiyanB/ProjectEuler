def quad_test(a,b):
    n = -1
    p = 0
    while p == 0:
        n += 1
        t = n**2 + (a*n) + b
        pt = 1==len(filter(lambda x: t%x==0,[x for x in xrange(1,int(abs(t)**0.5)+1)]))
        if pt:
            pass
        else:
            p = 1
            return [n-1,a*b]
ch = [0,0]
for y in xrange(-1000,1000):
    for z in xrange(-1000,1000):
        l = quad_test(y,z)
        if l[0]>ch[0]:
            ch = l
            print ch
print ch
        
