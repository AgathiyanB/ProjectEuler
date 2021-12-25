term = 0
num = 0
while term < 10002:
    num = num + 1
    for f in range(2,num):
        if num % f == 0:
            break
    else:
        term = term + 1
        print str(num) + " is the term " + str(term)
print term
        
            
