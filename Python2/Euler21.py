def factors(n):
    l = []
    gen = (i for i in range (1,int(n**0.5)+1) if n % i == 0)
    for i in gen:
        l.append(i)
        l.append(n//i)
    return l
g=[]
def amicabletest(t):
    x = sum(factors(t))-t
    y = sum(factors(x))-x
    if y == t and x != t:
        g.append(t)
        g.append(x)
for z in range(1,10001):
    amicabletest(z)
print sum(g)/2
