import math
def pcheck(p):
    p_ = str(p)
    c = True
    for x in range(0,(math.ceil(len(p_)/2))+1):
        if p_[x] == p_[(len(p_)-x-1)]:
            c = c and True
        else:
            c = False
    return c
total = 0
for a in range(10,1000000):
    ba = str(bin(int(a)))[2:]
    if pcheck(a) and pcheck(ba):
        print(a,ba)
        total += a
#Because single digit palindrome numbers are a thing
print(total+1+3+5+7+9)
