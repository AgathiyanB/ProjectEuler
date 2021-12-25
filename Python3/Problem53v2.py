import math

def ncr(n,r):
    return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))

count = 0
for N in range(1,101):
    for R in range(1,N):
        if ncr(N,R) > 1000000:
            count += 1
print(count)
