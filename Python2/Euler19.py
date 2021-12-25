week = 0
sndy = 0
for a in range(1900,2001):
    for m in range(1,13):
        if m == 2:
            if (a%100 != 0 and a%4 == 0) or (a%100 == 0 and a%400 == 0):
                for e in range(1,30):
                    week += 1
                    if e == 1 and week%7 == 0 and a != 1900:
                        sndy += 1
            else:
                for f in range(1,29):
                    week += 1
                    if f == 1 and week%7 == 0 and a != 1900:
                        sndy += 1
        elif (m <= 7 and m%2 == 1) or (m >= 8 and m%2 == 0):
            for t in range(1,32):
                week += 1
                if t == 1 and week%7 == 0 and a != 1900:
                    sndy += 1
        else:
            for l in range(1,31):
                week += 1
                if l == 1 and week%7 == 0 and a != 1900:
                    sndy += 1
print sndy
