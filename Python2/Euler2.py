num1 = 0
num2 = 1
num3 = 1
answer = 0
while num3 < 4000000:
    if num3 % 2 == 0:
        answer = answer + num3
    num1 = num2
    num2 = num3
    num3 = num1 + num2
print answer
