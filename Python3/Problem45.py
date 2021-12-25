t = [1,3,6]
p = [1,5,12]
h = [1,6,15]
cond = True
while cond:
    if t[-1] == h[-1] and t[-1] == p[-1] and t[-1] != 40755:
        cond = False
    elif t[-1] <= p[-1] and t[-1] <= h[-1]:
        t.append(round(0.5*len(t)*(len(t)+1)))
    elif p[-1] <= t[-1] and p[-1] <= h[-1]:
        p.append(round(0.5*len(p)*(3*len(p) - 1)))
    elif h[-1] <= p[-1] and h[-1] <= t[-1]:
        h.append(round(len(h)*((2*len(h)) - 1)))
print(t[-1])
