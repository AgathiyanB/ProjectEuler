mult = 0
answer = 0
while mult < 1000:
    if mult % 3 == 0:
        answer = mult + answer
        mult = 1 + mult
    elif mult % 5 == 0:
        answer = mult + answer
        mult = 1 + mult
    else:
        mult = 1 + mult
print answer
