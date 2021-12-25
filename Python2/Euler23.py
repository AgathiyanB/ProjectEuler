m = int(raw_input())
xe = filter(lambda a:a<sum(filter(lambda x: a%x == 0,[x for x in xrange(1,int(a/2)+1)])),[a for a in xrange(2,m,2)])
xo = filter(lambda a:a<sum(filter(lambda x: a%x == 0,[x for x in xrange(1,int(a/2)+1)])),[a for a in xrange(1,m,2)])
x = xe + xo
i = [u for u in xrange(1,m)]
print "aight"
for o in  xrange(1,m):
    if o%2== 0:
        for n in filter(lambda k: k<=(o/2+1),xe):
            if o-n in xe:
                i.remove(o)
                break
    else:
        for t in filter(lambda t: t<=o,xo):
            if o-t in xe:
                i.remove(o)
                break
    if o in i:
        for w in filter(lambda k: k<=(o/2+1),xo):
            if o-w in xo:
                i.remove(o)
                break
print sum(i)
    
