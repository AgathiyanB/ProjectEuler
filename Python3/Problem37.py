import math
xtra = [2,3,5,7]
def Condition(x):
    print(x)
    c = True
    for a in range(0,len(x)):
        if (int(x[a:]) in plist or int(x[a:]) in xtra) and (int(x[:a+1]) in plist or int(x[:a+1]) in xtra):
            c = True and c
        else:
            c = False
    return c
ans = []
plist = list(x for x in range(10,1000000) if len(list((y for y in range(1,math.ceil(x**0.5)+1) if x%y ==0))) == 1 and x !=1)
plis = list(j for j in plist if int(str(j)[0]) in xtra and len(list(o for o in range(1,len(str(j))) if int(str(j)[o])%2 == 0)) == 0)
for pstr in plis:
    p = str(pstr)
    if Condition(p):
        print(p)
        ans.append(int(p))
print(ans)
print(sum(ans))
