def test(arg1,arg2):
    print(arg1)
    print(arg2)
    arg1=100
    arg2.append(30)
    print(arg1)
    print(arg2)
    return arg1

a=10
b=[20,40,50]
print(a)
print(b)
c=test(a,b)
print(c)
print(a)
print(b)