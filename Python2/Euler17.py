ref1 = [0,3,3,5,4,4,3,5,5,4]
#one to nine, step 1
ref2 = [3,6,6,8,8,7,7,9,8,8]
#ten to nineteen, step 1
ref3 = [0,0,6,6,5,5,5,7,6,6]
#twenty to ninety, step 10
chck = {}
tot = 0
for i in range(1,1000):
    print i
    val = 0
    if 9 < i%100 and i%100 < 20:
#if number is between ten and nineteen
        val += ref2[i%10]
        val -= ref1[i%10]
    elif (i-(i-(i%100))-(i%10))/10 == 0:
#if the number has a ten digit of 0
        p=1
    else:
#if the number has a ten digit greater than or equal to 2
        val += ref3[(i-(i-(i%100))-(i%10))/10]
        print ref3[(i-(i-(i%100))-(i%10))/10]
    val += ref1[i%10]
#next step (added units and tens)
    if i%100 == 0:
#exact divisor of hundred
        val += ref1[i/100]
        val += 7
    elif (i-(i%100))/100 == 0:
#no hundred digit
        p=1
    else:
#has a hundred digit
        val += ref1[(i-(i%100))/100]
        val += 10
    chck[str(i)] = val
    tot += val
tot = tot + 11
print tot
loop = 0
while loop ==0:
    numchck = raw_input()
    print chck[numchck]
        
