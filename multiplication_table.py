x=1
y=1

for x in range(1,10):
    for y in range(1,10):
        print y,'*',x,'=',"%-3d" % (x*y),
        y+=1
    print ''
    x+=1

