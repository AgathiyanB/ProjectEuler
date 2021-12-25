import math

c = 0
for n in range(1,100):
    for r in range(0,math.floor(n/2)+1):
        if math.factorial(n) / (math.factorial(r)*math.factorial(n-r)) > 1000000:
            c += ((math.floor(n/2)+1)-r)*2 + (n+1)%2
            break
print(c)
