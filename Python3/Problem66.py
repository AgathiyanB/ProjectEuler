Largestx = 0
for D in (a for a in range(2,7) if a%(a**0.5) != 0):
    ValueFound = 0
    Coefficient = 0
    while ValueFound == 0:
        Coefficient += 1
        x = ((D*Coefficient)-1)**0.5
        y = ((D*Coefficient)-2)*Coefficient
        print(x,y,D)
        input()
        if x%1 == 0 and x != 1 and y%1 == 0:
            ValueFound = 1
            print(x,y,D)
            if x > Largestx:
                Largestx == x
