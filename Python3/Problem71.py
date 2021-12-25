import math

D = 7
N = 2

for d in range(3,1000000):
    for n in range(math.floor(d*(N/D)),math.ceil(d*(3/7))):
        if n*D > d*N:
            D = d
            N = n
    if d%1000 == 0:
        print(d)

print(N,D)