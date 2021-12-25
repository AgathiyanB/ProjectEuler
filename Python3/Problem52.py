import math

def digit_count(par):
    freq = {}
    str_num = str(par)
    for letter in str_num:
        try:
            freq[letter] += 1
        except:
            freq[letter] = 0
    return freq

power = 1
done = False
while not done:
    power += 1
    for num in range(10**(power-1),math.ceil((10**power)/6)):
        done = True
        freq = digit_count(num)
        for multiplier in range(2,7):
            if not freq == digit_count(num*multiplier):
                done = False
                break
        if done:
            answer = num
            break
print(answer)
