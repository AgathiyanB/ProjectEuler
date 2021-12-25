tes = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
for a in range(0,19):
    buf = 0
    for i in range(0,21):
        buf += tes[i]
        tes[i] = buf
fin = 0
for t in range(len(tes)):
    fin = fin + tes[t]
print fin
    
    
