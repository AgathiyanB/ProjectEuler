testn=5
num=5
answer=0
biglis=0
while testn < 1000001:
    num=testn
    lis=1
    while num != 1:
        if num % 2 == 1:
            num = (3*num)+1
            lis = lis + 1
        else:
            num = num/2
            lis = lis + 1
    if lis > biglis:
        biglis = lis
        print testn
        answer = testn
    testn = testn + 1
print answer
print biglis
