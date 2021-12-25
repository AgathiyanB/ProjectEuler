answer = 2
number = 2
prime_numbers = [2]
while True:
    number += 1
    prime = True
    for factor in prime_numbers:
        if number%factor == 0:
            prime = False
        if factor > number**0.5:
            break
    if prime:
        answer *= number
        prime_numbers.append(number)
    if answer >= 1000000:
        answer /= number
        break
print(answer)
