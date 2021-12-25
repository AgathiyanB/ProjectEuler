c = 0
cil = 1
ci = -1
ans = []
tans = 1
for a in range(0,1000001):
    ci += 1
    if ci == cil:
        c += 1
        cil = len(str(c))
        ci = 0
    d = int(str(c)[ci])   
    if a == 1 or a == 10 or a == 100 or a == 1000 or a == 10000 or a == 100000 or a == 1000000:
        print(int(str(c)[ci]),a)
        tans = tans * d
        ans.append(d)
print(tans)
