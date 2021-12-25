#Project Euler
#Problem 26
import math
import decimal

answer = [0,0]
for a in (x for x in range(0,1000) if len(list((y for y in range(1,math.ceil(x**0.5)+1) if x%y ==0))) == 1 and x !=1):
    for c in range(1,100):
        t = ((1/decimal.Decimal(a))-((1/decimal.Decimal(a))*(10**c))*10000)
        t_ = int(((1/decimal.Decimal(a))-((1/decimal.Decimal(a))*(10**c))*10000))
        if a == 521:
            print((1/decimal.Decimal(a))-((1/decimal.Decimal(a))*(10**c))*1000)
        if t and c > answer[0]:
            answer = [c,a]
            print(answer)
            break
        elif (1/decimal.Decimal(a)) == 0:
            print(c,a)
            break
print(answer)

