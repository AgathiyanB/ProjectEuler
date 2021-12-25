def rec_rec(x):
    for a in xrange(1,x):
        buf = 1/float(a)
        for b in xrange(1,20):
            print buf-(buf*(10**b))
rec_rec(1000)
