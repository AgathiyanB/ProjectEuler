p1 = [2]
for a in range(3,1000000):
    cn = True
    for f in p1:
        if f > round(a**0.5):
            break
        elif a%f == 0:
            cn = False
    if cn:
        p1.append(a)
        if len(p1)%500 == 0:
            print(a)
        
b = -1
c = 0
print("y")
cond = True
ans = [0,0]

for s in range(0,len(p1)-1):
    for l in range(s+1,len(p1)):
        chain = [p1[a] for a in range(s,l)]
        if len(chain) > ans[0]:
            if sum(chain) >= 1000000:
                break
            elif sum(chain) in p1:
                ans = [len(chain),sum(chain)]
                print(ans)
print(ans)
