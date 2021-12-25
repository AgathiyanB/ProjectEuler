answers = {}
ans = 0
anst = 1
for a1 in range(1,10):
    a = str(a1)
    print(a)
    for b1 in range(1,10):
        b = str(b1)
        for c1 in range(1,10):
            c = str(c1)
            if not(b == a and a == c):
                num1 = int(b+a)
                dem1 = int(a+c)
                num2 = int(b)
                dem2 = int(c)
                if num1/dem1 == num2/dem2:
                    lcmn = num2
                    lcmd = dem2
                    print(num1,dem1,num2,dem2,"Y")
                    answers[ans] = (lcmn,lcmd,num1,dem1)
                    ans += 1
                    anst = (anst*lcmd)/lcmn
print(answers)
print(anst)
                                    
                            
                            
                        

