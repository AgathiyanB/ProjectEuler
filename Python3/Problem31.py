import math
count = 0
a = []
for _1 in range(0,201):
    print(_1)
    for _2 in range(0,math.floor((200-_1)/2)+1):
        for _5 in range(0,math.floor((200-_1-(_2*2))/5)+1):
            for _10 in range(0,math.floor((200-_1-(_2*2)-(_5*5))/10)+1):
                for _20 in range(0,math.floor((200-_1-(_2*2)-(_5*5)-(_10*10))/20)+1):
                    for _50 in range(0,math.floor((200-_1-(_2*2)-(_5*5)-(_10*10)-(_20*20))/50)+1):
                        for _100 in range(0,math.floor((200-_1-(_2*2)-(_5*5)-(_10*10)-(_20*20)-(_50*50))/100)+1):
                            if (_1*1)+(_2*2)+(_5*5)+(_10*10)+(_20*20)+(_50*50)+(_100*100) == 200:
                                count += 1
                                if _1 == 200:
                                    print([_1,_2,_5,_10,_20,_50,_100])
print(count)
