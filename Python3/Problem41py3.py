import math
digits = [1,2,3,4,5,6,7]
p = list(a+b*10+c*100+d*1000+e*10000+f*100000+g*1000000 for a in range(1,8) for b in range(1,8) for c in range(1,8) for d in range(1,8) for e in range(1,8) for f in range(1,8) for g in range(1,8) if a not in [b,c,d,e,f,g] and b not in [a,c,d,e,f,g] and c not in [a,b,d,e,f,g] and d not in [a,b,c,e,f,g] and e not in [a,b,d,c,f,g] and f not in [a,b,d,e,c,g] and g not in [a,b,d,e,f,c])
print(max(list(x for x in p if len(list((z for z in range(1,math.ceil(x**0.5)+1) if x%z ==0))) == 1 and x !=1)))
