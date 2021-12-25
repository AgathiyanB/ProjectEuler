import itertools
k = []
def remove_duplicates(numbers):
    newlist = []
    for number in numbers:
       if number not in newlist:
           newlist.append(number)
    return newlist
t = [1,2,3,4,5,6,7,8,9]
s = set(itertools.permutations(t))
lisT = filter(lambda a: int(reduce(lambda x,y: x + y, [str(g) for g in list(a)[0:3]])) * int(reduce(lambda x,y: x + y, [str(g) for g in list(a)[3:5]])) == int(reduce(lambda x,y: x + y, [str(g) for g in list(a)[5:9]])) or int(reduce(lambda x,y: x + y, [str(g) for g in list(a)[0:1]])) * int(reduce(lambda x,y: x + y, [str(g) for g in list(a)[1:5]])) == int(reduce(lambda x,y: x + y, [str(g) for g in list(a)[5:9]])),[a for a in s])
for j in lisT:
    item = int(str(list(j)[5])+str(list(j)[6])+str(list(j)[7])+str(list(j)[8]))
    k.append(item)
k = remove_duplicates(k)
ans = reduce(lambda o,p: o+p,k)
print ans
