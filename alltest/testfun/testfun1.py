def fen(nums):
    a=[]
    b=[]
    for i in  nums:
        if i%2:
            a.append(i)
        else:
            b.append(i)
    return a,b

l=[20,11,52,41,30,65,84]
print(fen(l))
