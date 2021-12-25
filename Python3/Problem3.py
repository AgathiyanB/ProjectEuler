a = int(input())
b = a
ans = 0
for a_ in range(2,a):
    c = True
    while c:
        if b%a_==0:
            b = b/a_
            if a_ > ans:
                ans = a_
        else:
            c = False
    if a_ > b:
        break
print(ans)
        
