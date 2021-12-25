def lol(f):
    c = 1
    t = f
    r = 1
    while t > 1:
        r = r + 1
        p = 0
        while t % r == 0:
            t = t / r
            p = p + 1
        if p != 0:
            c = c*(p+1)
    return c
trinum = 0
for i in xrange(0,1000000):
    trinum = trinum + i
    div = lol(trinum)
    if div >= 500:
        break
print trinum
print div
