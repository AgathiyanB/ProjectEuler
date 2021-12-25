import math

def test_prime(par):
    prime = True
    for factor in range(2,math.ceil(par**0.5)+1):
        if par%factor == 0:
            prime = False
    return prime

done = False
prime_count = 0
total_count = 1
side_length = 1
while not done:
    side_length += 2
    total_count += (side_length-1)*4
    for multiplier in range(1,4):
        if test_prime(total_count-(multiplier*(side_length-1))):
            prime_count += 1
    if prime_count/(((side_length-1)*2)+1) < 0.1:
        print(side_length)
        done = True
