count = 0
for base in range(1,10):
    power = 0
    done = False
    while not done:
        power += 1
        if len(str(base**power)) == power:
            count += 1
        else:
            done = True
print(count)
