x = 1
for iteration in range(0,7830457):
    x = int(str(x*2)[-10:])
    if iteration % 100000 == 0:
        print(x)
x = (x*28433)+1
print(int(str(x)[-10:]))
