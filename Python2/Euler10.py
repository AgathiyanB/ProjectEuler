term = 5
num = 3
listnum = [2,3]
while num < 2000000:
    num = num + 2
    if (num-1)/6 == 0 or (num+1)/6:
        for n in listnum:
            if num % n ==0:
                break
        else:
            listnum.append(num)
    if num % 10000 == 1:
        print str((float(num-1)/2000000)*100) + "% done"
        
print sum(listnum[0:len(listnum)])
        
            
