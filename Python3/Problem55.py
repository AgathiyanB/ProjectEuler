def reverse_digits(par):
    str_num = str(par)
    reverse_list  = []
    for digit in str_num:
        reverse_list.insert(0,digit)
    return int("".join(reverse_list))

lyc_list = []
pal_list = []
for number in range(0,10000):
    path = [number]
    if not(number in pal_list) and (not number in lyc_list):
        lychrel = True
        for iteration in range(0,50):
            step = path[-1] + reverse_digits(path[-1])
            if step == reverse_digits(step) or (step in pal_list):
                for num in path:
                    if num<10000:
                        pal_list.append(num)
                lychrel = False
                break
            elif step in lyc_list:
                break
            else:
                path.append(step)
        if lychrel == True:
            for num in path:
                if num<10000:
                    lyc_list.append(num)
print(lyc_list[0:20])
print(len(lyc_list))
