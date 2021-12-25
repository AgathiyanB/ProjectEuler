import math as mt
total = 0
lis = []
for a_ in range(0,10):
    print(lis)
    for b_ in range(0,10):
        for c_ in range(0,10):
            for d_ in range(0,10):
                for e_ in range(0,10):
                    for f_ in range(0,10):
                        for g_ in range(0,10):
                            number = int(str(a_)+str(b_)+str(c_)+str(d_)+str(e_)+str(f_)+str(g_))
                            strnum = str(number)
                            fctrl = (lambda x: mt.factorial(x) if x != 0 else 0)
                            fact = 0
                            for x in range(0,len(strnum)):
                                fact += mt.factorial(int(strnum[x]))
                            if number == fact and number > 2:
                                total += number
                                lis.append(number)
print(total)
                            
