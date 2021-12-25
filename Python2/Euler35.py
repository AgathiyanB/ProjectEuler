a = [2] + list(x for x in range(1,1000000,2) if list(y for y in range(1,round(x**0.5)+1) if x%y == 0) == [1]  and x != 1 and list(z for z in range(0,len(str(x))) if int(str(x)[z])%2 == 0) == [])
print("kk")
ans = []
for n in a:
    c = 0
    for m in range(0,len(str(n))):
        if m != 0:
            o = int((str(n)[m:len(str(n))])+(str(n)[0:m]))
        else:
            o = n
        if o in a:
            c += 1
    if c == len(str(n)):
        ans.append(n)
print(ans)
print(len(ans))
        
