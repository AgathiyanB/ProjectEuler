import math
def pf(n):
    tn = n
    p = 2
    pl = []
    while tn != 1:
        if tn%p == 0:
            pl.append(p)
            while tn%p == 0:
                tn = tn/p
        else:
            p += 1
    return(len(pl))
cond = True
a = 1
c = 0
ans = a
while c != 4:
    a += 1
    if pf(a) == 4:
        c += 1
    else:
        c = 0
    if c == 1:
        ans = a
    if c == 3:
        print(ans,"3")
print(ans)
