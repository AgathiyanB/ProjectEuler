#Project Euler
#Problem 26
import math
import decimal

answer = [0,0]
for a in (x for x in range(0,10) if len(list((y for y in range(1,math.ceil(x**0.5)+1) if x%y ==0))) == 1 and x !=1):
    for c in range(1,1000):        
        bk = 0
        st = decimal.Decimal(1000)/decimal.Decimal(a)
        st_ = (decimal.Decimal(1000)/decimal.Decimal(a))*(10**(c+3))
        print(st,st_,10**c+3)
        t = True
        for e in range(0,c+1):
            try:
                t = t and st[10+e]==st_[10+e]
            except:
                t = False
        if t:
            bk = 1
            break
    print(c,a)
    if c > answer[0] and bk == 1:
        print(c,a)
        answer = [c,a]
print(answer)

