def fun1(x,y,z):

    sum = 0
    print "Array :"
    print z
    for num in z:
        sum += num
    print sum
    tmp = x
    x = y
    y = x
    return {'x' : x, 'y' : y , 'string' : "Fuck U"}

a = [1,2,3,4,5]

print a[0]
a.reverse()
print a[0]
a.reverse()

foo = fun1(a[0],a[1],a)

print "After function call"
print foo['x']
print foo['string']
