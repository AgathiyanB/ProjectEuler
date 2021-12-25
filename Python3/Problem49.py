import math
primes = [None,None]
primes[0] = [a for a in range(1000,9999) if len([f for f in range(1,math.floor(a**0.5)+2) if a%f == 0]) == 1]
primes[1] = [list((str(b))) for b in primes[0]]
can = []
bl = []
for prime in primes[0]:
    c = 0
    d = {}
    e = []
    for item in primes[1][primes[0].index(prime)]:
        d[item] = primes[1][primes[0].index(prime)].count(item)
    for p in primes[0]:
        if p not in bl:
            dt = {}
            for item in primes[1][primes[0].index(p)]:
                dt[item] = primes[1][primes[0].index(p)].count(item)
            if dt == d:
                e.append(p)
                c += 1
                bl.append(p)
    if c >= 3:
        can.append(e)
        print(e)
for group in can:
    for i in group:
        for j in group:
            for k in group:
                if i != j:
                    if (i - j) == (j - k):
                        print(i,j,k)
