
largest_total = 0
for base in range(0,100):
    for power in range(0,100):
        total = 0 
        for digit in str(base**power):
            total += int(digit)
        if total>largest_total:
            largest_total = total
            print(total)
            
