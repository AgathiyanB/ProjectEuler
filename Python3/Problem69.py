import math
prime_numbers = [2]
for number in range(3,500001):
    prime = True
    for factor in prime_numbers:
        if number%factor == 0:
            prime = False
        if factor > number**0.5:
            break
    if prime:
        prime_numbers.append(number)        

def prime_factors(number):
    factor_list = set()
    for factor in prime_numbers:
        if number%factor == 0:
            factor_list.add(factor)
            factor_list.add(int(number/factor))
        if factor > number**0.5:
            factor_list.add(number)
            break
    return factor_list

prime_factor_dict = {}
max_totient_function = 0
max_n = 0
for number in range(2,1000001):
    prime_factor_dict[number] = prime_factors(number)
    relative_prime_count = 1
    for relative_prime in range(2,number):
        if len(prime_factor_dict[number] & prime_factor_dict[relative_prime]) == 0:
            relative_prime_count += 1
        if max_totient_function > number/relative_prime_count:
            break
    totient_function = number/relative_prime_count
    if max_totient_function < totient_function:
        max_n = number
        max_totient_function = totient_function
        print(max_n,max_totient_function)
    if number%1000 == 0:
        print(number)

