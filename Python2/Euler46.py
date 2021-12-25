m = int(input())
p = list(x for x in range(1,m,2) if list(y for y in range(1,round(x**0.5)+1) if x%y == 0) == [1]  and x != 1)
c = list(x for x in range(1,m,2) if not(x in p))
c.remove(1)
print("kk")
w = []
k = []
for a in c:
    v = 0
    for b in list(xx for xx in p if xx<a):
        t = ((a-b)/2)**0.5
        if round(t) == t:
            v = 1
    if v == 0:
        w.append(a)
print("""
""")
print(w)
