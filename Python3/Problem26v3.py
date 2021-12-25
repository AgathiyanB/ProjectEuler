import math
ans = [0,0]
for a in range(1,10):
    p = 1
    rl = []
    while True:
        r = (10**p)%a
        if r not in rl:
            rl.append(r)
        else:
            break
        p += 1
    if len(rl)-rl.index(r) > ans[0]:
        ans = [len(rl)-rl.index(r),a]
for a in range(10,100):
    p = 1
    rl = []
    while True:
        r = (100**p)%a
        if r not in rl:
            rl.append(r)
        else:
            break
        p += 1
    if len(rl)-rl.index(r) > ans[0]:
        ans = [len(rl)-rl.index(r),a]
for a in range(100,1000):
    p = 1
    rl = []
    while True:
        r = (1000**p)%a
        if r not in rl:
            rl.append(r)
        else:
            break
        p += 1
    if len(rl)-rl.index(r) > ans[0]:
        ans = [len(rl)-rl.index(r),a]
print(ans)
    
