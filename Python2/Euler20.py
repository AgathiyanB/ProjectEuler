c=1
for i in range(1,101):
    print i
    c=c*i
print c
t=0
for x in range(len(str(c))):
    print int(str(c)[x])
    t = t + int(str(c)[x])
print t
