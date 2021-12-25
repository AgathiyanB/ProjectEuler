number = 116396280
divisor = 1
while divisor < 21:
    if number % divisor == 0:
        divisor = divisor + 1
    else:
        print "divisibility:" + str(divisor)
        number = number + 116396280
        print "number testing:" + str(number)
        divisor = 1
print number
