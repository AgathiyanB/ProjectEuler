import math
from itertools import combinations

def product(combination):
    output = 1
    for item in combination:
        output *= item
    return output

prime_numbers = [2]
for number in range(3,500000):
    prime = True
    for factor in prime_numbers:
        if number%factor == 0:
            prime = False
        if factor > number**0.5:
            break
    if prime:
        prime_numbers.append(number)        

max_totient_function = 1
max_n = 0
for number in range(2,1000001,2):
    prime_factors = []
    for prime_number in prime_numbers:
        if number%prime_number == 0:
            prime_factors.append(prime_number)
        if prime_number > number:
            break
    relative_composite_count = 0
    for length in range(1,len(prime_factors)+1):
        if length%2 == 0:
            for comb in list(combinations(prime_factors,length)):
                relative_composite_count -= math.floor(number/product(comb))
        else:
            for comb in list(combinations(prime_factors,length)):
                relative_composite_count += math.floor(number/product(comb))
            if relative_composite_count < number-(number/max_totient_function):
                break
    totient_function = number/(number-relative_composite_count)
    if max_totient_function < totient_function:
        max_n = number
        max_totient_function = totient_function
        print(max_n,max_totient_function)
    if number%1000 == 0:
        print(number)
