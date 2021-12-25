ans = 0
for x in range(0,100000):
    a = ""
    c1 = 0
    c2 = [0,0,0,0,0,0,0,0,0]
    while len(a) < 9:
        c1 += 1
        a += str(c1*x)
    if len(a) == 9:
        for b in [1,2,3,4,5,6,7,8,9]:
            for cr in range(0,9):
                if a[cr] == str(b):
                    c2[b-1] = 1
    if c2 == [1,1,1,1,1,1,1,1,1]:
        if int(a) > ans:
            ans = int(a)
            print(ans)
print(ans)
