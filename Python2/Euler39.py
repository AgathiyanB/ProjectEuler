ans = 0
aum = 0
for a in range(1,1001):
    num=0
    for b in range(1,a):
        for c in range(b,a):
            if (b+c+((b**2+c**2)**0.5)) == a:
                num += 1
    if num > ans:
        ans = num
        aum = a
        print aum
        print ans
print aum
