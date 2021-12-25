dictn={}
perm=0
for a in range(2,101):
    for b in range(2,101):
        try:
            print dictn[a**b]
        except KeyError:
            dictn[a**b] = "a"
            perm += 1
print perm
