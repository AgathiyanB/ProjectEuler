num1 = 999
num2 = 999
pal = 0
paltest = 0
while num2 > 100:
    pal = num1*num2
    palstr = str(pal)
    if len(palstr) == 6:
        if palstr[5] == palstr[0] and palstr[4] == palstr[1] and palstr[3] == palstr [2]:
            if pal > paltest:
                paltest = pal
    else:
        if palstr[4] == palstr[0] and palstr[3] == palstr[1]:
            if pal > paltest:
                paltest = pal
    if num1 == 100:
        num1 = 999
        num2 = num2 - 1
    else:
        num1 = num1 - 1
print paltest
    
