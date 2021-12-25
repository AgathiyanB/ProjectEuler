a=0
term=2
fn1=1
fn2=1
buf=0
while a == 0:
    term += 1
    buf=fn1+fn2
    fn1=fn2
    fn2=buf
    if len(str(fn2))==1000:
        a=1
    print fn2
    print len(str(fn2))
print term
    
    
    
