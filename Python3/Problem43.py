import itertools

s = 0
for item in list(itertools.permutations("1234567890")):
    if int(item[3])%2 == 0:
        if int(item[2] + item[3] + item[4])%3 == 0:
            if int(item[5])%5 == 0:
                if int(item[4] + item[5] + item[6])%7 == 0:
                    if int(item[5] + item[6] + item[7])%11 == 0:
                        if int(item[6] + item[7] + item[8])%13 == 0:
                            if int(item[7] + item[8] + item[9])%17 == 0:
                                s += int("".join(item))
print(s)
