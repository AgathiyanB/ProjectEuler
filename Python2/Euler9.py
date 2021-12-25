a=0
b=1
answer = 0
while answer == 0:
    a = a + 1
    if a == 1000:
        a = 1
        b = b + 1
    c=((a**2) + (b**2))**0.5
    if(a+b+c == 1000):
        print str(a) + " " + str(b) + " " + str(c)
        answer = 1
print (a*b*c)
    
