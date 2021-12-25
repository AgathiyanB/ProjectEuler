import math
import itertools
from functools import reduce

def prime_factors(x):
    b = x
    a = 1
    s = set()
    while b != 1:
        a += 1
        while b%a == 0:
            b = b/a
            s.add(a)
    return list(s)
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))
cond = True
c = 1
while cond:
    c += 1
    l = prime_factors(c)
    count = 0
    for d in powerset(l):
        if len(d) != 0:
            if len(d)%2 == 1:
                count += math.floor((c-1)/reduce(lambda x, y: x*y,d))
            else:
                count -= math.floor((c-1)/reduce(lambda x, y: x*y,d))
    if (c-1-count)/(c-1) < 15499/94744:
        cond = False
    if c%1000 == 0:
        print(c)
print(c)
