p = [1,5,12]
c = True
#p[i] is the sum of the pentagonal numbers, p[a] and (p[i] - p[a]) are the two numbers of consideration
while c:
    i = len(p) - 1
    for a in range(i,0,-1):
        if p[a] < (p[i] - p[i-1]):
            break
        if (p[i] - p[a]) in p:
            if (p[i] - (2*p[a])) in p:
                print(p[i] - (2*p[a]),p[i] - p[a],p[a])
                c = False
    p.append(int(round(len(p)*((3*len(p))-1)/2)))
    if len(p)%1000 == 0:
        print(len(p))
